// The web page main JS
// https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON
const main = async () => {
    const resulting = await get_data("UserTest");
    let anchor = document.getElementById("JSON");
    for (const resultingKey in resulting) {
        anchor.innerText += resulting[resultingKey]["owner"];
    }
}

main();

