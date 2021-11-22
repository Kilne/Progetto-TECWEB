export class DatabaseEntry {
    #json_object = {
        "name": "",
        "obj": "",
        "quantified_objective": 0,
        "date": Object,
        "time_left": 0,
        "percentage_done": 0.0,
        "step_total": 0,
        "steps_left": 0,
        "single_step_value": 0,
        "is_finished": false,
        "is_concrete": false
    };

    constructor(name_string, objective_string, objective_value_int, date_big_int, is_concrete_bool) {
        this.#json_object.name = name_string;
        this.#json_object.obj = objective_string;
        this.#json_object.quantified_objective = objective_value_int;
        this.#json_object.date = new Date(date_big_int);
        this.#json_object.is_concrete = is_concrete_bool;
    }


}

