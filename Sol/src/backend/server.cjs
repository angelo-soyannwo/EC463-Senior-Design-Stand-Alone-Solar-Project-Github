const express = require("express")
const cors = require("cors");
const app = express();
const mongoose = require('mongoose')
const Login = require('./models/Login.cjs');
const Profile = require('./models/userProfile.cjs');
var bodyParser = require('body-parser');

app.use(bodyParser.json()) // for parsing application/json
app.use(bodyParser.urlencoded({ extended: true })) // for parsing application/x-www-form-urlencoded

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

// app.use(express.json())
// app.use(express.urlencoded({extended: true}))

app.use(cors());

app.get('/', cors(), (res,req)=>{

})

app.post('/getUser', async(req, res) => {

        const {email} = req.body
        // console.log(email)

        await Profile.findOne({email: email})
        .then(user => {
            if (!user){
                // console.log(user)
                res.status(400).json({msg: 'There is no user'})
            }
            else{
                // console.log(user)
                res.json(user)
            }
        })
        .catch(e => {
                console.log(e);
                res.json(e);
        })
        
                
        

    })


app.get('/accounts', async(res,req)=>{

    try {
        await Login.findOne({email: true}).then((y)=>{
            if (y){
              console.log(response)
            } 
            else{
                console.log("no entries")
                console.log(y)
            }
          }).catch(e=>{
            console.log(e)
          })
      }
      catch(e){
          console.log(e);
      }

        });


app.post('/sign-up', async(req, res)=>{

    // console.log(req.body)

    const {email,password,userName} = req.body
    const loginData = {
        email:email,
        password:password
    }

    // const profileData = {
    //     email:email,
    //     userName:userName,
    //     user:mongoose.ObjectId(),
    //     solarArrays:[]
    // }

    try {
        const checkEmail = await Login.findOne({email: email});

        if (checkEmail){
            res.json("exists");
        }
        else{
            res.json("notExist")
            const profileData = {
                email:email,
                userName:userName,
                user: new mongoose.Types.ObjectId(),
                solarArrays:[]
            }
            await Profile.insertMany([profileData])
            await Login.insertMany([loginData])
            
        }
            
    }
    catch(e){
        console.log(e);
    }
})

app.post("/login", async(req,res)=>{
    const {email,password} = req.body;
    Login.findOne({email: email}).then(user => {

        if (user){
            if(user.password === password){
                res.json("Success");
            }
            else{
                res.json("incorrectPassword");
            }
        }
        else{
            res.json("notExist");
        }
    }).catch(e => {
            res.json("notExist");
        });
})

app.listen(8000, ()=>{
    console.log("port connected")
})