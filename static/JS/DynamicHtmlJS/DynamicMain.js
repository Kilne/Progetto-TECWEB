console.log("main start");
console.log("Replication script starting")
const anchoredElem = document.querySelector("#showcase");

for (let i = 0; i < 4; i++) {
    let col = document.createElement("div");
    col.classList.add("col");
    col.id = "scheda: " + i;
    col.append(cardCreator("test title", "text", "/"));
    anchoredElem.appendChild(col);
}

console.log("finished");
console.log("main finished");