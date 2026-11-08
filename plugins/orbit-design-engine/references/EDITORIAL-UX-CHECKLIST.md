# Video content reference: 35 trust / compliance / humane UX points

These points are **visible themes from the uploaded explainer**, intended for contextual UX audits only. This list is **not legal advice**, not independently verified law, and not a universal set of requirements. Applicability varies by country, audience, product type and actual practices; consult appropriate legal/privacy/security specialists. Do not silently implement marketing/email permissions, policies or legal assertions based on a visual-video skill. Ask for business requirements, draft placeholders clearly, and request review before publishing.

1. Provide an appropriate privacy policy.
2. Provide terms of service.
3. Present consent-oriented cookie controls where applicable.
4. Give marketing email recipients an unsubscribe mechanism.
5. Explain and enforce defined data-retention limits.
6. Avoid fake countdown urgency timers.
7. Provide meaningful alternative text for informative images.
8. Support real keyboard navigation and focus visibility.
9. Do not claim customers/partners using logos without permission.
10. Check licenses for images, fonts and source code.
11. Offer relevant export and deletion request flows.
12. Remove deceptive or coercive design patterns.
13. Label AI-generated content where appropriate and required.
14. Provide clear affirmative acceptance of legal terms when required; do not precheck acceptance.
15. Provide a clear refund policy where applicable.
16. Allow straightforward subscription cancellation.
17. Minimize personal data collected.
18. Do not fabricate reviews.
19. Do not make unsupported marketing claims.
20. Handle children's data/parental permissions appropriately where applicable.
21. Record auditable acceptance of applicable terms.
22. Check open-source license obligations, including notices.
23. Separate optional marketing permission from mandatory terms.
24. Do not claim SOC 2 compliance without support.
25. Establish an appropriate copyright notice/takedown process; assess any designated-agent registration needs with counsel.
26. Prevent unauthorized use of customer data for AI training.
27. Clearly disclose auto-renewal terms.
28. Audit third-party SDKs, analytics and trackers.
29. Put necessary data-processing agreements in place.
30. Block nonessential trackers until appropriate consent where required.
31. Make service-provider/subprocessor information available where applicable.
32. Describe realistic uptime/service commitments.
33. Disclose charges and fees before confirmation.
34. Provide legitimate business contact details.
35. Use qualified legal review for relevant policies and launch risks.

> The video’s closing reminder says this is not legal advice and recommends a qualified lawyer review the app. Some apparent checklist step numbering in frames may shift as text animates; this is a normalized thematic extraction, not a word-for-word transcription.

## Use in app design (only when relevant)

- Consents: plain-language, unbundled options; enforce real backend choices, logged at appropriate scope; no fake “saved” state.
- Authentication/checkout: show actual terms/refund/renewal/fees, accessible links and keyboard controls; action state disabled until valid without inventing acceptance.
- Account & data: visible export/delete and cancellation pathways if offered, with confirmation and backend processing.
- Analytics & integrations: no tracker before relevant consent if required; document integrations, limits and third-party roles.
- Claims & testimonials: only show verified facts/permissions, no fake scarcity or social proof.

Use `orbit-ui-trust-consent-ux` for relevant screens. For normal dashboard work, do not load this checklist by default; it is not a design-system requirement to add legal features everywhere.
