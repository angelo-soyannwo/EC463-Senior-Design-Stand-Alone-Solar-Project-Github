import * as React from "react";
import { Link } from "react-router-dom";
import './css/SolarArrayCard.css'
import 'bootstrap/dist/css/bootstrap.min.css';
import {useState} from 'react'

function SolarArrayCard(props) {

  const [pageName, setPageName] = useState('');

  return (
    <>
      
                <div className="col-5"> 
                  <div className="card">
                    <div className="card-body">
                      <h6 className="solarArray-title">
                      <div className="text-left">{props.title}</div>
                      <br/>
                      </h6>
                      <div>
                      <p>
                      location: <br/>
                      current: <br/>
                      voltage: <br/>
                      power: <br/>
                      </p> 
                      
                      </div>
                      

                    </div>
                  </div>
                </div>
    </>
  );
}

export default SolarArrayCard