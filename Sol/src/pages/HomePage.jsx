
// import './css/home-page.css'
// import 'bootstrap/dist/css/bootstrap.min.css';

export const HomePage = () => {
    return (
        <>
        <header>
        <nav class="navbar">
              <div className="logo">
                Sol <span><img src={Sol_logo} className="sol_logo" alt="Sol logo" /></span>
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

                <div className="col-5"> 
                  <div className="card">
                    <div className="card-body">
                      <h5 className="card-title">Homepage</h5>

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