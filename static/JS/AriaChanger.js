// Aspetto il documento che sia pronto
$(document).ready(function () {
    // Prendo l'indirizzo dal browser
    let currentAddress = window.location.href;
    // Selezioni tutti gli elementi <a> con class nav-link e ciclo con .each(funzione(indice,elemento))
    $("a.nav-link").each(function (idx, ele) {
        /*Dato che Jinja2/flask con url_for crea il link al momento del caricamento
        lo conforto con l'indirizzo corrente , questo approccio è prono però ad errori se l'indirizzo è più
        profondo di quello standard creato da url for*/
        if (ele.href === currentAddress) {
            // Se i due indirizzi corrispondono gli do la classe active
            ele.classList.add("active");
            // Inoltre gli assegno l'aria current come da linee guida W3C
            $(this).attr("aria-current", "page");
        }
    })
})