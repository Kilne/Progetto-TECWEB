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
// @TODO: finire la schema per il database tenere conto della data in mongoDB-JS-Python
class DatabaseEntry{
    #internal_json= {
        "Project_id"    :   "",
        "Project_name"  :   "",
        "Project_obj"   :   "",
        "Project_own"   :   "",
        "Project_time"  :   0,
        "Project_tmlft" :   0,
        "Project_per"   :   0.0,
        "Project_steps_tot"     :   0,
        "Project_steps_left"    :   0,
        "Project_num"   :   0,
        "Project_finish"    :   false,
        "Project_concrete"  :   false
    }
    constructor(id,name,own,obj) {

    }
}