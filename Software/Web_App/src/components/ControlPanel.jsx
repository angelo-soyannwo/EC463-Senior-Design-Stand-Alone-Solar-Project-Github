import * as React from "react";
import { Link } from "react-router-dom";
// import '../pages/css/home-page.css'
import './css/ControlPanel.css'
import 'bootstrap/dist/css/bootstrap.min.css';
import {useState} from 'react'
import SolarArrayCard from './SolarArrayCard'

function ControlPanel(props) {

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

            {/* <SolarArrayCard title = {'Solar Array '}/> */}

            <div className="col"></div>

          </div>

        </div>

      </div>
    </>
  );
}

export default ControlPanel