import {BasicData} from "./BasicData";

export class BudgetBasedEntry extends BasicData {

    constructor(name_p_string, objective_p_string,
                objective_value, user_saving_value,
                user_savings_frequency = 1, user_saving_total = 0,
                date_of_completion = new Date()) {
        super(name_p_string, objective_p_string);
        this._objective_p_string = objective_p_string;
        this._objective_value = objective_value;
        this._user_saving_value = user_saving_value;
        this._user_saving_total = user_saving_total;
        this._date_of_completion = date_of_completion;
    }


    get objective_p_string() {
        return this._objective_p_string;
    }

    get objective_value() {
        return this._objective_value;
    }

    get user_saving_value() {
        return this._user_saving_value;
    }

    get user_saving_total() {
        return this._user_saving_total;
    }

    get date_of_completion() {
        return this._date_of_completion;
    }
}