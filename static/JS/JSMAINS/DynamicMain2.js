console.log("main start");

for (let i = 0; i < 12; i++) {
    document.querySelector(".list-group").appendChild(
        list_group_creator("Prova", "prova", Math.floor((Math.random() * 100) + 1), "/"));
}
console.log("main finished");