// The web page main JS
// https://www.w3schools.com/js/js_json_intro.asp
// https://www.sitepoint.com/loop-through-json-response-javascript/
// https://newbedev.com/how-to-extract-data-out-of-a-promise
// While you can get a value from an awaited Promise inside an async function (simply because it pauses the function to
// await a result), you can't ever get a value directly out of a Promise
// and back into the same scope as the Promise itself.

(async () => {
    const data_array = await get_data("UserTest");
    console.log(data_array);
    const anchor = document.getElementById("JSON");

    for (const dataArrayKey in data_array) {
        const list = list_group_creator(
            data_array[dataArrayKey]["proj_name"],
            data_array[dataArrayKey]["objective"],
            data_array[dataArrayKey]["percentage"],
            "/");
        anchor.appendChild(list);
    }

    let data_to_send = {
        "owner": "Luca",
        "project_number": 55,
        "objective": "Pepo",
        "percentage": 99.0,
        "proj_name": "Meme"
    };


    const injection_response = await post_data("UserTest", data_to_send);

    console.log(injection_response);

    const update_array = await get_data("UserTest");

    console.log(update_array)

    let entry_to_update = {};

    for (const updateArrayKey in update_array[2]) {
        entry_to_update[updateArrayKey] = update_array[2][updateArrayKey];
    }
    entry_to_update["owner"] = "Yoda";
    console.log(entry_to_update);
    const update_response = await put_data("UserTest", entry_to_update);
    console.log(update_response);
})();








