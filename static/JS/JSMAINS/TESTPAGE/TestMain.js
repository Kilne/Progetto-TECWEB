//@todo:the response JSON from JQUERY is itself a JSON with many fields must pick the right one and return it
let data = JSON.parse(post_data("UserTest"))
console.log(data)
document.getElementById("JSON").innerText = data