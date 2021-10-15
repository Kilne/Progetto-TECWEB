// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise?retiredLocale=it
// https://it.javascript.info/fetch
// https://newbedev.com/how-to-extract-data-out-of-a-promise
// While you can get a value from an awaited Promise inside an async function
// (simply because it pauses the function to await a result),
// you can't ever get a value directly out of a Promise and back into the same scope as the Promise itself.


async function get_data(username) {
    //Url della route di flask, ritorna una PROMISE
    const url = `/db/${username}`;
    //Dalla risposta tiro fuori i dati che interessano con la fetch
    const response = await fetch(url);
    // Ritorno SOLO il JSON contenente i dati del DB user se lo trova, attenzione i dati sono in un array di array
    // JSON_DATI[ARRAY_DI_JSON] l'accesso dopo quindi dovrà essere :
    // JSON_DATI[i]->accedo al primo membro del json di dati->JSON_DATI[i][nome_proprietà]-> effettivo accesso
    // all'iesimo JSON e al valore della sua proprietà chiamata.
    return await response.json();
}

async function post_data(username, data) {
    // Url della route di flask, ritorna una PROMISE
    const url = `/db/${username}/post`
    // Mando i dati insieme alla fetch specifico il modo in cui le mando e che tipologia di dato sta arrivando con
    // il campo @headers i dati sono nel campo @body che sfrutta la funzione @JSON.stringify per renderlo leggibile a
    // flask altrimenti ho molti problemi lato backend
    const response = await fetch(url, {
        method: "POST",
        mode: "cors",
        headers: {
            "content_type": "application/json"
        },
        body: JSON.stringify(data)
    });
    // Ottengo la risposta il JSON (sempre un JSON di array) conterrà solo la risposta del DB altrimenti avrò un bel
    // server internal error 500
    return await response.json();


}
