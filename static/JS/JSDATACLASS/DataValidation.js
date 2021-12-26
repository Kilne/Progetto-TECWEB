document.getElementById("Finalize").addEventListener("click", function (ev) {
    ev.preventDefault()
    //@TODO:validare e poi fare subimit all'url non mandare JSON poi ci pensa il backend
    let json_data = {};
    json_data["project_name"] = document.getElementById("text-form").value
    console.log("event fired")
    console.log(json_data)


    $.ajax({
        url: "/finalize/",
        method: "POST",
        data: JSON.stringify(json_data),
        content: "application/json"
    })
})

