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
import {MDBTable,
        MDBTableHead, 
        MDBTableBody, 
        MDBRow, 
        MDBCol, 
        MDBContainer, 
        MDBBtn,
        MDBBtnGroup,
      } from "mdb-react-ui-kit"




function AnalyticsPanel(props) {

  const [pageName, setPageName] = useState('');
  const [times, setTimes] = useState(null);
  const [power, setPower] = useState(null);
  const [luminances, setLuminances] = useState(null);
  const [luminaceTimes, setLuminanceTimes] = useState(null);
  const [loading, setLoading] = useState(null)
  const [loading2, setLoading2] = useState(null)
  const [loading3, setLoading3] = useState(null)
  const [days, setDays] = useState([])
  const [daysList, setDaysList] = useState([])
  const [lux, setLux] = useState("");
  const [tempC, setTempC] = useState("");
  const [tempF, setTempF] = useState("");
  const [selectedDay, setSelectedDay] = useState(null)
  const [searchQuery, setSearchQuery] = useState('');

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
    setLoading3(true)
    // console.log(props.email)

    // axios.post('http://localhost:8000/getDay',).then((result) => {
    //   try{
    //     if(result){
    //       setPower(result.data.power.map(item => item.$numberDecimal))
    //       setTimes(result.data.times.map(item => item.slice(11, 22)))
    //       // console.log(result.data.power.map(item => item.$numberDecimal))
    //       // console.log(result.data.times)
    //     }
    //   }
    //   catch(err){
    //     console.log(err)
    //   }
    //   finally{
    //     setLoading(false);
    //   }
      
    // })
    axios.get('http://localhost:8000/luminanceTempGraphData').then(result => {
      console.log(result.data[0])
      try{
        setLuminanceTimes(result.data[0].times.map(item => item.slice(11, 22)))
        setLuminances(result.data[0].luminances.map(item => item.$numberDecimal))
      }
      catch(err){
        console.log(err)
        Alert.alert('sorry an error occcured whilst trying to get the days')
      }
      finally{
        setLoading3(false)
      }

    })

    axios.get('http://localhost:8000/getDays').then(result => {
      try{

        var x = result.data.reverse()
        setPower(result.data[0].power.map(item => item.$numberDecimal))
        setTimes(result.data[0].times.map(item => item.slice(11, 22)))
        setSelectedDay(result.data[0].date.slice(0, 10))
        setDays(result.data)
        setDaysList(result.data)
        // console.log(result.data)
      }
      catch(err){
        console.log(err)
        Alert.alert('sorry an error occcured whilst trying to get the days')
      }
      finally{
        setLoading(false)
      }
    })

    axios.get('http://localhost:8000/get_luminance_and_temp').then(result => {
      try{

        setLux(result.data.luminance.luminance.$numberDecimal)
        setTempC(result.data.temp.temperature_celsius.$numberDecimal)
        setTempF(result.data.temp.temperature_farenheit.$numberDecimal)
        console.log(result.data.temp.temperature_celsius.$numberDecimal)
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

  function setDisplayData(x){
    setPower(x.power.map(item => item.$numberDecimal)); 
    setTimes(x.times.map(item => item.slice(11, 22)));
  }

  function findDay(array, date){

    // var formattedDate = date.slice(7,10) + '-' + date.slice(4,5) + '-' + date.slice(0,1)
    console.log(date)
    for(var i=0; i<array.length; i++){
      if (array[i].date.slice(0, 10) === date){
        setSelectedDay(array[i].date.slice(0, 10))
        setPower(array[i].power.map(item => item.$numberDecimal)); 
        setTimes(array[i].times.map(item => item.slice(11, 22)));
      }
    }
  }

  function arrayList(array){
    if (!array || array === undefined){
      return null
    }

    return (array.map((item, index) => {
      // console.log(solarArray);
      
      return(
        <MDBTableBody key={index}>
          <tr onClick={() => {setDisplayData(item); setSelectedDay(item.date.slice(0, 10))}}>
            <th scope="row">{index+1}</th>
            <td className='tableRow'>
              {/* {item} */}
              {item.date.slice(0, 10)}
            </td>
          </tr>
        </MDBTableBody>

      );
    })
    );
  }

  function handleSearch(){
    console.log(searchQuery)
    findDay(days, searchQuery)
    // props.setEmailAddress(props.email)
  }

  function handleReset() {
    console.log('reset')
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

                  {selectedDay ? <h5>{selectedDay}</h5> : null}
                  

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

                                      {
                                        label: 'luminance',
                                        data: luminances,
                                        backgroundColor: "yellow",
                                        borderColor: "yellow",
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


                    {loading ? null : 
                    
                    <MDBContainer>

                      <div style={{
                        margin: 'auto',
                        padding: '15px',
                        maxWidth: '400px',
                        alignContent: 'center'
                      }}
                      className="d-flex input-group w-auto"
                      onSubmit={handleSearch}
                      >

                      <input
                        type='date'
                        className='form-control'
                        placeholder='Search'
                        value={searchQuery}
                        onChange={(e) => setSearchQuery(e.target.value)}
                        
                      />

                      <MDBBtnGroup>
                        {/* <MDBBtn type='submit'>Search</MDBBtn> */}
                        {/* <MDBBtn onClick={() => handleSearch()}>Search</MDBBtn>
                        <MDBBtn className='mx-2' color='info' onClick={() => handleReset()}>Reset</MDBBtn> */}
                        <button className="btn" state={{id:props.email}} onClick={() => {handleSearch()}}>Search</button>
                      </MDBBtnGroup>

                      </div>

                      {/* <div style={{marginTop: "100px"}}> */}

                        <MDBRow>
                          <MDBCol size="12">
                          <MDBTableHead >
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
                      {/* </div> */}
                    </MDBContainer>
                    }

                    
                </div>

                <div className="col">

                <div className="card-body">
                      <h6 className="">
                      <div className="text-center">Data</div>
                      <br/>
                      </h6>
                      <div>
                      <p>
                      Luminance: {lux} Lux<br/>
                      Temperature:  <br/> {tempC} °C | {tempF} °F
                      </p> 
                      
                      </div>
                      

                  </div>

                </div>
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