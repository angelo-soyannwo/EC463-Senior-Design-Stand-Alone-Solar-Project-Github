import * as React from "react";
import { Link } from "react-router-dom";
import './css/SolarArrayCard.css'
import 'bootstrap/dist/css/bootstrap.min.css';
import {useState} from 'react'

function SolarArrayCard2(props) {

  const location = props.location;
  const solarArrayTitle = 'Solar Array: '.concat(location)

  // return (
  //   <>
      
    //             <div className="col-5"> 
    //               <div className="card">
    //                 <div className="card-body">
    //                   <h6 className="solarArray-title">
    //                   <div className="text-left">{solarArrayTitle}</div>
    //                   <br/>
    //                   </h6>
    //                   <div>
    //                   <p>
    //                   id: {solarArray._id} <br/>
    //                   {/* power: {} <br/>
    //                   current: {} <br/>
    //                   voltage: {} <br/> */}
    //                   </p> 
                      
    //                   </div>
                      

    //                 </div>
    //               </div>
    //             </div>
    // </>

  return (
    <>
      
                  <div className="card">
                    <div className="card-body">
                      <h6 className="solarArray-title">
                      <div className="text-left">{solarArrayTitle}</div>
                      <br/>
                      </h6>
                      <div>
                      <p>
                      current: {props.current} mA<br/>
                      voltage: {props.voltage} V<br/>
                      {/* current: <br/>
                      voltage: <br/>  */}
                      {/* power: <br/> */}
                      </p> 
                      
                      </div>
                      

                    </div>
                  </div>
    </>
  );
}

export default SolarArrayCard2