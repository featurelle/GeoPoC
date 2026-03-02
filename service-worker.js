self.addEventListener('install', event => {
    self.skipWaiting();
    console.log('Service Worker installed');
});

self.addEventListener('activate', event => {
    event.waitUntil(self.clients.claim());
    console.log('Service Worker activated');
});

self.addEventListener('fetch', event => {
    // For navigation requests, always go to network
    if (event.request.mode === 'navigate') {
        event.respondWith(fetch(event.request));
        return;
    }
    // Pass-through for everything else
    event.respondWith(fetch(event.request));
});
