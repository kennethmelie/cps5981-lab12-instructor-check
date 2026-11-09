"""Post-deploy verification: is production serving exactly the approved bytes?
Compares the live tarball and every live file against the approved SHA-256 and the verified artifact."""
import sys, json, hashlib, tarfile, time, urllib.request, os
base, version, approved, verified = sys.argv[1].rstrip('/') + '/', sys.argv[2], sys.argv[3], sys.argv[4]
get = lambda p: urllib.request.urlopen(urllib.request.Request(base + p + f'?nocache={time.time()}', headers={'Cache-Control': 'no-cache'}), timeout=30).read()
for attempt in range(24):  # Pages can take a few minutes to serve a new deployment
    try:
        rel = json.loads(get('release.json'))
        if rel.get('version') == version: break
    except Exception as e:
        rel = {'error': str(e)}
    time.sleep(10)
rows, ok = [], True
def row(check, expected, actual):
    global ok
    good = expected == actual; ok &= good
    rows.append((check, expected, actual, 'PASS' if good else 'FAIL'))
row('release.json version', version, rel.get('version'))
row('release.json sha256', approved, rel.get('sha256'))
live = get('release/cougar-advising.tar.gz'); open('live.tar.gz', 'wb').write(live)
row('live tarball sha256', approved, hashlib.sha256(live).hexdigest())
with tarfile.open(verified) as t:
    for m in t.getmembers():
        if not m.isfile(): continue
        name = m.name.split('/', 1)[1]
        want = hashlib.sha256(t.extractfile(m).read()).hexdigest()
        try: have = hashlib.sha256(get(name)).hexdigest()
        except Exception as e: have = f'not served ({e.__class__.__name__})'
        row(f'live file {name}', want[:16], have[:16])
md = [f"# Post-deploy verification", '', f"- Production URL: {base}", f"- Approved release: {version}", f"- Approved SHA-256: `{approved}`",
      f"- Checked at: {time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime())}", f"- Run: {os.environ.get('GITHUB_SERVER_URL','')}/{os.environ.get('GITHUB_REPOSITORY','')}/actions/runs/{os.environ.get('GITHUB_RUN_ID','')}", '',
      '| Check | Expected | Actual | Result |', '|---|---|---|---|'] + [f'| {a} | `{b}` | `{c}` | {d} |' for a, b, c, d in rows] + ['', f"**Result: {'production is serving the approved bytes' if ok else 'MISMATCH - production is not serving the approved bytes'}**"]
open('post-deploy.md', 'w').write('\n'.join(md) + '\n'); print('\n'.join(md))
sys.exit(0 if ok else 1)
