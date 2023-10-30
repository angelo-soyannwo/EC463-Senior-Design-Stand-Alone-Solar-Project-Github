import React from 'react';
import  Sol_logo  from '../assets/sol.png'
import './css/landing-page.css';
import 'bootstrap/dist/css/bootstrap.min.css';

export default function AnalyticsPage() {
    return (
        <>
        <header>
          <nav class="navbar">
                <div className="logo">
                  Sol <span><img src={Sol_logo} className="sol_logo" alt="Sol logo" /></span>
                </div>
  
            <ul class="topnav">
              <li><a className="nav-link" href="#">Analytics</a></li>
              <li><a className="nav-link" href="#">Control Center</a></li>
              <li><a className="nav-link" href="#">Anomalies</a></li>
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
                      <div className="text-center">Analytics</div>
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