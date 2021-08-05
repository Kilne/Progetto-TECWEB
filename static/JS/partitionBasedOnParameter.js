export function partitionBasedOnParameter(partitionValue, valueToPartition) {


    // Checking numbers
    try {
        if (typeof (partitionValue) != "number" || typeof (valueToPartition) != "number") {
            throw "Wrong data input type";
        } else if (partitionValue < 0 || valueToPartition < 0) {
            throw "Negative values of data inputs";
        }
    } catch (err) {
        return "An error has occurred: " + err;
    }
    // mod of the value to partition
    let mod = valueToPartition % partitionValue;
    if (mod === 0) {
        // returns the single value to obtain the partition
        return valueToPartition / partitionValue;
    } else if (valueToPartition > partitionValue) {
        /*
        returns an array containing:
        1)The values of the partition subtracted of the mod value to even it
        2)The mod excess to be added from the first element to obtain original partition
        value
        3) the desired partition number
        */
        return [(valueToPartition - mod) / partitionValue, mod, partitionValue];
    } else {
        /* 
        if the partition desired is greater than the value to be partitioned will be returned:
        1)A single unit 1
        2)The desired number of partitions
        */
        return [1,partitionValue];
    }


}