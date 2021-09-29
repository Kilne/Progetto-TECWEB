async function post_data(username) {
    //@todo:devi usare la fetch lascia perdere jquery
    const db_data = await fetch("/db/" + username);

    return db_data.json()
}