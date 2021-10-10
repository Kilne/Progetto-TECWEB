// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise?retiredLocale=it
// https://it.javascript.info/fetch
async function get_data(username) {

    const url = `/db/${username}`;

    const response = await fetch(url);
    const json = await response.json();
    console.log(json);
    return json;
}
