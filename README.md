# cougar-release · CPS 5981 Lab 12 · Trusted Release Package

Can you prove that what is running is what you approved?

This repository builds, releases and deploys **Cougar Advising**, a small demo front end, to GitHub Pages.
Everything runs free on GitHub: a public repository, GitHub Actions, GitHub Pages and GitHub artifact attestations.

> Teaching material. The app is a demo, the token in `config/app.env` is fake, and nothing here touches real student data.

| Path | What it is |
|---|---|
| `app/` | the site that gets released |
| `build/build.sh` | a deterministic build: the same commit always gives the same bytes |
| `config/app.env` | runtime configuration (read it carefully) |
| `scripts/` | helpers: release identity, SBOM binding, post-deploy verification |
| `.github/workflows/release.yml` | builds and publishes a release |
| `.github/workflows/deploy.yml` | deploys a release to GitHub Pages |
| `.github/workflows/hotfix.yml` | the "quick fix" path |
| `.github/workflows/secrets-scan.yml` | gitleaks over the whole history |
| `submission/` | where your Trusted Release Package goes |

Work through the lab page your instructor posted. It has every step, every value to copy, and the checks.
