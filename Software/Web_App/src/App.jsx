
import React, { useState, useContext} from 'react';
import  Sol_logo  from './assets/sol.png'
import  viteLogo  from '/vite.svg'
// import './App.css';
import './pages/css/landing-page.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import axios from "axios"
import { Link, useNavigate} from "react-router-dom";
import {LoginContext} from './helper/Context.cjs'


function App() {

  // const [loggedIn, setLoggedIn] = useContext(LoginContext)

    const history=useNavigate();

    const [email, setEmail] = useState('')
    const [password, setPassword] = useState('')

    const baseUrl = "http://localhost:8000/";

    async function submit(e) {
        e.preventDefault();

        try{
            await axios.post(baseUrl.concat("login"), {email, password}).then(res=>{
              if (res.data==="Success"){
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
              <li><Link className="nav-link" to="login">Login</Link></li>
              <li><Link className="nav-link" to="sign-up">Sign Up</Link></li>
            </ul>
          </nav>
        </header>
  
        <body>
          <div className="page_content">
            
            <div className="row">
              <div className="col"></div>
  
                  <div className="col-4">
                      <div className="row">
                      <p className="maxim">Harness The Power of The Sun.<br></br>
                      </p>
                      </div>
                  </div>
  
                  <div className="col-5"> 
                    <div className="card">
                      <div className="card-body">
                        <form acction="Post">
                            <h5 className="card-title">Login</h5>
    
                            <div className="mb-3">
                            <label className="form-label">Email Address</label>
                            <input type="email" onChange={(e)=>{setEmail(e.target.value)}} class="form-control" id="email-address" name="userEmail" placeholder="email@example.com"></input>
                            </div>
                    
                            <div className="mb-3">
                            <label className="visually-hidden">Password</label>
                            <input type="password" onChange={(e)=>{setPassword(e.target.value)}} class="form-control" id="userPassword" placeholder="Password"></input>
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
  
        </body>
      </>
    )
}
export default App