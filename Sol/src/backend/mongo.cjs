// Import the mongoose module
const mongoose = require("mongoose");

// Connecting to database
mongoose.connect('mongodb://127.0.0.1:27017/sol').then(
    ()=>{
        console.log('mongo database connected');
    }).catch(
        (e)=>{
            console.log(e);
            console.log('database failed');
        }
    );
 
// Creating Schemas
const logInSchema = new mongoose.Schema({
    email: String,
    password: String,
})

const Login = mongoose.model('Login', logInSchema);

module.exports = Login;