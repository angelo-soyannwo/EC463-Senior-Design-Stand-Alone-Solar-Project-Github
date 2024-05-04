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
        MDBPagination,
        MDBPaginationItem,
        MDBPaginationLink,
      } from "mdb-react-ui-kit"




function AnalyticsPanel(props) {

  const [pageName, setPageName] = useState('');
  const [times, setTimes] = useState(null);
  const [power, setPower] = useState(null);
  const [luminances, setLuminances] = useState(null);
  const [luminanceList, setLuminanceList] = useState(null);
  const [temperatures, setTemperatures] = useState(null)
  const [luminaceTimes, setLuminanceTimes] = useState(null);
  const [chargeRate, setChargeRate] = useState(null)
  const [charge_graphs, setCharge_graphs] = useState(null)
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
  const [start, setStart] = useState(0);
  const [end, setEnd] = useState(5);
  const [page, setPage] = useState(1);

  const baseUrl = "https://ec463-senior-design-stand-alone-solar.onrender.com/";

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
    axios.get(baseUrl.concat('luminanceTempGraphData')).then(result => {
      console.log(result.data)
      try{
        setLuminanceTimes(result.data[result.data.length-1].times.map(item => item.slice(11, 22)))
        setLuminances(result.data[result.data.length-1].luminances.map(item => item.$numberDecimal))
        setTemperatures(result.data[result.data.length-1].temperature_farenheit.map(item => item.$numberDecimal))
        setLuminanceList(result.data)
        // console.log(result)
      }
      catch(err){
        console.log(err)
        Alert.alert('sorry an error occcured whilst trying to get the days')
      }
      finally{
        setLoading3(false)
      }

    })

    axios.get(baseUrl.concat('getDays')).then(result => {
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

    axios.get(baseUrl.concat('get_luminance_and_temp')).then(result => {
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

    axios.get(baseUrl.concat('getCharge_graph')).then(result => {
      try{

        setChargeRate(result.data[result.data.length-1].charge_rate.map(item => item.$numberDecimal))
        setCharge_graphs(result.data)
      }
      catch(err){
        console.log(err)
        Alert.alert('sorry an error occcured whilst trying to get the charge rate graphs')
      }
    })
    

  }, [])

  function setDisplayData(x){
    setPower(x.power.map(item => item.$numberDecimal)); 
    setTimes(x.times.map(item => item.slice(11, 22)));
  }

  function findDay(array, date, luminanceArray, chargeRateArray){

    var formattedDate = date.slice(7,10) + '-' + date.slice(4,5) + '-' + date.slice(0,1)
    console.log(date)
    var flag = false
    for(var i=0; i<array.length; i++){
      if (array[i].date.slice(0, 10) === date){

        setSelectedDay(array[i].date.slice(0, 10))
        setPower(array[i].power.map(item => item.$numberDecimal)); 
        setTimes(array[i].times.map(item => item.slice(11, 22)));
        flag = true
      }
    }
    for(var i=0; i<luminanceArray.length; i++){
       if (luminanceArray[i].day.slice(0, 10) === date){
    //     setSelectedDay(luminanceArray[i].date.slice(0, 10))
         setLuminances(luminanceArray[i].luminances.map(item => item.$numberDecimal));
         if(luminanceArray[i].temperature_farenheit.length === 0) {
          setTemperatures(null)
          console.log('00000')
         }
         else {
          setTemperatures(luminanceArray[i].temperature_farenheit.map(item => item.$numberDecimal))
         }
         
    //     setTimes(array[i].times.map(item => item.slice(11, 22)));
    }
    }

    for(var i=0; i<chargeRateArray.length; i++){
      console.log(chargeRateArray[i].date)
      if (chargeRateArray[i].date.slice(0, 10) === date){
        setChargeRate(chargeRateArray[i].charge_rate.map(item => item.$numberDecimal)); 
      }
    }
    
  }

  function arrayList(array, start){
    if (!array || array === undefined){
      return null
    }

    return (array.map((item, index) => {
      // console.log(solarArray);
      
      return(
        <MDBTableBody key={index}>
          <tr onClick={() => {setDisplayData(item); setSelectedDay(item.date.slice(0, 10)), findDay(days, item.date.slice(0, 10).replaceAll('-', '/'), luminanceList, charge_graphs)}}>
            <th scope="row">{start+index+1}</th>
            <td className='tableRow' >
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
    console.log(luminanceList)
    findDay(days, searchQuery, luminanceList, charge_graphs)
    // props.setEmailAddress(props.email)
  }

  function handleReset() {
    console.log('reset')
  }



  

  return (
    <>
      {/*!-- library  --*/}


        <div className="page_content">
          
          <div className="row" style={{display: 'flex', flexWrap: 'wrap'}}>
            <div className="col"></div>

                <div className="col-5"> 
                  {/* <div className="card"> */}
                    <div className="card-body">
                      <h5 className="card-title">
                      <div className="text-center">{props.title}</div>
                      </h5>

                    </div>
                  { loading ? null : 

                  <div  style={{marginTop: "20px"}}>

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
                                        label: 'solar irradiation',
                                        data: luminances,
                                        backgroundColor: "black",
                                        borderColor: "black",
                                      },
                                      {
                                        label: 'temperature farenheit',
                                        data: temperatures,
                                        backgroundColor: "red",
                                        borderColor: "red",
                                      },
                                      {
                                        label: 'Charge Rate',
                                        data: chargeRate,
                                        backgroundColor: "grey",
                                        borderColor: "grey",
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


                            arrayList(days.slice(start, end), start)

                          
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
                        
                        {start > 0 ? 

                          <button className="btn" state={{id:props.email}} onClick={() => {setStart(start-5); setEnd(end-5); setPage(page-1)}}>back</button> 
                          
                          : 

                          null
                        }

                        {days.length > end ? 
                          <button className="btn" state={{id:props.email}} onClick={() => {setStart(start+5); setEnd(end+5); setPage(page+1)}}>next</button> 
                          
                          : 
                          
                          null
                          
                        }
                        

                      </div>

                      

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
                      Solar Irradiation: {lux} W/m^2<br/>
                      Temperature:  <br/> {tempC} °C | {tempF} °F
                      </p> 
                      
                      </div>
                      

                  </div>

                </div>
          </div>

          

        </div>


      
    </>
  );
}

export default AnalyticsPanel