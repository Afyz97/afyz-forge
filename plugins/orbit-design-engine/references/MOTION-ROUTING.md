# Motion routing for four distinct references

1. **original enterprise demo / product listing:** general enterprise visual language, shell, density, components; original link is not proof of exact CSS.
2. **User's 29.6s project-management dashboard recording (299130.mp4):** observed real UI interactions: KPI, Kanban, filters, charts, modal, theme.
3. **User's 92.47s vertical animated checklist video:** editorial/explainer motion, layered UI illustrations, kinetic typography, progress storytelling, mascot and ethical/trust design topics. It is NOT a the enterprise reference screen recording and is not proof of actual app functionality.

| Task | Start with | Add only if useful |
|---|---|---|
| Admin dashboard, CRUD, table, form, sidebar | `orbit-ui-director` + `orbit-ui-motion` | `orbit-ui-video-motion` for dashboards, `orbit-ui-components` |
| User filter / Kanban / chart / modal | Specific existing v3 skill | `orbit-ui-motion-qa` |
| Homepage hero, product onboarding, feature walkthrough | `orbit-ui-motion-storytelling` | `orbit-ui-kinetic-type`, `orbit-ui-layered-cards`, `orbit-ui-mascot-motion` |
| Motion-heavy product explainer / interactive storyboard | `orbit-ui-motion-storytelling` + `orbit-ui-kinetic-type` | `orbit-ui-layered-cards`, `orbit-ui-motion-qa` |
| Permission, cancellation, data privacy, pricing | Domain requirements + `orbit-ui-trust-consent-ux` | `orbit-ui-components`; only modest appropriate motion |
| Existing implementation “make it like video” | `orbit-ui-motion-storytelling` + `orbit-ui-motion-qa` | the corresponding specific skill |

**Safety and usability gate:** don't automatically add decorative animation, mascot, checklist/legal text or marketing-type auto-play to operational screens. Do not apply animation to conceal state, skip validation or induce an action. Preserve stable layouts and meaning.


## Reference D — 6.175-second Fernly project-management video (latest user sample)

This is distinct from the original Kinlo website, the 29-second dashboard interaction video and the ~92-second editorial explainer. **For app-shell navigation / KPI counting / range-switch choreography**, start with `orbit-ui-workspace-navigation` and `orbit-ui-metric-choreography`. For actual project workspaces also use `orbit-ui-project-workspaces`. Use `PROJECT-WORKSPACE-VIDEO-AUDIT.md` and the labelled reference frames. Avoid applying marketing title or code-panel aesthetics to actual app screens. The snippet suggests persisted accent theme with GSAP swatch feedback but does not show that change taking place in the app in these 6 seconds.

## Reference E (v7): angled login/signup card transition

| Task | Specialist | Reference |
|---|---|---|
| Login, register, password entry UI | `orbit-ui-auth-forms` + `orbit-ui-components` | `AUTH-VIDEO-AUDIT.md` |
| Diagonal blade transition, sign-in ↔ sign-up | `orbit-ui-diagonal-wipe` + `orbit-ui-motion-qa` | `AUTH-TRANSITION-PLAYBOOK.md` and visual frames |

This 5s video demonstrates a tightly scoped motion pattern, **not** an instruction to apply angled wipes to every route. Only use for paired states with a visual narrative. Respect reduced motion and keep real auth/validation semantics.
