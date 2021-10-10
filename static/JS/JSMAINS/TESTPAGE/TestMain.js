// The web page main JS
// https://www.w3schools.com/js/js_json_intro.asp
// https://www.sitepoint.com/loop-through-json-response-javascript/
(async () => {

    const resp = await get_data("UserTest");
    resp.forEach((data) => {
        Object.entries(data).forEach(([key, value]) => {
            console.log(`${key}: ${value}`);
        });
    });
})();



