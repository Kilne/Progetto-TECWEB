document.getElementById("Finalize").addEventListener("click", function (ev) {
    ev.preventDefault()
    //@TODO:validare e poi fare subimit all'url non mandare JSON poi ci pensa il backend
    let json_data = {};
    let form_aggreate = document.querySelectorAll(" div > input")

    form_aggreate.forEach(value => {
        if (value["value"] === "") {
            alert("NO INPUT")
        } else {
            console.log("ok")
        }
    })


    // $.ajax({
    //     url: "/finalize/",
    //     method: "POST",
    //     data: JSON.stringify(json_data),
    //     content: "application/json"
    // })
})

