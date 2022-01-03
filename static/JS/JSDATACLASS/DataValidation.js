document.getElementById("Finalize").addEventListener("click", function (ev) {
    ev.preventDefault()
    let json_data = {};
    let form_aggreate = document.querySelectorAll(" div > input").values()

    for (const element of form_aggreate) {
        json_data[element.id] = element.value
        //    @TODO finito il form prepare i data validation
    }

    $.ajax({
        url: "/finalize/",
        method: "POST",
        data: JSON.stringify(json_data),
        content: "application/json"
    })

})

