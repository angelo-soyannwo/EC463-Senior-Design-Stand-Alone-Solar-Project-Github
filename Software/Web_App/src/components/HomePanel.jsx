import * as React from "react";
import { Link, } from "react-router-dom";
// import '../pages/css/home-page.css'
import './css/HomePanel.css'
import 'bootstrap/dist/css/bootstrap.min.css';
import {useState, useEffect} from 'react'
import SolarArrayCard from './SolarArrayCard'
import SolarArrayCard2 from './SolarArrayCard2'
import axios from "axios"
import ModalForm from "./modalForm";
import ModalFormCSAI from "./modalFormCreateSolarArrayInstance";


// const mongoose = require('mongoose')

function HomePanel(props) {

  const email = props.email;
  const [user, setUser] = useState(null)
  const [solarArrays, setSolarArrayObjects] = useState({})
  // const [refresh, setRefresh] = useState(false)
  const baseUrl = "https://ec463-senior-design-stand-alone-solar.onrender.com/";
  const [refresh, setRefresh] = useState(null)

  useEffect(() => {
    axios.post(baseUrl.concat('getUser'), {email: email}).then( profile => {
      setUser(profile)
      if (profile) {
        localStorage.setItem("currentUser", JSON.stringify(profile.data));
        console.log(profile.data)
        // setSolarArrayList(profile.data.solarArrays);
          axios.post(baseUrl.concat('getSolarArrays'), {array: profile.data.solarArrays}).then( response => {
            setSolarArrayObjects(response);
            // console.log(response)
          }).catch(err => {
              console.log(err)
            });
      }
    }).catch(err => {
      console.log(err)
    });
  }, []);

  console.log(solarArrays.data)

  

  function arrayList(array){
    if (!array || array === undefined){
      return null
    }

    return (array.map((solarArray) => {
      // console.log(solarArray);
      return(
        <SolarArrayCard2 
        location={solarArray.location}  
        current={solarArray.Current_reading} 
        voltage={solarArray.Voltage_reading}/>

        // current={solarArray.currentCurrent.$numberDecimal} 
        // voltage={solarArray.currentVoltage.$numberDecimal}/>
      );
    })
    );
  }

if (!solarArrays){
    return (
    <> 
      <div className='pagebody'>
        <div className="page_content">
          
          <div className="row">
            <div className="col"></div>

                <div className="col-5"> 
                  {/* <div className="card"> */}
                    <div className="card-body">
                      <h5 className="card-title">
                      <div className="text-center">{props.title}</div>
                      </h5>

                    </div>
                  {/* </div> */}
                </div>

                <div className="col"></div>
          </div>

          <div className="row">
            <div className="col"></div>

              {/* { 
                solarArrays.data.map((solarArray) => {
                  console.log(solarArray);
                  return(<SolarArrayCard2 location={solarArray.location}  current={solarArray.currentCurrent} voltage={solarArray.currentVoltage}/>);
                })
              } */}
            {/* <SolarArrayCard title = {'Solar Array '}/> */}

            <div className="col">
              <div className="text-center">
                <ModalForm email = {email} />

                <ModalFormCSAI />
              </div>
            </div>

          </div>

        </div>

      </div>
    </>
  );
}

else{
    return (
      <>

          <div className="page_content">
            
            

            <div className="row">
              <div className="col"></div>


              <div className="col">
              <h5 className="card-title">
                  <div className="text-center" style={{marginBottom: '20px'}}>{props.title}</div>
              </h5>
                {arrayList(solarArrays.data)}
                </div>

              {/* <SolarArrayCard title = {'Solar Array '}/> */}

              <div className="col" style={{display: 'flex', justifyContent: 'center'}}>
                <div className="text-center">
                {/* the line below has a button which allows for the creation of a solar array in our database*/}
                  <ModalForm email = {email} refresh = {refresh} setRefresh = {setRefresh}/>


                  {/* the line below has a button which allows for the creation of a solar array in our database*/}
                  {/* <ModalFormCSAI /> */}
                </div>
              </div>

            </div>

          </div>


      </>
    );
  }
}

export default HomePanel