// @TODO: finire la schema per il database tenere conto della data in mongoDB-JS-Python
export class DatabaseEntry{
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
    constructor(id,name,obj,own,time,tmlft,perc,steps_t,steps_l,num,finish,concrete) {
        this.#internal_json.Project_id = id
        this.#internal_json.Project_name = name
        this.#internal_json.Project_obj = obj
        this.#internal_json.Project_own = own
        this.#internal_json.Project_time = time
        this.#internal_json.Project_tmlft = tmlft
        this.#internal_json.Project_per = perc
        this.#internal_json.Project_steps_tot = steps_t
        this.#internal_json.Project_steps_left = steps_l
        this.#internal_json.Project_num = num
        this.#internal_json.Project_finish = finish
        this.#internal_json.Project_concrete = concrete
    }
}