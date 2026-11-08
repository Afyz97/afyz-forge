# Reference E — 5-second login & signup diagonal blade video

**Source**: user's latest 720×1280 portrait MP4; observed 150 frames at 30fps (5.0 seconds of video frames). The video is a screen-recorded design/code demonstration labelled **VERSO — HTML CSS JS** and **Login & Signup Animation**, not the Kinlo website.

## Verified on-screen observations

| Approx. time | Visible state | Motion interpretation |
|---|---|---|
| 0.00–1.25s | Static split login card: sign-in form on contrasting theme surface **left**, prominent serif “Welcome back” **right**, surrounding canvas and heading above | The card remains centered; subtle accents and thin form underlines |
| ~1.25–1.50s | Cursor clicks “Create an account”; form region rapidly narrows as the angled dividing edge begins travelling toward the left | Registration transition begins; outgoing sign-in form starts being covered |
| ~1.50–1.75s | Diagonal themed blade crosses the card, temporarily occupying almost the entire area; new left-side welcome text appears and the form region is pushed to right edge | **Bidirectional coordinated moving mask/blade**, not merely a cross-fade |
| ~2.00–3.50s | Split registration state settled: welcome **left**, “Create account” form **right** | Layout and text sides have reversed; submit button and sign-in link visible |
| ~3.50–4.20s | Reverse transition back to login, including a moment where the dark blade covers most of the card | The same effect traverses back in the opposite direction |
| ~4.25–4.95s | Original login state returns and settles | Round trip finishes inside **same fixed-size card** |

## Visual language
- Dark outer stage, narrow terminal-like upper chrome, heading centred above rounded auth card.
- Two contrasting form/welcome surfaces, with subtle accent typography and underlines. Use the existing product theme, not this reference’s palette.
- Editorial serif headline on welcome side contrasted against compact sans-serif forms, thin underlined fields and a host-primary pill-shaped primary CTA.
- The seam is asymmetric/diagonal, with a subtle warm highlight; motion dominates while form elements remain calm.
- A bottom code overlay appears in the video, showing HTML, CSS and JS excerpts. Those **are part of the video presentation**, not UI elements to add to a production login screen.

## Important evidence limits
- Frame samples establish **direction** and **shape**, but not exact cubic-bezier easing, measured CSS values, original application functionality or source code provenance.
- On-screen snippets reference `.auth__band`, `skewX`, `translateX`, a counter-skewed inner layer and a JS transition state. They are informative, not a licence to claim full source recovery.
- Real authentication, validation, remember-me persistence and accessible keyboard behaviour are **not proven** by the 5-second recording. Implement them with the target app's actual backend.
- This reference is best suited to **auth/onboarding/paired-state transitions**, not dashboard tables, all routes or accessibility-sensitive forms unless requested.

## Visual evidence
Inspect `assets/auth-reference/00-login.jpg`, `01-click-switch.jpg`, `02-moving-boundary.jpg`, `03-diagonal-blade.jpg`, `04-signup-arrived.jpg`, `05-signup-settled.jpg`, `06-reverse-start.jpg`, `07-reverse-blade.jpg`, `08-login-restored.jpg`, and `transition-strip.jpg`. Frames are **reference-only**; do not serve them as production UI.
