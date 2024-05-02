// Import the mongoose module
const mongoose = require("mongoose");

 
// Creating Schemas
const logInSchema = new mongoose.Schema({
    email: String,
    password: String,
})

const Login = mongoose.model('Login', logInSchema);

module.exports = Login;