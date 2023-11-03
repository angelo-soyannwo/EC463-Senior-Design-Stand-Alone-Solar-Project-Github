import React, { useState } from 'react';
import  Sol_logo  from '../assets/sol.png'
import './css/home-page.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Link, useNavigate} from "react-router-dom";
import axios from 'axios';


export default function SignUpPage() {

  // const history=useNavigate();

  //   const [email,setEmail]=useState('')
  //   const [password,setPassword]=useState('')

  //   async function submit(e){
  //       e.preventDefault();

  //       try{

  //           await axios.post("http://localhost:8000/signup",{
  //               email,password
  //           })
  //           .then(res=>{
  //               if(res.data=="exist"){
  //                   alert("User already exists")
  //               }
  //               else if(res.data=="notexist"){
  //                   history("/home",{state:{id:email}})
  //               }
  //           })
  //           .catch(e=>{
  //               alert("wrong details")
  //               console.log(e);
  //           })

  //       }
  //       catch(e){
  //           console.log(e);

  //       }

  //   }

    //ADD back
        const history=useNavigate();
        const [email, setEmail] = useState('')
        const [password, setPassword] = useState('')

    async function submit(e) {
        e.preventDefault();
        // const history=useNavigate();
        // const [email, setEmail] = useState('')
        // const [password, setPassword] = useState('')

        try{
            await axios.post("http://127.0.0.1:8000/sign-up", {email, password}).then(res=>{
              if (res.data=="exist"){
                alert("You already have an account with us")
                history("/home",{state:{id:email}})
              }
              else if (res.data=="notExist"){
                history("/home",{state:{id:email}})
              }
            }).catch(e=>{
              alert(e)
              console.log(e)
            })
        }
        catch{
            console.log(e)
        }
    }

  
    return (
      <>
      <header>
          <nav className="navbar">
                <div>
                  <Link className="logo" to="/">
                  Sol <span><img src={Sol_logo} className="sol_logo" alt="Sol logo" /></span>
                  </Link>
                </div>
  
            <ul className="topnav">
                <li><Link className="nav-link" to="../login">Login</Link></li>
                <li><Link className="nav-link" to="../sign-up">Sign Up</Link></li>
            </ul>
          </nav>
        </header>
  
        <div className='pagebody'>
        <div className="page_content">
            
            <div className="row">
              <div className="col"></div>

                    <div className="col-5"> 
                    <div className="card">
                      <div className="card-body">
                        <h5 className="card-title">Sign Up</h5>
  
                        <div className="mb-3">
                          <label className="form-label">Email Address</label>
                          <input type="email" onChange={(e)=>{setEmail(e.target.value)}} className="form-control" id="email-address" name="userEmail" placeholder="email@example.com"></input>
                        </div>
                  
                        <div className="mb-3">
                          <label className="form-label">Password</label>
                          <input type="password" onChange={(e)=>{setPassword(e.target.value)}} className="form-control" id="userPassword" placeholder="Password"></input>
                        </div>

                        <span className="text-center">
                            <p>Already have an account? <Link to="../login">Login</Link> </p>
                        </span>

                        <button type="submit" className="btn signin-btn btn-lg" onClick={submit}>Login</button>
                        
                      </div>
                    </div>

                  </div>
                  
  
                  <div className="col"></div>
            </div>
          </div>
  
        </div>
      </>
    )
}