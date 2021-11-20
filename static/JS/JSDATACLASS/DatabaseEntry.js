export class DatabaseEntry {
    #existing_entry_json = {
        "Project_id": "",
        "Project_name": "",
        "Project_obj": "",
        "Project_time": 0,
        "Project_tmlft": 0,
        "Project_per": 0.0,
        "Project_steps_tot": 0,
        "Project_steps_left": 0,
        "Project_finish": false,
        "Project_concrete": false
    }
    #new_entry_json = {
        "Project_name": "",
        "Project_obj": "",
        "Project_time": 0,
        "Project_concrete": false
    }

    constructor(
        name,
        objective_string,
        is_concrete_bool,
        is_concrete,
    ) {
        //    @TODO:Continuare con i parametri opzionali e la logica di entry nuova o esistente
    }
}