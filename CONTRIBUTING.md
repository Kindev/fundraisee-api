# Contributing to Fundraisee

Fundraisee is our way to hopefully help creating fundraising platform easier. If you're interested in contributing, hopefully this document makes the process for contributing clear.

## Get involved

There are many ways to contribute, and many of them do not involve writing any code. Here's a few ideas to get started:

* Simply start using. Does everything work as expected? If not, we're always looking for improvements. Let us know by [opening an issue](#reporting-new-issues).
* Look through the [open issues](https://github.com/Kindev/fundraisee-api/issues). Provide workarounds, ask for clarification, or suggest labels.
* If you find an issue you would like to fix, [open a pull request](#pull-requests). Issues tagged as [_Good first issue_](https://github.com/Kindev/fundraisee-api/labels/Good%20first%20issue) are a good place to get started.
* Take a look at the [features requested](https://github.com/Kindev/fundraisee-api/labels/feature%20request) by others in the community and consider opening a pull request if you see something you want to work on.

## Reporting new issues

When [opening a new issue](https://github.com/Kindev/fundraisee-api/issues/new), always make sure to fill out the [issue template](https://raw.githubusercontent.com/Kindev/fundraisee-api/master/.github/ISSUE_TEMPLATE.md). **This step is very important!** Not doing so may result in your issue not managed in a timely fashion. Don't take this personally if this happens, and feel free to open a new issue once you've gathered all the information required by the template.

* **One issue, one bug:** Please report a single bug per issue.
* **Provide reproduction steps:** List all the steps necessary to reproduce the issue. The person reading your bug report should be able to follow these steps to reproduce your issue with minimal effort.

## Pull requests

Working on your first Pull Request? You can learn how from this free video series:

[**How to Contribute to an Open Source Project on GitHub**](https://egghead.io/courses/how-to-contribute-to-an-open-source-project-on-github)

We have a list of [beginner friendly issues](https://github.com/Kindev/fundraisee-api/labels/good%20first%20issue) to help you get your feet wet in our codebase and familiar with our contribution process. This is a great place to get started.

### Sending a pull request

Small pull requests are much easier to review and more likely to get merged. Make sure the PR does only one thing, otherwise please split it.

_Before_ submitting a pull request, please make sure the following is done…

1.  Fork the repo and create your branch from `master`. A guide on how to fork a repository: https://help.github.com/articles/fork-a-repo/

    Open terminal (e.g. Terminal, iTerm, Git Bash or Git Shell) and type:

    ```sh
    git clone https://github.com/<your_username>/fundraisee-api.git
    cd fundraisee-api
    git checkout -b my_branch
    ```

    Note: Replace `<your_username>` with your GitHub username

1. Describe your [**test plan**](#test-plan) in your pull request description. Make sure to test your changes.

All pull requests should be opened against the `master` branch.

#### Test plan

A good test plan has the exact commands you ran and their output, provides screenshots or videos if the pull request changes UI.

### What happens next?
The fundraisee team will be monitoring for pull requests. When we get one, Travis CI will run some automated tests on it first. From here, we'll need to get another person to review the changes and then merge the pull request.