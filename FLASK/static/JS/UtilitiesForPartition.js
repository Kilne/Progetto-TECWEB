class ProjectStub {
    constructor(name, numberTotalToDivide, numberDivideValues) {
        this.totalToDive = numberTotalToDivide;
        this.divideValue = numberDivideValues;
        this._projectArraySteps = [];
        this.modRemanider = 0;
        this.singleStepValue = 0;
        this._name = name;
    }


    get name() {
        return this._name;
    }

    get projectArraySteps() {
        this.#popTheArray();
        return this._projectArraySteps;
    }

    #popTheArray() {
        if (this.totalToDive > this.divideValue) {
            this.modRemanider = this.totalToDive % this.divideValue;
        } else {
            for (let i = 0; i < this.totalToDive; i++) {
                this._projectArraySteps[i] = 1;
            }
        }

        if (this.modRemanider === 0) {
            this.singleStepValue = this.totalToDive / this.divideValue;
            for (let i = 0; i < this.divideValue; i++) {
                this._projectArraySteps[i] = this.singleStepValue;
            }
        } else {
            this.singleStepValue = this.totalToDive / this.divideValue - this.modRemanider;
            for (let i = 0; i < this.divideValue; i++) {
                this._projectArraySteps[i] = this.singleStepValue;
            }
            for (let i = 0; i < this.modRemanider; i++) {
                this._projectArraySteps[i] += 1;
            }
        }
    }
}



