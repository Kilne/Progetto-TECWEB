// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise?retiredLocale=it
// https://it.javascript.info/fetch


async function get_data(username) {
    const url = `/db/${username}`;
    const response = await fetch(url);
    const json = await response.json();
    console.log(json);
    let array = [];
    for (const jsonKey in json) {
        console.log(json[jsonKey]);
        for (const jsonElementKey in json[jsonKey]) {
            array.push(json[jsonKey][jsonElementKey]);
        }
    }
    console.log(array[0]);
    return new MongoClass(array[0], array[1], array[2], array[3], array[4], array[5]);
}
