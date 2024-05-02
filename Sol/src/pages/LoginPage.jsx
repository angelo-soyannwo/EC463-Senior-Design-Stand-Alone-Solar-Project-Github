import React, { useState, useContext } from 'react';
import  Sol_logo  from '../assets/sol.png'
import './css/landing-page.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Link, useNavigate } from "react-router-dom";
import { useEffect } from 'react';
import axios from "axios"
import {LoginContext} from '../helper/Context.cjs'


export default function LoginPage() {
  // const [loggedIn, setLoggedIn] = useContext(LoginContext)


    const history=useNavigate();

    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')

    async function submit(e) {
        e.preventDefault();

        try{
            await axios.post("http://localhost:8000/login", {email, password}).then(async(res)=>{
              if (res.data==="Success"){
                await axios.post("http://localhost:8000/getUser", {email}).then(async(user)=>{
                  window.localStorage.setItem("currentUser", JSON.stringify(user));
                }
                );
                history("/home", {state:{id:email}})
              } 
              else if (res.data=="notExist"){
                  alert("You have not signed up")
              }
              else if (res.data=="incorrectPassword"){
                alert("incorrect login details")
              }
            }).catch(e=>{
              alert("Wrong details")
              console.log(e)
            })
        }
        catch(e){
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
  
        <div className="page_content">
            
            <div className="row">
              <div className="col"></div>

                    <div className="col-5"> 
                    <div className="card">
                      <div className="card-body">
                        <form acction="Post">
                            <h5 className="card-title">Login</h5>
    
                            <div className="mb-3">
                            <label className="form-label">Email Address</label>
                            <input type="email" onChange={(e)=>{setEmail(e.target.value)}} className="form-control" id="email-address" name="userEmail" placeholder="email@example.com"></input>
                            </div>
                    
                            <div className="mb-3">
                            <label className="form-label">Password</label>
                            <input type="password" onChange={(e)=>{setPassword(e.target.value)}} className="form-control" id="userPassword" placeholder="Password"></input>
                            </div>

                            <span className="text-center">
                                <p>Don't have an account? <Link to="../sign-up">Sign Up</Link> </p>
                            </span>
    
                            <button type="submit" className="btn signin-btn btn-lg" onClick={submit}>Login</button>
                        </form>
                      </div>
                    </div>

                  </div>
                  
  
                  <div className="col"></div>
            </div>
          </div>

      </>
    )
}