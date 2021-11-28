export class BasicData {
    constructor(name_p_string, objective_p_string) {
        this._name = name_p_string;
        this._object = objective_p_string;
    }

    get p_name() {
        return this._name;
    }

    get p_obj_name() {
        return this._object;
    }
}