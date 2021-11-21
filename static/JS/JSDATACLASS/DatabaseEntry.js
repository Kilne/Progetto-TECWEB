export class DatabaseEntry {

    //existing database entry object notation
    #json_object_existing = {
        "id": "",
        "name": "",
        "obj": "",
        "date": Object,
        "time_left": 0,
        "percentage_done": 0.0,
        "step_total": 0,
        "steps_left": 0,
        "is_finished": false,
        "is_concrete": false
    };
    //new dabase entry to be sent
    #json_object_new = {
        "name": "",
        "obj": "",
        "date": Object,
        "is_concrete": false,
    }

    constructor(
        name,
        objective_string,
        time_int_64,
        is_concrete_bool,
        project_id_UUID = "",
        time_left = 0,
        percentage_done = 0.0,
        steps_total = 0,
        steps_left = 0,
        is_finished_bool = false
    ) {
        this.#_p_name = name;
        this.#_p_obj = objective_string;
        this.#_p_date.setTime(time_int_64);
        this.#_p_is_concrete = is_concrete_bool;
        this.#_p_id = project_id_UUID;
        this.#_p_time_left = time_left;
        this.#_p_per_done = percentage_done;
        this.#_p_step_tot = steps_total;
        this.#_p_step_left = steps_left;
        this.#_p_is_finished = is_finished_bool;
    }

    //required
    #_p_name;

    get p_name() {
        return this.#_p_name;
    }

    #_p_obj;

    get p_obj() {
        return this.#_p_obj;
    }

    #_p_date = new Date();

    get p_date() {
        return this.#_p_date.getTime();
    }

    #_p_is_concrete;

    get p_is_concrete() {
        return this.#_p_is_concrete;
    }

    // not required it will be assigned/sent by DB
    #_p_id;

    get p_id() {
        return this.#_p_id;
    }

    // not required deducted by logic or assigned by DB
    #_p_time_left;

    get p_time_left() {
        return this.#_p_time_left;
    }

    #_p_per_done;

    get p_per_done() {
        return this.#_p_per_done;
    }

    #_p_step_tot;

    get p_step_tot() {
        return this.#_p_step_tot;
    }

    #_p_step_left;

    get p_step_left() {
        return this.#_p_step_left;
    }

    #_p_is_finished;

    get p_is_finished() {
        return this.#_p_is_finished;
    }


}

// @TODO: forse forse è il caso di fare due classi una per un entry esistente una per nuova da mandare