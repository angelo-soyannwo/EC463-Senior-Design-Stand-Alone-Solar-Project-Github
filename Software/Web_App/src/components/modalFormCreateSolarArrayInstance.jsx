import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
// import "./css/modal.css";
import { useState } from 'react';
import axios from 'axios'
import Modal from 'react-bootstrap/Modal';
import mongoose from 'mongoose'


function ModalFormCSAI(props) {

    let buttonClear = document.querySelector('button')
    let inputs = document.querySelector('inputs')

    const [email, setEmail]= useState(props.email)

    const [show, setShow] = useState(false);
    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);
    const [arrayLocation, setArrayLocation] = useState('')
    const baseUrl = "http://localhost:8000/";

  async function createSolarArrayInstance(e) {
    e.preventDefault();

    const Data = {
      location:arrayLocation,
      solarPanels:[]
  }

    try{
        await axios.post(baseUrl.concat("createSolarArrayInstance"), Data).then(res=>{
          if(res.data === "notExist") {
            alert("Created Solar Array")
          }
        }).catch(e=>{
          alert(e)
          console.log(e)
        })
    }
    catch(e){
        console.log(e)
    }
}




  return (
  <>
    <button onClick={handleShow}>
      Create Solar Array Instance
    </button>

    <Modal show={show} onHide={handleClose}>
      <Modal.Header closeButton>
        <Modal.Title>Create Solar Array Instance</Modal.Title>
      </Modal.Header>
      <Modal.Body>

        
            <div className="mb-3">
            <label className="form-label">Array Location</label>
            <input type="id" onChange={(e)=>{setArrayLocation(e.target.value)}} className="form-control" id="arrayLocation" name="arrayLocation" placeholder="location"></input>
            </div>


            <button onClick={createSolarArrayInstance}>Create Solar Array</button>

      </Modal.Body>
      <Modal.Footer>
        
      </Modal.Footer>
    </Modal>
      
    </>
  );
}

export default ModalFormCSAI

