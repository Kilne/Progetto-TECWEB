//DEPRECATO NESSUNA SOLUZIONE PER IMPLEMENTARE IL SERVICE WORKER

let cacheName = "TAPP_CACHE"
let filesToCache = [
    "/static/CSS/Style.css",
    "/template/Main.html",
    "/template/Testing.html",
    "templates/UserProject.html",
    "/static/PWA FILES/Manifest Icons/32px-Antu_alarm-clock.svg.png",
    "/static/PWA FILES/Manifest Icons/64px-Antu_alarm-clock.svg.png",
    "/static/PWA FILES/Manifest Icons/128px-Antu_alarm-clock.svg.png",
    "/static/PWA FILES/Manifest Icons/256px-Antu_alarm-clock.svg.png",
    "/static/PWA FILES/Manifest Icons/512px-Antu_alarm-clock.svg.png",
    "/static/PWA FILES/Manifest Icons/Antu_alarm-clock.svg",
];
self.addEventListener('install', function (event) {
    // Perform install steps
    event.waitUntil(
        caches.open(cacheName)
            .then(function (cache) {
                console.log('Opened cache');
                return cache.addAll(filesToCache);
            })
    );
});