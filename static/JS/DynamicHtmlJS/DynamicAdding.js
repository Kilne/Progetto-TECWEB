function Creator(Number) {
    console.log("Replication script starting")
    const anchoredElem = document.querySelector("#showcase");

    const card = cardCreator("test title", "text", "/");

    anchoredElem.appendChild(card);
    //@TODO: creare un certo numero di schede per test

    console.log("finished");
}