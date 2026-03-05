# Security Policy

## Intended Users

This repository is intended for use by the student author and the course instructor for **code_3000**. It is an academic project repository used for submitting coursework.

## Security Risk Assessment

The risk level for this repository is **low**:

- No sensitive user data, credentials, or personally identifiable information (PII) is stored here.
- The code is written for educational purposes and is not deployed in any production environment.
- No API keys or secrets are committed to the repository.

## Steps Taken to Secure This Repository

The following protections are actively enforced on the default branch via a GitHub ruleset named **"Pull request approvals"**:

- **Deletion protection**: Direct deletion of the default branch is blocked.
- **No force pushes**: Non-fast-forward (force) pushes are disabled, preventing history rewrites.
- **Pull request required**: All changes must go through a pull request before merging.
- **Code owner review required**: A CODEOWNERS file is in place, and review from the designated code owner is required before a PR can be merged.
- **Merge flexibility**: Merge, squash, and rebase merge methods are all permitted.

These rules are actively enforced with no bypass actors configured, meaning no one can skip these protections.
