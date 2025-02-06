self.addEventListener("install", event => {
    event.waitUntil(
        caches.open("water-tracker-cache").then(cache => {
            return cache.addAll([
                "/",
                "/static/css/style.css",
                "/static/js/main.js",
                "/static/manifest.json",
                "/static/images/icon-192.png",
                "/static/images/icon-512.png",
            ]);
        })
    );
});

self.addEventListener("fetch", event => {
    event.responseWith(
        caches.match(event.request).then(response => {
            return response || fetch(event.request);
        })
    );
});