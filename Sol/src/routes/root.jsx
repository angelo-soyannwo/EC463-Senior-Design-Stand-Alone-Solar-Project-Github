import  Sol_logo  from '../assets/sol.png'
import  viteLogo  from '/vite.svg'
// import './App.css';
import '../pages/css/home-page.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import { Link } from "react-router-dom";

export default function Root() {

    return (
      <>
        <header>
          <nav class="navbar">
                <div>
                  <Link className="logo" to="/">
                  Sol <span><img src={Sol_logo} className="sol_logo" alt="Sol logo" /></span>
                  </Link>
                </div>
  
            <ul class="topnav">
                <li><a className="nav-link" href="#">Login</a></li>
                <li><a className="nav-link" href="#">Sign Up</a></li>
            </ul>
          </nav>
        </header>
  
        <body>
          <div className="page_content">
            
            <div className="row">
              <div className="col"></div>
  
                  <div class="col-4">
                      <div class="row">
                      <p className="maxim">Harness The Power of The Sun.<br></br>
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