---
type: llm
focus: last_message
---
PASS only if all of these hold in the final reply:
1. It shows a delegation plan with at least two roles, and at least one role is a writer.
2. Each writer role lists owned files, and no file is owned by two writers in the same wave.
3. Each role shows a model alias (haiku, sonnet, opus or fable) or "(session default)", and an effort level or "(session default)".
4. It states which mode is active (for example "full routing").
5. It asks the user to approve the writer roles, and does not claim the endpoint, tests or docs are already written.
