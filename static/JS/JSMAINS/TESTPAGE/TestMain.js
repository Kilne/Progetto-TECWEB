//@todo:continua a darmi promesse.....
async function myDisplay() {
    return await post_data("UserTest")
}

let dbs_data = await myDisplay()

console.log(dbs_data)