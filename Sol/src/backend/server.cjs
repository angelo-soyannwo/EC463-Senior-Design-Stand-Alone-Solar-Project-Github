const express = require("express")
const cors = require("cors");
const app = express();
const mongoose = require('mongoose')
const Login = require('./models/Login.cjs');
const Profile = require('./models/userProfile.cjs');
const SolarArray = require('./models/SolarArray.cjs');
var bodyParser = require('body-parser');
require('dotenv').config({path:'./.env'})

const databaseEntryPoint = 'mongodb+srv://seun:JGOf3ykPlQ3ilDac@sol-cluster.mretkif.mongodb.net/Sol?retryWrites=true&w=majority'

app.use(bodyParser.json()) // for parsing application/json
app.use(bodyParser.urlencoded({ extended: true })) // for parsing application/x-www-form-urlencoded



app.use(cors());

app.get('/', cors(), (res,req)=>{

})


app.post('/sign-up', async(req, res)=>{

    const {email,password,userName} = req.body
    const loginData = {
        email:email,
        password:password
    }

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

app.post('/getSolarArrays', async(req, res) => {

    const {array} = req.body
    // console.log(array)

    // console.log(myJsonString)



    const records = await SolarArray.find().where('_id').in(array).exec();
    // console.log(records)

    await SolarArray.find({_id: {$in: array}})
    .then(solarArrays => {
        if (!solarArrays){
            // console.log(user)
            res.status(400).json({msg: 'No solar arrays'})
        }
        else{
            // console.log(1)
            res.json(solarArrays)
        }
    })
    .catch(e => {
            console.log(e);
            res.json(e);
    })

})

app.post('/createSolarArrayInstance', async(req, res) => {

    const {location,solarPanels} = req.body

    const Data = {
        location:location,
        currentCurrent:0,
        currentVoltage:0,
        currentPower:0,
        solarPanels:solarPanels
    }

    try {
        // const checkArray = await SolarArray.findOne({id:id});

        // const checkArray = await SolarArray.findById({id});

        // if (checkArray){
        //     res.json("exists");
        // }
        // else{
            res.json("notExist")
            await SolarArray.insertMany([Data])
            
        // }
            
    }
    catch(e){
        console.log(e);
    }

})

app.post('/addSolarArray', async(req, res) => {

    const {email,arrayId} = req.body
    // const mongoArrayId = mongoose.Types.ObjectId(arrayId);

    try {
        // const checkArray = await SolarArray.findOne({id:arrayId});
        const checkArray = await SolarArray.findOne({_id:arrayId});
        console.log(arrayId)


        if (checkArray){
            var val = false


            await Profile.findOne({email: email}).then(
                user => {
                    // console.log(user)
                    const ID = new mongoose.Types.ObjectId(arrayId); //may not need anymore
                    val = user.solarArrays.includes(arrayId, 0);
                    console.log(user.solarArrays)
                }
            );

            if (val){
                res.json("solarArrayAlreadySelected");
                return
            }

            await Profile.updateOne(
                { email: email},
                { $push: { solarArrays: arrayId } }
             )
            res.json("exists");
        }
        else{
             
            res.json("notExist")
            
        }
            
    }
    catch(e){
        console.log(e);
        res.json("notExist")
    }

})

// app.listen(8000, ()=>{
//     console.log("port connected")
// })

mongoose.connect(databaseEntryPoint).then(()=>{
    app.listen(8000, ()=>{
        console.log("port connected")
        // console.log(process.env.MONGO_URI)
    })
    console.log('mongo database connected');
}).catch(
    (e)=>{
        console.log(e);
        console.log('database failed');
    }
);