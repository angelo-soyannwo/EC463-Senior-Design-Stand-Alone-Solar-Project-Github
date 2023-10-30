import React from 'react';
import './css/landing-page.css';
import 'bootstrap/dist/css/bootstrap.min.css';

function LandingPage() {
    return (
        <>
        

      <body>
        <div className="page_content">
          
          <div className="row">
            <div className="col"></div>

                <div class="col-4">
                    <div class="row">
                    <p><br></br><br></br><br></br><br></br>Harness The Power of The Sun.<br></br>
                    </p>
                    </div>
                </div>

                <div className="col-5"> 
                  <div className="card">
                    <div className="card-body">
                      <h5 className="card-title">Login</h5>

                      <div className="mb-3">
                        <label for="exampleFormControlInput1" class="form-label">Email Address</label>
                        <input type="email" class="form-control" id="email-address" name="From" placeholder="email@example.com"></input>
                      </div>
                
                      <div className="mb-3">
                        <label for="inputPassword" class="visually-hidden">Password</label>
                        <input type="password" class="form-control" id="inputPassword" placeholder="Password"></input>
                      </div>

                      <form action="control_center.html">
                        <button type="submit" className="btn signin-btn btn-lg" >Login</button>
                      </form>
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

export default LandingPage;