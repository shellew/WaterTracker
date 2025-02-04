self.addEventListener("install", event => {
    event.waitUntil(
        caches.open("water-tracker-cache").then(cache => {
            return cache.addAll([
                "/",
                "/static/css/style.css",
                "/static/js/main.js",
                "/static/manifest.json"
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