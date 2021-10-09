// https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise?retiredLocale=it
// https://it.javascript.info/fetch
function get_data(username) {

    return fetch("/db/" + username)
        .then(value => value.json())
        .then(value => {
            return value;
        });
}
