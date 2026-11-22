// كشتة: works without the internet after the first open. The page itself is fetched fresh when there is a connection (so updates arrive).
const C = 'kashta-8.6.2-1795354323';
self.addEventListener('install', e => { self.skipWaiting(); e.waitUntil(caches.open(C).then(c => c.addAll(['./', './index.html', './manifest.webmanifest', './icon-192.png']).catch(() => {}))); });
self.addEventListener('activate', e => e.waitUntil(caches.keys().then(ks => Promise.all(ks.filter(k => k !== C).map(k => caches.delete(k)))).then(() => self.clients.claim())));
self.addEventListener('fetch', e => {
  const u = new URL(e.request.url); if (e.request.method !== 'GET' || u.origin !== location.origin) return;
  const page = e.request.mode === 'navigate' || /\/(index\.html)?$/.test(u.pathname);
  if (page) e.respondWith(fetch(e.request).then(r => { const k = r.clone(); caches.open(C).then(c => c.put('./index.html', k)); return r; }).catch(() => caches.match('./index.html')));
  else e.respondWith(caches.match(e.request).then(m => m || fetch(e.request).then(r => { if (r.ok) { const k = r.clone(); caches.open(C).then(c => c.put(e.request, k)); } return r; })));
});
