function Creator(Number) {
    console.log("Replication script starting")
    const anchoredElem = document.querySelector("#test");
    const array = [Number];
    for (let i = 0; i < Number; i++) {
        array[i] = document.createElement("div");
        array[i].id = "h" + i;
        array[i].innerText = "I'm level " + i;
    }

    for (let i = 0; i < array.length; i++) {
        console.log(array[i]);
    }
    let i = array.length - 1;
    while (i > 0) {
        array[i - 1].append(array[i]);
        i--;
    }
    anchoredElem.appendChild(array[0]);


    console.log("finished");
}