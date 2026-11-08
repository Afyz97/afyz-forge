# Example: Assignee picker (40 users)

Rules: P1, P2, P3, P4, A5, A15, F8

## Before

```html
<label>Assignee</label>
<select>
  <option>Select...</option>
  <option>user_014</option>
  <!-- 40 options, alphabetical by username -->
</select>
```

Problems: vague trigger (P3); developer terms instead of names (N2); no search over 40 items
(P1, F8 > 15 options); no faces (P2); no recent picks (N6); label not associated.

## After (ARIA combobox pattern)

```html
<div class="picker">
  <label for="assignee-input" class="picker__label">Assignee</label>
  <div class="picker__field">
    <svg aria-hidden="true" class="picker__icon"><use href="#icon-user-plus"/></svg>
    <input id="assignee-input" type="text" role="combobox"
           aria-expanded="true" aria-controls="assignee-list" aria-autocomplete="list"
           aria-activedescendant="opt-ravi" placeholder="Search by name or email" autocomplete="off">
  </div>

  <ul id="assignee-list" role="listbox" aria-label="People">
    <li role="presentation" class="picker__group">Recent</li>
    <li id="opt-ravi" role="option" aria-selected="false" class="is-active">
      <img src="ravi.jpg" alt="" width="24" height="24"> Ravi Kumar <span class="picker__meta">ravi@acme.my</span>
    </li>
    <li id="opt-aisyah" role="option" aria-selected="false">
      <img src="aisyah.jpg" alt="" width="24" height="24"> Aisyah binti Rahman <span class="picker__meta">aisyah@acme.my</span>
    </li>
    <li role="presentation" class="picker__group">Everyone (40)</li>
    <!-- filtered as the user types -->
  </ul>

  <!-- zero results state -->
  <div class="picker__empty" role="status" hidden>
    No one named "Ali". <button type="button">Invite Ali by email</button>
  </div>
</div>
```

Behaviour:
- Closed state is a button "Set assignee" with an icon; opening moves focus to the input.
- Up/Down move `aria-activedescendant`; Enter selects; Esc closes and returns focus to the trigger.
- Search matches name and email, case- and accent-insensitive; highlight the match.
- "Recent" shows the last 3-5 picks by this user; hide the group when searching.
- Zero-results text is announced via `role="status"` and offers a next step.
- Rows at the A7 house floor; long names truncate with the full name in the accessible name.
