const { Decimal128 } = require("mongodb");
const mongoose = require("mongoose");

 
// Creating Schemas
const DaySchema = new mongoose.Schema({
    date: Date,
    times: [{type: Date}],
    power: [{type: Decimal128}],
})

const Day = mongoose.model('Day', DaySchema);

module.exports = Day;

