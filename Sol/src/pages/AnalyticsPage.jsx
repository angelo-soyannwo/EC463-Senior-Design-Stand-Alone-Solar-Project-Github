import React from 'react';
import {useEffect, useState} from 'react'
import axios from 'axios'
import  Sol_logo  from '../assets/sol.png'
import './css/landing-page.css';
import 'bootstrap/dist/css/bootstrap.min.css';
// import navbarLink from '../components/navbarLink';
import { Link, useLocation } from "react-router-dom";
import AnalyticsPanel from '../components/AnalyticsPanel'



export default function AnalyticsPage() {

  const { state } = useLocation()
  const [user, setUser] = useState(null)
  const [email, setEmail] = useState("")
    
  useEffect(() => {

    const getUser = async() => {
      var userJsonString = localStorage.getItem("currentUser")
      var user = JSON.parse(userJsonString)
      setEmail(user.email)
      setUser(user)
  
    }

    getUser();
    // axios.post('http://localhost:8000/getUser', {email: email}).then( profile => {
    //   setUser(profile)
    // }).catch(err => {
    //   console.log(err)
    // });
  }, []);


  var welcomeMessage =''
  if(!user){
    welcomeMessage = 'Analytics'
  }
  else{
    // welcomeMessage = user.data.userName.concat('\'s Analytics Page')
    welcomeMessage = user.userName.concat('\'s Analytics Page')
  }

    return (
        <>
        <header>
          <nav class="navbar">
              <div>
              <Link className="logo" to="../home" state={{id:email}}>
                Sol <span><img src={Sol_logo} className="sol_logo" alt="Sol logo" /></span>
              </Link>
              </div>
  
            <ul class="topnav">
              {/* <li><a className="nav-link" href="#">Analytics</a></li> */}
              <li><Link className="nav-link" to="../analytics" state={{id:email}}>Analytics</Link></li>
              {/* <li><Link className="nav-link" to="../control-center" state={{id:email}}>Control Center</Link></li> */}
              <li><Link className="nav-link" to="../anomalies" state={{id:email}}>Anomalies</Link></li>
            </ul>
          </nav>
        </header>

        {/* <div className='pagebody'>
        <div className="page_content">
          
          <div className="row">
            <div className="col"></div>

                <div className="col-8"> 
                  <div className="card">
                    <div className="card-body">
                      <h5 className="card-title">
                      <div className="text-center">Analytics</div>
                      </h5>

                    </div>
                  </div>
                </div>

                <div className="col"></div>
          </div>
        </div>

        </div> */}
        { user !== null && user.solarArrays.length > 0 ?
         <AnalyticsPanel title={welcomeMessage} setEmailAddress={setEmail} email={email}/>
          :
          <div className='pagebody'>
          <div className="page_content">
            
            <div className="row">
              <div className="col"></div>

                  <div className="col-5"> 
                    {/* <div className="card"> */}
                      <div className="card-body">
                        <h5 className="card-title">
                        <div className="text-center">{welcomeMessage}</div>
                        </h5>

                      </div>
                    {/* </div> */}
                  </div>

                  <div className="col"></div>
            </div>

            <div className="row">
              <div className="col"></div>


              <div className="col">

                </div>

              {/* <SolarArrayCard title = {'Solar Array '}/> */}

              <div className="col">
                <div className="text-center">
              
                </div>
              </div>

            </div>

          </div>

        </div>
        }
      </>
    );
}