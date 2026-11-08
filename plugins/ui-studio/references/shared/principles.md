# Design principles (DP)

Cross-cutting rules for every ui-studio skill. Cite the ID in reviews.

- **DP1 Anchor in a real subject.** Before choosing anything visual, know three things: what
  the product is, who uses it, and the one job this screen must do. If the brief is silent,
  suggest a concrete answer and get a yes before going further. Identity comes from that
  subject: its trade, its physical materials, the words insiders use. A reading app for
  primary-school children and a risk console for bank analysts share almost nothing, and their
  interfaces should show it. Work with real content from the first draft; whatever is known
  about the user is a clue, not decoration.
- **DP2 The brief outranks taste.** A direction the brief sets explicitly is followed to the
  letter, even when it names a look that `ai-defaults.md` calls a default. Personal judgment
  only fills the dimensions the brief leaves unspecified.
- **DP3 One loud thing.** Pick a single element to carry the personality and let the rest stay
  calm and disciplined. Before you call it finished, take one ornament away (the Chanel test).
  Cut any decoration that does not serve the brief.
- **DP4 Structure must mean something.** Rules, borders, numbers, eyebrows and dividers are
  information, not texture. Numbered markers (01 / 02 / 03) are reserved for things that really
  happen in order: steps, timelines, rankings.
- **DP5 Motion has to pay rent.** Allow at most one choreographed moment the user did not
  trigger (an entrance sequence or a single reveal). Staggered fade-ups on every section and
  hover animation on every card are tells, not polish. Motion that answers a user action
  (opening, expanding, confirming) is welcome when it shows what changed. Timings: M1-M2 in
  `visual-system.md`.
- **DP6 Words are part of the design.** Interface text is written from the user's side of the
  screen, in plain words, active voice and sentence case. Full rules: the **ui-ux-copy** skill (user-first-ux plugin), if installed. Placeholder
  text makes a layout feel templated as fast as a stock gradient does.
- **DP7 Review what you made.** Look at the rendered result (screenshots through Playwright when
  available) and critique it before handing it over. Keep observation ("5 of 8 testers missed
  the button") apart from interpretation ("the button is in the wrong place").
- **DP8 Polish by refining, not by adding.** On the final pass, sharpen spacing, alignment and
  type on what already exists. If the urge is to add a new element, ask instead how the existing
  ones could be better. Keep short notes on what you tried so a later pass explores something
  new.
