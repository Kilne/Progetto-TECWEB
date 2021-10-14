class MongoClass {

    objective
    owner
    percentage
    proj_name
    project_number
    id

    constructor(user) {
        let data = this.getData(user);
        let data_array = [];
        for (const dataKey in data) {
            for (const element in data[dataKey]) {
                data_array.push(element);
            }
        }
        this.id = data_array[0];
    }

    get objective() {
        return this.objective;
    }

    get owner() {
        return this.owner;
    }

    get percentage() {
        return this.percentage;
    }

    get proj_name() {
        return this.proj_name;
    }

    get project_number() {
        return this.project_number;
    }

    get id() {
        return this.id;
    }

    async getData(link) {
        const response = await fetch(link);
        const data_db = await response.json();
        return data_db;
    }
}
