import React, { useState } from 'react'
import Swal from "sweetalert2";

function EmailSend() {
    const [isLoading, setIsLoading] = useState(false);
    const[subject,changeSubject]=useState("");
    const[message,changeMessage]=useState("");

    const handleSubmit=(e)=>{
      e.preventDefault();
      const empdata={subject,message};
      setIsLoading(true);
      fetch("http://127.0.0.1:8000/send-bulk-email/",{
        method:"POST",
        headers:{"content-type":"application/json"},
        body:JSON.stringify(empdata)

      }).then((res)=>{
        changeSubject("");
        changeMessage("");
        if (res.status == 200){
            Swal.fire({
                title: "Success",
                text: "Successfully Send",
                icon: "success",
                confirmButtonText: "OK",
              })
        }else{
        Swal.fire({
            title: "error",
            text: 'something is wrong',
            icon: "error",
            confirmButtonText: "OK",
            })
        }
        setIsLoading(false);
      }).catch((err)=>{
        console.log(err)
        Swal.fire({
            title: "error",
            text: 'something is wrong',
            icon: "error",
            confirmButtonText: "OK",
          })
      })
  
    }
  return (
    <div>
        <div class="card col-11 col-md-6 mx-auto mt-4">
          <div class="card-body">
          
          <form onSubmit={handleSubmit}>
            <label>Email Subject</label>
            <input className='form-control' required value={subject}  onChange={e=>changeSubject(e.target.value)} placeholder='Email Subject' /><br />
            <label>Message</label>
            <textarea className='form-control'  required value={message}  onChange={e=>changeMessage(e.target.value)} placeholder='Email Message' cols="20" rows="5"></textarea>
              <div className='text-center'>
                <button className='btn btn-dark mt-3' type='submit'>Send</button>
                <h2>{isLoading ?'Loding...'  : ''}</h2>
              </div>
            </form>
          </div>
        </div>    
    </div>
  )
}

export default EmailSend