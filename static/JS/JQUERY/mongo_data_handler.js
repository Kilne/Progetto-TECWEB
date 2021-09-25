function post_data(username) {
    console.log($.post("/db/" + username))
    // @TODO: pick the right JSON field of the response from th POST data
    return $.post("/db/" + username)
}