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
  

  useEffect(() => {
    axios.post('http://localhost:8000/getUser', {email: email}).then( profile => {
      setUser(profile)
      if (profile) {
        // setSolarArrayList(profile.data.solarArrays);
          axios.post('http://localhost:8000/getSolarArrays', {array: profile.data.solarArrays}).then( response => {
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
      console.log(solarArray.currentCurrent)
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
                <ModalForm email = {email}/>

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


              <div className="col">
                {arrayList(solarArrays.data)}
                </div>

              {/* <SolarArrayCard title = {'Solar Array '}/> */}

              <div className="col">
                <div className="text-center">
                  <ModalForm email = {email}/>

                  <ModalFormCSAI />
                </div>
              </div>

            </div>

          </div>

        </div>
      </>
    );
  }
}

export default HomePanel