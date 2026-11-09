"""Bind the SBOM to the release artifact: record the artifact's SHA-256 and build identity in CycloneDX metadata."""
import json, sys
raw, out, ident = sys.argv[1:4]
s = json.load(open(raw)); i = json.load(open(ident))
comp = s.setdefault('metadata', {}).setdefault('component', {})
comp.update({'type': 'application', 'name': 'cougar-advising.tar.gz', 'version': i['version'],
             'hashes': [{'alg': 'SHA-256', 'content': i['sha256']}]})
props = s['metadata'].setdefault('properties', [])
for k in ('version', 'sha256', 'source_commit', 'build_run', 'builder', 'built_at'):
    props.append({'name': f'cps5981:release:{k}', 'value': str(i[k])})
json.dump(s, open(out, 'w'), indent=2)
print(f"SBOM bound to sha256:{i['sha256']} ({len(s.get('components', []))} components)")
