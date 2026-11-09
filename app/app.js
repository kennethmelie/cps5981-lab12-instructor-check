// Cougar Advising - demo front end for CPS 5981 Lab 12. Never connect it to real student data.
document.getElementById('book').addEventListener('submit', (e) => {
  e.preventDefault();
  const sid = e.target.sid.value, day = e.target.day.value;
  document.getElementById('msg').textContent = `Request received for ${day}. Your advisor will confirm by email.`;
});
fetch('release.json').then(r => r.ok ? r.json() : null).then(j => {
  if (j) document.getElementById('rel').textContent = `${j.version || j.tag} · sha256:${(j.sha256 || '').slice(0, 12)}`;
}).catch(() => {});
