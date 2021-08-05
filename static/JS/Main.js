// @TODO : SERVICE WORKER NON FUNZIONA NENACHE COSI URGE UNA GUIDA FATTA BENE
window.onload = () => {
    "use strict";

    if ('service worker ' in navigator) {
        navigator.serviceWorker
            .register("../static/PWA%20FILES/sw.js").then(function (registration) {
                console.log("Service Worker successfully registered with scope: ", registration.scope);
            },
            function (error) {
                console.log("Service Worker failed to registry ", error);
            });
    }

}
