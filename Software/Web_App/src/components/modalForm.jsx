import React from "react";
import 'bootstrap/dist/css/bootstrap.min.css';
// import "./css/modal.css";
import { useState } from 'react';
import axios from 'axios'
import Modal from 'react-bootstrap/Modal';


function ModalForm(props) {

    let buttonClear = document.querySelector('button')
    let inputs = document.querySelector('inputs')


    

    const [email, setEmail]= useState(props.email)

    const [show, setShow] = useState(false);
    const handleClose = () => setShow(false);
    const handleShow = () => setShow(true);
    const [id, setId] = useState('')
    // const [refresh, setRefresh] = useState(false)

  async function addSolarArray(e) {
    e.preventDefault();

    try{
        await axios.post("http://localhost:8000/addSolarArray", {email:email, arrayId:id}).then(res=>{
          if(res.data === "notExist") {
            alert("Check array details")
          }
          else if(res.data==="exists"){
            window.location.reload();
            alert('Solar Array Added')
          }
          else if (res.data==="solarArrayAlreadySelected"){
            alert('You already have access to this solar array')
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
      Add Solar Array to your account
    </button>

    <Modal show={show} onHide={handleClose}>
      <Modal.Header closeButton>
        <Modal.Title>Add Solar Array</Modal.Title>
      </Modal.Header>
      <Modal.Body>

        
            <div className="mb-3">
            <label className="form-label">Array ID</label>
            <input type="id" onChange={(e)=>{setId(e.target.value)}} className="form-control" id="id" name="id" placeholder="id"></input>
            </div>


            <button onClick={addSolarArray}>Add solar Array</button>


                    
    

      
      </Modal.Body>
      <Modal.Footer>
        
      </Modal.Footer>
    </Modal>

      
    </>
  );
}

export default ModalForm

