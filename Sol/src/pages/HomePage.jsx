import {useEffect, useState} from 'react'
import  Sol_logo  from '../assets/sol.png'
import './css/home-page.css'
import 'bootstrap/dist/css/bootstrap.min.css';
import { Link, useLocation,} from "react-router-dom";

import ControlPanel from '../components/ControlPanel'
import axios from 'axios';


export default function HomePage() {
  const location = useLocation()

  const [user, setUser] = useState(null)
  const [email, setEmail] = useState(location.state.id)
    
  useEffect(() => {
    axios.post('http://localhost:8000/getUser', {email: email}).then( profile => {
      setUser(profile)
    }).catch(err => {
      console.log(err)
    });
  }, []);


  var welcomeMessage =''
  if(!user){
    welcomeMessage = 'Homepage'
  }
  else{
    welcomeMessage = user.data.userName.concat('\'s Homepage')
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
              <li><Link className="nav-link" to='../analytics' state={{id:email}}>Analytics</Link></li>
              <li><Link className="nav-link" to="../control-center" state={{id:email}}>Control Center</Link></li>
              <li><Link className="nav-link" to="../anomalies" state={{id:email}}>Anomalies</Link></li>
          </ul>
        </nav>
      </header>

            <ControlPanel title = {welcomeMessage}/>


      </>
    );
}