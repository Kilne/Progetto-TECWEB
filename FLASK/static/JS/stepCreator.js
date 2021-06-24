export function stepCreator(singleStepValue, valueToPartition) {
    //Checking value to partition
    try {
        if (typeof (valueToPartition) != "number") {
            throw "Inconsistent value to partition";
        }
    } catch (err) {
        return "An error has occurred: " + err;
    }

    //supporting variables
    let arraySteps = [];
    let breakPoint = 0;

    switch (typeof (singleStepValue)) {
        case "number":
            while (breakPoint !== valueToPartition) {
                arraySteps.push(singleStepValue);
                breakPoint += singleStepValue;
            }
            return arraySteps;
        case "object":
            for (const key in singleStepValue) {
                if (Object.hasOwnProperty.call(singleStepValue, key)) {
                    arraySteps.push(singleStepValue[key]);

                }
            }
            //Extra array for returning the result
            let extraArray = [];
            if (arraySteps.length === 3) {
                for (let index = 0; index < arraySteps[2]; index++) {
                    extraArray.push(arraySteps[0]);
                }
                for (let index = 0; index < arraySteps[1]; index++) {
                    extraArray[index] += 1;
                }
                return extraArray;
            } else {
                for (let index = 0; index < arraySteps[1]; index++) {
                    extraArray.push(1);
                }

                return extraArray;
            }
            throw "An unexpected value was found";
    }

}