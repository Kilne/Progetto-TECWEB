document.getElementById("Finalize").addEventListener("click", function (ev) {
    ev.preventDefault()
    let json_data = {};
    let input_forms = document.getElementsByClassName("form-control");
    let radio_checked = $(".form-check-input")

    for (const inputFormsKey in input_forms) {
        console.log("input:" + inputFormsKey.id)
    }

    for (const radioCheckedKey in radio_checked) {
        console.log("radio:" + radio_checked.id)
    }
    //@TODO uuuuuuuuuuuggggggggggggggggggggghhhhhhhhhhhhhhhhhhhhhhhhhhh
    $.ajax({
        url: "/finalize/",
        method: "POST",
        data: JSON.stringify(json_data),
        content: "application/json"
    })

})

