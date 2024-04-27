const { Decimal128, Double } = require("mongodb");
const mongoose = require("mongoose");

 
// Creating Schemas
const LuminanceSchema = new mongoose.Schema({
    day: String,
    luminance: Decimal128,
})

const Luminance = mongoose.model('Luminance', LuminanceSchema);

module.exports = Luminance;
