// DEPRECATO NESSUNA SOLUZIONE PER L'IMPLEMENTAZIONE DEL SERVICE WORKER
if ('serviceWorker' in navigator) {
    navigator.serviceWorker
        .register("../static/PWA%20FILES/sw.js", {scope: '/'})
        .then(registration => {
            console.log("ServiceWorker running");
        })
        .catch(err => {
            console.log(err);
        })
}