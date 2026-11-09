# Trusted Release Package (Lab 12, 20 points)

Put these here through a pull request:

| Path | What it holds |
|---|---|
| `secret-controls/` | evidence that secret scanning and push protection are enabled; the gitleaks finding before and after; how the token was externalized, scoped, rotated and revoked |
| `artifact-hash.txt` | the SHA-256 of the released artifact (from the release) |
| `release-sbom.json` | the SBOM from the same build, bound to that hash (from the release) |
| `provenance/` | the passing verification and the two failing ones (from the provenance-check run) |
| `post-deploy.md` | what you checked after deploying, and the result (from the deploy run) |
| `pipeline-run.md` | the run IDs: A, H, B, P, C |
