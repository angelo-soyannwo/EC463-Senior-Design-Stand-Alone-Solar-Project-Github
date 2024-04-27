const { Decimal128 } = require("mongodb");
const { Double } = require("mongodb");
const mongoose = require("mongoose");

 
// Creating Schemas
const TemperatureSchema = new mongoose.Schema({
    day: String,
    temperature_celsius: Decimal128,
    temperature_farenheit: Decimal128
})

const Temperature = mongoose.model('Temperature', TemperatureSchema);

module.exports = Temperature;
