const { Decimal128 } = require("mongodb");
const mongoose = require("mongoose");

 
// Creating Schemas
const solarArraySchema = new mongoose.Schema({
    id: {type: String},
    location: {type: String},
    Voltage_reading: {type: String},
    Current_reading: {type: String},
    currentPower: {type: String},
    solarPanels: [{type: mongoose.Schema.Types.ObjectId, ref:'SolarPanels'}],
})

const SolarArray = mongoose.model('SolarArray', solarArraySchema);

module.exports = SolarArray;