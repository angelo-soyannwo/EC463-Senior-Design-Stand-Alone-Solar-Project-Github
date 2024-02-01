import * as React from "react";
import ChartsEmbedSDK from '@mongodb-js/charts-embed-dom';
import { Link } from "react-router-dom";
// import '../pages/css/home-page.css'
import './css/ControlPanel.css'
import 'bootstrap/dist/css/bootstrap.min.css';
import {useState, useEffect} from 'react'
import SolarArrayCard from './SolarArrayCard'
import axios from "axios"
import { Alert } from "bootstrap";
import {Chart as ChartJS } from "chart.js/auto"
import {Line} from "react-chartjs-2"
import {MDBTable, MDBTableHead, MDBTableBody, MDBRow, MDBCol, MDBContainer} from "mdb-react-ui-kit"




function AnalyticsPanel(props) {

  const [pageName, setPageName] = useState('');
  const [times, setTimes] = useState(null);
  const [power, setPower] = useState(null);
  const [loading, setLoading] = useState(null)
  const [loading2, setLoading2] = useState(null)
  const [days, setDays] = useState([])

  const sdk = new ChartsEmbedSDK({
    baseUrl: "https://charts.mongodb.com/charts-embedding-examples-wgffp", // ~REPLACE~ with the Base URL from your Embed Chart dialog.
  });
  const chart = sdk.createChart({
    chartId: "735cfa75-15b8-483a-bc2e-7c6659511c7c", // ~REPLACE~ with the Chart ID from your Embed Chart dialog.
    height: "300px",
    // Additional options go here
  });

  useEffect(() => {

    setLoading(true)
    setLoading2(true)
    

    axios.post('http://localhost:8000/getDay',).then((result) => {
      try{
        if(result){
          setPower(result.data.power.map(item => item.$numberDecimal))
          setTimes(result.data.times)
          // console.log(result.data.power.map(item => item.$numberDecimal))
          // console.log(result.data.times)
        }
      }
      catch(err){
        console.log(err)
      }
      finally{
        setLoading(false);
      }
      
    })

    axios.get('http://localhost:8000/getDays').then(result => {
      try{
        setDays(result.data)
        // console.log(result.data)
      }
      catch(err){
        console.log(err)
        Alert.alert('sorry an error occcured whilst trying to get the days')
      }
      finally{
        setLoading2(false)
      }
    })
    
  }, [])

  function arrayList(array){
    if (!array || array === undefined){
      return null
    }

    return (array.map((item, index) => {
      // console.log(solarArray);
      
      return(
        <MDBTableBody key={index}>
          <tr>
            <th scope="row">{index+1}</th>
            <td>
              {/* {item} */}
              {item.date.slice(0, 10)}
            </td>
          </tr>
        </MDBTableBody>

      );
    })
    );
  }

  

  return (
    <>
      {/*!-- library  --*/}


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
                  { loading ? null : 

                  <div style={{marginTop: "20px"}}>
                  
                  <Line
                                  data={{
                                    labels: times,
                                    datasets: [
                                      {
                                        label: 'power',
                                        data: power,
                                        backgroundColor: "#064FF0",
                                        borderColor: "#064FF0",
                                      },
                                    ]
                                  }}
                                  options={{
                                    elements: {
                                      line: {
                                        tension: 0.5,
                                      },
                                    },
                                    plugins: {
                                      title: {
                                        text: "Power against time",
                                      },
                                    },
                                  }}
                    />

                    </div>
                    
                    }


                    {loading2 ? null : 
                    
                    <MDBContainer>
                      <div style={{marginTop: "100px"}}>

                        <MDBRow>
                          <MDBCol size="12">
                          <MDBTableHead>
                            <tr>
                              <th scope="col">No.</th>
                              <th scope="col">Day</th>
                            </tr>
                          </MDBTableHead>

                          {days.length === 0 ? 

                          (<MDBTable className="align-center mb-0">

                            <tr>
                              <td colSpan={2} className='text-center mb-0'>No data found</td>
                            </tr>
                          </MDBTable>)
                          
                          : 
                          
                          arrayList(days)



                          }

                          </MDBCol>
                        </MDBRow>
                      </div>
                    </MDBContainer>
                    }

                    
                </div>

                <div className="col"></div>
          </div>

          <div className="row">
            <div className="col"></div>

            {/* <SolarArrayCard title = {'Solar Array '}/> */}
            {/* <ChartComponent/> */}

           



            <div className="col"></div>

          </div>

        </div>

      </div>

      
    </>
  );
}

export default AnalyticsPanel