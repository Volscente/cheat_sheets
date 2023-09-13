# Overwiew
## Definition
GitHub Actions is a continuous integration and continuous delivery (CI/CD) platform that allows you to automate your build, test, and deployment pipeline. You can configure a GitHub Actions workflow to be triggered when an event occurs in your repository.

## Components
## Workflow
A GitHub Action Workflow is a configurable automated process that is defined by a YAML file sinde the `github/workflows` folder.

Exmaple workflow `.github/workflows/github-actions-demo.yml`:
```yml
name: GitHub Actions Demo
run-name: ${{ github.actor }} is testing out GitHub Actions 🚀
on: [push]
jobs:
  Explore-GitHub-Actions:
    runs-on: ubuntu-latest
    steps:
      - run: echo "🎉 The job was automatically triggered by a ${{ github.event_name }} event."
      - run: echo "🐧 This job is now running on a ${{ runner.os }} server hosted by GitHub!"
      - run: echo "🔎 The name of your branch is ${{ github.ref }} and your repository is ${{ github.repository }}."
      - name: Check out repository code
        uses: actions/checkout@v3
      - run: echo "💡 The ${{ github.repository }} repository has been cloned to the runner."
      - run: echo "🖥️ The workflow is now ready to test your code on the runner."
      - name: List files in the repository
        run: |
          ls ${{ github.workspace }}
      - run: echo "🍏 This job's status is ${{ job.status }}."
```
### Jobs
Each GitHub Action Workflow is composed by one or more jobs, which can run in sequential or in parallel. Each job runs insides its own virtual machine runner or container. Each job has one or more steps that can run a specific script or an action.

Jobs are define in the `jobs` element inside the GitHub Action Workflow YAML file, like the job `Explore-GitHub-Actions`:
```yml
jobs:
  Explore-GitHub-Actions:
```