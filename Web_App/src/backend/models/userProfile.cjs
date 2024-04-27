// Import the mongoose module
const mongoose = require("mongoose");

 
// Creating Schemas
const profileSchema = new mongoose.Schema({
    email: String,
    userName: {type: String, required:true},
    user:{
        type: mongoose.Schema.Types.ObjectId,
        required:true,
        ref: 'user'
    },
    solarArrays: [{type: mongoose.Schema.Types.ObjectId, ref:'SolarArray'}],
})

const Profile = mongoose.model('Profile', profileSchema);

module.exports = Profile;