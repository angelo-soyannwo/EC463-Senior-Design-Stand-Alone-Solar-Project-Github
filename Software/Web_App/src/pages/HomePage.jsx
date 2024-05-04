import {useEffect, useState} from 'react'
import  Sol_logo  from '../assets/sol.png'
import './css/home-page.css'
import 'bootstrap/dist/css/bootstrap.min.css';
import { Link, useLocation,} from "react-router-dom";


import HomePanel from '../components/HomePanel';


import axios from 'axios';


export default function HomePage() {
  const location = useLocation()

  const [user, setUser] = useState(null)
  const [email, setEmail] = useState(location.state.id)
  const [solarArrayList, setSolarArrayList] = useState(null)
  const [userSolarArrayObjects, setUserSolarArrayObjects] = useState(null)

  const baseUrl = "https://ec463-senior-design-stand-alone-solar.onrender.com/";
    
  useEffect(() => {
    axios.post(baseUrl.concat('getUser'), {email: email}).then( profile => {
      setUser(profile)
      if (profile) {
        setSolarArrayList(profile.data.solarArrays);
          axios.post(baseUrl.concat('getSolarArrays'), {array: profile.data.solarArrays}).then( response => {
            setUserSolarArrayObjects(response);
            // console.log(response)
          }).catch(err => {
              console.log(err)
            });
        
      }
    }).catch(err => {
      console.log(err)
    });
  }, []);


  // useEffect(() => {
  //   axios.post('http://localhost:8000/getSolarArrays', {array: solarArrayList}).then( response => {
  //     setUserSolarArrayObjects(response)
  //     console.log(response)
  //   }).catch(err => {
  //     console.log(err)
  //   });
  // }, []);

  
  var welcomeMessage =''
  if(!user){
    welcomeMessage = 'Homepage'

  }
  else{
    welcomeMessage = user.data.userName.concat('\'s Homepage')
    // console.log(userSolarArrayObjects)
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
              {/* <li><Link className="nav-link" to="../control-center" state={{id:email}}>Control Center</Link></li> */}
              <li><Link className="nav-link" to="../anomalies" state={{id:email}}>Anomalies</Link></li>
          </ul>
        </nav>
      </header>

            <HomePanel title = {welcomeMessage} email = {email} solarArrayObjects = {userSolarArrayObjects}/> 
            {/* solarArrayObjects = {userSolarArrayObjects} */}


            


      </>
    );
}