const { Decimal128 } = require("mongodb");
const mongoose = require("mongoose");

 
// Creating Schemas
const Charge_graphSchema = new mongoose.Schema({
    times: [{type: Date}],
    charge_rate: [{type: Decimal128}],
    day: String,
})

const Charge_graph = mongoose.model('Charge_graph', Charge_graphSchema);

module.exports = Charge_graph;
