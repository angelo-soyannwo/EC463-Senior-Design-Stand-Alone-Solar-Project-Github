import * as React from "react";
import {useEffect, useState} from 'react'
import { Link } from "react-router-dom";
// import '../pages/css/home-page.css'
import './css/ControlPanel.css'
import 'bootstrap/dist/css/bootstrap.min.css';
import SolarArrayCard from './SolarArrayCard';
import axios from "axios"
import { Alert } from "bootstrap";
import {Line} from "react-chartjs-2"
import {MDBTable,
        MDBTableHead, 
        MDBTableBody, 
        MDBRow, 
        MDBCol, 
        MDBContainer, 
        MDBBtn,
        MDBBtnGroup,
        MDBPagination,
        MDBPaginationItem,
        MDBPaginationLink,
      } from "mdb-react-ui-kit"

function AnomaliesPanel(props) {

  const [pageName, setPageName] = useState('');
  const [loading, setLoading] = useState(null);
  const [anomalies, setAnomalies] = useState([])
  const [start, setStart] = useState(0);
  const [end, setEnd] = useState(5);
  const [page, setPage] = useState(1);


  useEffect(() => {

    setLoading(true)

    axios.get('http://localhost:8000/getAnomalies').then(result => {
      console.log(result.data)
      try{
        setAnomalies(result.data)
        // console.log(result)
      }
      catch(err){
        console.log(err)
        Alert.alert('sorry an error occcured whilst trying to get the days')
      }
      finally{
        setLoading(false)
      }

    })
  
  }, [])

  function arrayList(array, start){
    if (!array || array === undefined){
      return null
    }

    return (array.map((item, index) => {
      // console.log(solarArray);
      
      return(
        <MDBTableBody key={index}>
          <tr onClick={() => {setDisplayData(item); setSelectedDay(item.date.slice(0, 10)), findDay(days, item.date.slice(0, 10), luminanceList)}}>
            <th scope="row">{start+index+1}</th>
            {/* <td className='tableRow'> */}
            <td className='table_row' style={{marginRight: '5px'}}>
              {/* {item} */}
              {item.date.slice(0, 10)}
            </td>
            <td className='table_row'>
              <div className='text-center'>
                {item.current.$numberDecimal}
              </div>
            </td>
            <td className='table_row'>
              <div className='text-center'>
                {item.voltage.$numberDecimal}
              </div>
            </td>

            <td className='table_row' style={{marginRight: '5px'}}>
              {/* {item} */}
              {item.date.slice(11, 16)}
            </td>

          </tr>
        </MDBTableBody>

      );
    })
    );
  }

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
                      <div className="text-center" style={{marginBottom: '20px'}}>{props.title}</div>
                      </h5>


                    </div>
                  {/* </div> */}

                  {loading ? null : 
                    
                    <MDBContainer>

                      {/* <div style={{marginTop: "100px"}}> */}

                        <MDBRow>
                          <MDBCol size="12">
                          <MDBTableHead >
                            <tr>
                              <th scope="col">No.</th>
                              <th scope="col">Day</th>
                              <th scope="col">Current (mA)</th>
                              <th scope="col">Voltage (V)</th>
                              <th scope="col">Time</th>
                            </tr>
                          </MDBTableHead>

                          {anomalies.length === 0 ? 

                          (<MDBTable className="align-center mb-0">

                            <tr>
                              <td colSpan={2} className='text-center mb-0'>No data found</td>
                            </tr>
                          </MDBTable>)
                          
                          : 


                            arrayList(anomalies.slice(start, end), start)

                          
                          }

                          </MDBCol>
                        </MDBRow>
                      {/* </div> */}

                          <div style={{display: 'flex', justifyContent:'center'}}>
                            {page}
                          </div>
                      

                      <div style={{
                        display: 'flex'
                      }}
                      >

                        {anomalies.length > end ? 
                          <button className="btn" state={{id:props.email}} onClick={() => {setStart(start+5); setEnd(end+5); setPage(page+1)}}>next</button> 
                          
                          : 
                          
                          null
                          
                        }
                        
                        {start > 0 ? 

                          <button className="btn" state={{id:props.email}} onClick={() => {setStart(start-5); setEnd(end-5); setPage(page-1)}}>back</button> 
                          
                          : 

                          null
                        }
                        

                      </div>

                      

                    </MDBContainer>
                    }

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

export default AnomaliesPanel