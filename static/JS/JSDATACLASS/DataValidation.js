document.getElementById("Finalize").addEventListener("click", function (ev) {
    ev.preventDefault()
    let json_data = {};
    let input_forms = document.getElementsByClassName("form-control");
    let radio_checked = $(".form-check-input")

    // @TODO ok CheckMover.js muove l'attrivuto checked per i radio , basta prender quello e dargli il value

    $.ajax({
        url: "/finalize/",
        method: "POST",
        data: JSON.stringify(json_data),
        content: "application/json"
    })

})

