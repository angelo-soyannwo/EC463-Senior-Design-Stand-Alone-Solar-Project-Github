import * as React from "react";
import { Link } from "react-router-dom";
// import '../pages/css/home-page.css'
import './css/HomePanel.css'
import 'bootstrap/dist/css/bootstrap.min.css';
import {useState} from 'react'
import SolarArrayCard from './SolarArrayCard'
import mongoose from "mongoose";
import axios from "axios"


// const mongoose = require('mongoose')

function HomePanel(props) {

  const Data = {
    id: new mongoose.Types.ObjectId(),
    location:"Fenway",
    currentVoltage:1.2,
    currentCurrent:1.3,
    currentPower:1.56,
    solarPanels:[]
}
  async function submit(e) {
    e.preventDefault();

    try{
        await axios.post("http://localhost:8000/createSolarArrayInstance", Data).then(res=>{
          if(res.data === "notExist") {
            alert("created")
          }
          else if(res.data==="exists"){
            alert('This solar array instance already exists')
          }
        }).catch(e=>{
          alert(e)
          console.log(e)
        })
    }
    catch(e){
        console.log(e)
    }
}

  const [pageName, setPageName] = useState('');

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

            <SolarArrayCard title = {'Solar Array '}/>

            <div className="col">
              <div className="text-center">

                <button >Add Solar Array</button>

                <button onClick={submit}>Create Solar Array Instance</button>

                
              </div>
              
            </div>

          </div>

        </div>

      </div>
    </>
  );
}

export default HomePanel