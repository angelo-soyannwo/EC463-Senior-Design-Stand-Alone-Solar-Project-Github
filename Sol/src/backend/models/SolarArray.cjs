const { Decimal128 } = require("mongodb");
const mongoose = require("mongoose");

 
// Creating Schemas
const solarArraySchema = new mongoose.Schema({
    // id: {type: mongoose.Schema.Types.ObjectId, required:true},
    location: {type: String},
    currentVoltage: {type: Decimal128},
    currentCurrent: {type: Decimal128},
    currentPower: {type: Decimal128},
    solarPanels: [{type: mongoose.Schema.Types.ObjectId, ref:'SolarPanels'}],
})

const SolarArray = mongoose.model('SolarArray', solarArraySchema);

module.exports = SolarArray;