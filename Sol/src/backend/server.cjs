const express = require("express")
const cors = require("cors");
const app = express();
const mongoose = require('mongoose')
const Login = require('./mongo.cjs');

app.use(express.json())
app.use(express.urlencoded({extended: true}))

app.use(cors());

app.get('/', cors(), (res,req)=>{

})

// app.post("/login",async(req,res)=>{
//     const{email,password}=req.body

//     try{
//         const check=await collection.findOne({email:email})

//         if(check){
//             res.json("exist")
//         }
//         else{
//             res.json("notexist")
//         }

//     }
//     catch(e){
//         res.json("fail")
//     }

// })



// app.post("/signup",async(req,res)=>{
//     const{email,password}=req.body

//     const data={
//         email:email,
//         password:password
//     }

//     try{
//         const check=await collection.findOne({email:email})

//         if(check){
//             res.json("exist")
//         }
//         else{
//             res.json("notexist")
//             await collection.insertMany([data])
//         }

//     }
//     catch(e){
//         res.json("fail")
//     }

// })

// app.listen(8000,()=>{
//     console.log("port connected");
// })


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


app.post("/", async (req, res)=>{
    const[email,password] = req.body

    try {
        const checkEmail = await Login.findOne({email: email});

        if (checkEmail){
            res.json("exists");
        }
        else{
            res.json("notExist");
        }
    }
    catch(e){
        res.json("notExist");
    }
})

app.post('/sign-up', async(req, res)=>{

    const {email,password} = req.body
    const data = {
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
            await Login.insertMany([data])
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
        }
        else{
            res.json("Incorrect password");
        }
    }).catch(e => {
            res.json("notExist");
        });

    // try {
    //     // const checkEmail = await Login.findOne({email: email})
    //     Login.findOne({email: email}).then(user => {

    //         if (user){
    //             if(user.password === password)
    //         }
    //         else{
    //             res.json("notExist");
    //         }
    //     })
            
    // }
    // catch(e){
    //     res.json("notExist");
    // }
})

app.listen(8000, ()=>{
    console.log("port connected")
})