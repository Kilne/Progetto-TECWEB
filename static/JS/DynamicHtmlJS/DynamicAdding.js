function Creator(Number) {
    console.log("Replication script starting")
    const anchoredElem = document.querySelector("#showcase");

    for (let i = 0; i < Number; i++) {
        let col = document.createElement("div");
        col.classList.add("col");
        col.id = "scheda: " + i;
        col.append(cardCreator("test title", "text", "home"));
        anchoredElem.appendChild(col);
    }

    console.log("finished");
}