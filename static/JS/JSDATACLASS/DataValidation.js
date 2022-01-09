document.getElementById("Finalize").addEventListener("click", function (ev) {
    ev.preventDefault()
    let json_data = {};
    let input_forms = document.getElementsByClassName("form-control");
    let radio_checked = document.getElementsByClassName("form-check-input");

    for (const input_ele of input_forms) {
        // @TODO: ci siamo quasi da affinare la reg exp e poi la data
        if (input_ele.getAttribute("type") === "text") {
            if (/([^a-z]|[^0-9])/.test(input_ele.value)) {
                console.log("FARTS at" + input_ele.id);
            } else {
                json_data[input_ele.id] = input_ele.value;
            }
        }
    }

    for (const radioCheckedElement of radio_checked) {
        if (radioCheckedElement.hasAttribute("checked")) {
            json_data ["Prate"] = radioCheckedElement.value;
        }
    }


    $.ajax({
        url: "/finalize/",
        method: "POST",
        data: JSON.stringify(json_data),
        content: "application/json"
    })

})

