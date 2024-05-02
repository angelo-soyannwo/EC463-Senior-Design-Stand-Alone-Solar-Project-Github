const { Decimal128 } = require("mongodb");
const mongoose = require("mongoose");

 
// Creating Schemas
const GraphSchema = new mongoose.Schema({
    times: [{type: Date}],
    power: [{type: Decimal128}],
    day: String,
    luminances: [{type: Decimal128}],
    temperature_celcius: [{type: Decimal128}],
    temperature_farenheit: [{type: Decimal128}],
    times: [{type: Date}],
})

const Graph = mongoose.model('Graph', GraphSchema);

module.exports = Graph;
