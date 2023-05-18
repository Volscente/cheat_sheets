# Errors
## GitHub Desktop Stuck on "Pushing to Origin"
Open the project that you're trying to push on GitHub. Open the terminal and, from inside the root folder of the repo, type:
```
git config lfs.activitytimeout 30
```
Now close and re-open GitHub Desktop and push again.
