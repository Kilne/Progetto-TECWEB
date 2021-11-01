window.onload = () => {

    let anchor = document.getElementById("projects")
    let data = get_all_data()
    data.then(value => {
        for (const valueKey in value) {
            anchor.appendChild(
                list_group_creator(
                    value[valueKey]["proj_name"],
                    value[valueKey]["objective"],
                    value[valueKey]["percentage"],
                    "/"
                )
            )
        }
    })
}