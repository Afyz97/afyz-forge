#!/bin/sh
# ui-studio PostToolUse hook: warn (never block) about design-token leaks and common a11y
# regressions in the file Claude just edited. Always exits 0.
# Needs a POSIX shell + grep/sed/awk (Git Bash on Windows, which Claude Code already requires).
# Disable for a session: UI_STUDIO_HOOK=off

[ "${UI_STUDIO_HOOK:-on}" = "off" ] && exit 0

input=$(cat)

# ponytail: sed-based JSON read (no jq dependency); a file_path containing an escaped quote is
# skipped. Swap to jq if that ever matters.
file=$(printf '%s' "$input" | tr -d '\n' \
  | sed -n 's/.*"file_path"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' \
  | sed 's/\\\\/\//g; s/\\/\//g')
[ -n "$file" ] && [ -f "$file" ] || exit 0

case "$file" in
  */vendor/*|*/node_modules/*|*/public/build/*|*/storage/*|*/resources/views/vendor/*|*/.next/*|*/_source/*|*.min.css) exit 0 ;;
esac

case "$file" in
  *.blade.php) kind=markup ;;
  *.tsx|*.jsx) kind=markup ;;
  *.css|*.scss) kind=style ;;
  *) exit 0 ;;
esac

out=""
add() { out="${out}$1
"; }

# grep -n results -> "Lnn [rule] message: snippet", at most 5 per rule
report() { # $1 rule, $2 message, stdin = grep -n output
  awk -v r="$1" -v m="$2" 'NR<=5 { i=index($0,":"); s=substr($0,i+1); gsub(/^[ \t]+/,"",s);
    if (length(s)>70) s=substr(s,1,70) "..."; printf "L%s [%s] %s: %s\n", substr($0,1,i-1), r, m, s }'
}

# 1. hardcoded hex colours outside token definitions
r=$(grep -nE '(^|[^&0-9A-Za-z_])#([0-9a-fA-F]{8}|[0-9a-fA-F]{6}|[0-9a-fA-F]{3,4})([^0-9A-Za-z_-]|$)' "$file" \
  | grep -vE '(--[A-Za-z0-9_-]+|\$[A-Za-z0-9_-]+)[[:space:]]*:[[:space:]]*#' \
  | grep -vE 'href=|[[:space:]]id=' \
  | grep -vE '^[0-9]+:[[:space:]]*(//|/\*|\*|\{\{--|<!--)')
[ -n "$r" ] && add "$(printf '%s\n' "$r" | report hex 'Hardcoded colour; reference a token')"

if [ "$kind" = markup ]; then
  # 2. arbitrary Tailwind values (variants like data-[state=open]: and var(--token) wrappers are fine)
  r=$(grep -nE '[a-z0-9]-\[[^]]+\]' "$file" | awk '{
      s=$0; bad=0
      while (match(s, /[a-z0-9]-\[[^]]+\]/)) {
        v=substr(s, RSTART+3, RLENGTH-4); nxt=substr(s, RSTART+RLENGTH, 1)
        if (nxt != ":" && v !~ /^(var\(--|calc\(var\(--)/) bad=1
        s=substr(s, RSTART+RLENGTH)
      }
      if (bad) print $0 }')
  [ -n "$r" ] && add "$(printf '%s\n' "$r" | report arbitrary-value 'Arbitrary Tailwind value; use or add a token')"

  # 3. inline styles (custom-property-only styles are allowed)
  r=$(grep -nE 'style="|style=\{\{' "$file" | grep -vE "style=\"[[:space:]]*--|style=\{\{[[:space:]]*\[?[\"']--")
  [ -n "$r" ] && add "$(printf '%s\n' "$r" | report inline-style 'Inline style; move to tokens/utilities unless it is dynamic geometry')"

  # 5. hover motion on many items (DP5)
  n=$(grep -oE 'hover:(scale|-?translate|shadow)' "$file" | wc -l | tr -d ' ')
  [ "$n" -ge 3 ] && add "L- [hover-motion] $n elements animate on hover (scale/translate/shadow); keep motion for where it explains something (DP5)"

  # 9. canvas inside a Livewire view without wire:ignore
  case "$file" in *.blade.php)
    if grep -q '<canvas' "$file" && grep -q 'wire:' "$file" && ! grep -q 'wire:ignore' "$file"; then
      add "$(grep -n '<canvas' "$file" | report canvas 'Canvas in a Livewire view without wire:ignore; Livewire updates will reset it')"
    fi ;;
  esac

  # 10. pinch-zoom disabled
  r=$(grep -nE 'user-scalable[[:space:]]*=[[:space:]]*(no|0)|maximum-scale[[:space:]]*=[[:space:]]*1([^.0-9]|\.0|$)' "$file")
  [ -n "$r" ] && add "$(printf '%s\n' "$r" | report zoom-disabled 'Zoom disabled; fails WCAG 1.4.4 / A3')"

  # 11. positive tabindex
  r=$(grep -nE 'tabindex="[1-9]|tabIndex=\{[1-9]' "$file")
  [ -n "$r" ] && add "$(printf '%s\n' "$r" | report tabindex 'Positive tabindex breaks focus order (2.4.3)')"
fi

# 4. focus outline removed with no focus-visible replacement anywhere in the file
if grep -qE 'outline-none|outline:[[:space:]]*(none|0)([[:space:]]*;|[[:space:]]*!|$)' "$file" && ! grep -q 'focus-visible' "$file"; then
  add "$(grep -nE 'outline-none|outline:[[:space:]]*(none|0)' "$file" | report focus-removed 'Focus outline removed with no focus-visible style (2.4.7)')"
fi

# 6. transition on every property
r=$(grep -nE 'transition-all|transition:[[:space:]]*all' "$file")
[ -n "$r" ] && add "$(printf '%s\n' "$r" | report transition-all 'transition-all; name the properties and respect reduced motion')"

if [ "$kind" = style ]; then
  # 8. spacing off the 4pt grid (values above 2px not divisible by 4)
  r=$(grep -nE '(margin|padding|gap)[a-z-]*[[:space:]]*:' "$file" | awk '{
      line=$0; bad=0; s=line
      while (match(s, /[0-9]+px/)) { v=substr(s,RSTART,RLENGTH-2)+0; if (v>2 && v%4!=0) bad=1; s=substr(s,RSTART+RLENGTH) }
      if (bad) print line }')
  [ -n "$r" ] && add "$(printf '%s\n' "$r" | report off-scale 'Spacing off the 4pt grid (L1)')"
fi

[ -z "$out" ] && exit 0

out=$(printf '%s' "$out" | sed '/^$/d' | head -n 15)
count=$(printf '%s\n' "$out" | wc -l | tr -d ' ')
name=${file##*/}
body="ui-studio token check for $file (warnings only, edit already applied):
$out
Fix what applies; ignore findings that are intentional. Rules: ui-studio quality-floor and ai-defaults."

esc() { printf '%s' "$1" | tr '\t' ' ' | sed 's/\\/\\\\/g; s/"/\\"/g' | awk '{ printf "%s\\n", $0 }'; }

printf '{"hookSpecificOutput":{"hookEventName":"PostToolUse","additionalContext":"%s"},"systemMessage":"%s"}\n' \
  "$(esc "$body")" "$(esc "ui-studio: $count design warning(s) in $name")"
exit 0
