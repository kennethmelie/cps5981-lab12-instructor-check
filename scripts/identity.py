"""Write release-identity.json: what was built, from what, by whom, when. Emitted by the build itself."""
import json, os, hashlib, datetime, sys
art, version = sys.argv[1], sys.argv[2]
sha = hashlib.sha256(open(art, 'rb').read()).hexdigest()
env = os.environ.get
ident = {
    'artifact': os.path.basename(art), 'version': version, 'sha256': sha,
    'source_commit': env('GITHUB_SHA'), 'source_repository': env('GITHUB_REPOSITORY'),
    'build_run': f"{env('GITHUB_SERVER_URL')}/{env('GITHUB_REPOSITORY')}/actions/runs/{env('GITHUB_RUN_ID')}/attempts/{env('GITHUB_RUN_ATTEMPT')}",
    'builder': env('GITHUB_WORKFLOW_REF'), 'runner': f"{env('RUNNER_OS')}/{env('RUNNER_ARCH')} {env('ImageOS', '')} {env('ImageVersion', '')}".strip(),
    'built_at': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
}
json.dump(ident, open(os.path.join(os.path.dirname(art), 'release-identity.json'), 'w'), indent=2)
open(os.path.join(os.path.dirname(art), 'artifact-hash.txt'), 'w').write(f"{sha}  {os.path.basename(art)}\n")
print(json.dumps(ident, indent=2))
