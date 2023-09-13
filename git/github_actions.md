# Overwiew
## Definition
GitHub Actions is a continuous integration and continuous delivery (CI/CD) platform that allows you to automate your build, test, and deployment pipeline. You can configure a GitHub Actions workflow to be triggered when an event occurs in your repository.

## Components
### Jobs
Each GitHub Action Workflow is composed by one or more jobs, which can run in sequential or in parallel. Each job runs insides its own virtual machine runner or container. Each job has one or more steps that can run a specific script or an action.