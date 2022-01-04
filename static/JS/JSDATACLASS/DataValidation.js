document.getElementById("Finalize").addEventListener("click", function (ev) {
    ev.preventDefault()
    let json_data = {};
    let form_aggreate = document.querySelectorAll(" div > input").values()

    for (const element of form_aggreate) {
        if (element.hasAttribute("type").toString() === "radio") {
            if (element.checked) {
                // @TODO a quanto pare i radio devono scassare le palle
                json_data["Prate"] = element.value;
            } else {
                continue;
            }
        }
        json_data[element.id] = element.value
    }

    $.ajax({
        url: "/finalize/",
        method: "POST",
        data: JSON.stringify(json_data),
        content: "application/json"
    })

})

