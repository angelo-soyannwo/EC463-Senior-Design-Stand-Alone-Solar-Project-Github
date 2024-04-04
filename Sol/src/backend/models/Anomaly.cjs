const { Decimal128 } = require("mongodb");
const mongoose = require("mongoose");

 
// Creating Schemas
const AnomalieSchema = new mongoose.Schema({
    date: String,
    current: Decimal128,
    voltage: Decimal128,
})

const Anomalie = mongoose.model('Anomalie', AnomalieSchema);

module.exports = Anomalie;