export class BudgetBuilder {
    constructor(name, objective,
                objective_target,
                user_saving_value) {
        this.name = name;
        this.objective = objective;
        this.objective_target = objective_target;
        this.user_saving_value = user_saving_value
    }

    define_user_save_frequency(frequency = 1) {
        return this.user_saving_frequency = frequency;
    }

    set_existing_savings(savings) {
        return this.saving_total = savings;
    }

    define_a_date() {
        return new Date(
            (this.objective_target - this.saving_total) / (this.user_saving_frequency * this.user_saving_value)
        ).getTime();
    }

    buildBudget() {
        return new BudgetBasedEntry(this)
    }
}

