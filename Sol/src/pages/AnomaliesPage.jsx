import React from 'react';
import  Sol_logo  from '../assets/sol.png'
import './css/landing-page.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Link,} from "react-router-dom";

export default function AnomaliesPage() {
    return (
        <>
        <header>
          <nav class="navbar">
              <div>
                <Link className="logo" to="../home">
                Sol <span><img src={Sol_logo} className="sol_logo" alt="Sol logo" /></span>
                </Link>
              </div>
  
            <ul class="topnav">
              <li><Link className="nav-link" to="../analytics">Analytics</Link></li>
              <li><Link className="nav-link" to="../control-center">Control Center</Link></li>
              <li><Link className="nav-link" to="../anomalies">Anomalies</Link></li>
            </ul>
          </nav>
        </header>

        <body>
        <div className="page_content">
          
          <div className="row">
            <div className="col"></div>

                <div className="col-8"> 
                  <div className="card">
                    <div className="card-body">
                      <h5 className="card-title">
                      <div className="text-center">Anomalies</div>
                      </h5>

                    </div>
                  </div>
                </div>

                <div className="col"></div>
          </div>
        </div>

        </body>

      </>
    );
}