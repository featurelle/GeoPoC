self.addEventListener('install', event => {
    self.skipWaiting();
    console.log('Service Worker installed');
});

self.addEventListener('activate', event => {
    event.waitUntil(self.clients.claim());
    console.log('Service Worker activated');
});

self.addEventListener('fetch', event => {
    // Pass-through - no caching for this PoC
    event.respondWith(fetch(event.request));
});
