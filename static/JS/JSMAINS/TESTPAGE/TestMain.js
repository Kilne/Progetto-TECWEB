// The web page main JS
// https://www.w3schools.com/js/js_json_intro.asp
// https://www.sitepoint.com/loop-through-json-response-javascript/

let anchor = document.getElementById("JSON")
let data_to_send = {
    "proj_name": "kek",
    "objective": "big keks",
    "percentage": 99.99,
    "owner": "pepe",
    "project_number": 99
}
let a_value_to_update = {
    "proj_name": "extremely big keks",
    "_id": "617d86b2d10d9bed568c700c"
}
let a_project_to_delete = {
    "_id": "617eced2c7fc8b3da50557c0"
}


// let result = get_all_data()
// let post_result = add_project(data_to_send)
// let update_result = update_proj(a_value_to_update)
let delete_result = delete_a_project(a_project_to_delete)

// result.then(value => {
//     for (const valueKey in value) {
//         anchor.appendChild(
//             list_group_creator(
//                 value[valueKey]["proj_name"],
//                 value[valueKey]["objective"],
//                 value[valueKey]["percentage"],
//                 "/"
//             )
//         )
//     }
// })

// post_result.then(
//     value => {
//         console.log(value)
//     }
// )
//
// update_result.then(value => {
//     console.log(value)
// })

delete_result.then(value => {
        console.log(value)
    }
)



