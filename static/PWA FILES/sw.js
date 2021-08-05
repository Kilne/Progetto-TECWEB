let cacheName = "TAPP_CACHE"
let filesToCache = [
    "static/JS/Main.js",
    "static/CSS/Style.css",
    "templates/Main.html",
    "templates/Testing.html"
];

self.addEventListener('install', function (e) {
    e.waitUntil(
        caches.open(cacheName).then(function (cache) {
            return cache.addAll(filesToCache);
        })
    );
});

self.addEventListener('fetch', function (e) {
    e.respondWith(
        caches.match(e.request).then(function (response) {
            return response || fetch(e.request)
        })
    );
});