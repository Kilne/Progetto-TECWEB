function get_all_data() {
    return $.ajax({
        url: '/db/getALL/',
        method: "GET",
    })
}

function add_project(project_data) {
    return $.ajax({
        url: '/db/addONE/',
        method: "POST",
        data: JSON.stringify(project_data),
        contentType: "application/json"
    })
}

function update_proj(project_data) {
    return $.ajax({
        url: '/db/updateONE/',
        method: "PUT",
        data: JSON.stringify(project_data),
        contentType: "application/json"
    })
}

function delete_a_project(id) {
    return $.ajax({
        url: "/db/deleteONE/",
        method: "DELETE",
        data: JSON.stringify(id),
        contentType: "application/json"
    })
}