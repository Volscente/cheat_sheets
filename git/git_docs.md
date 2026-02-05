# Notifications
## Setup Remeinder
Going to the GitHub > Settings > Schedule Remeinders it is possible to setup a Slack connection that sends you alert notitifications for certain circumstances.
# Errors
## GitHub Desktop Stuck on "Pushing to Origin"
Open the project that you're trying to push on GitHub. Open the terminal and, from inside the root folder of the repo, type:
```
git config lfs.activitytimeout 30
```
Now close and re-open GitHub Desktop and push again.

# Branches
## Naming Conventions

```
Prefix	Use Case
feat/	New features (e.g., feat/add-login, feat/llm-integration).
fix/	Bug fixes (e.g., fix/typo-in-german-word).
docs/	Documentation only changes (e.g., docs/update-readme).
refactor/	Code changes that neither fix a bug nor add a feature (cleaning up code).
chore/	Updating dependencies, build scripts, or configurations.
```
## Compare
Add the `/compare` at the end of the repository URL.
