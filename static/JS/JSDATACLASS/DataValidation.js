let json_data = {};

let form_handler = document.getElementById("Finalize").onclick(function () {
    json_data.value = document.getElementById("text-form").innerText
    console.log(json_data)
})

