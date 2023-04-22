import React, { useState } from 'react'
import { Link, useNavigate} from 'react-router-dom'
import image from "./Components/images/log.jpeg";
import logo from "./Components/images/Logo2.png";



const Login = () => {
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");
//    console.log("username",username,"pass:",password)
const navigate = useNavigate();



const login =()=>{
    // alert("hi")
    if(username != "" && password !=""){
       navigate("/home")

    }
    else{
        alert('please fill the username and password')
    }

}
  return (
    <>
    <section className="vh-75" style={{backgroundColor: "#9A616D;", backgroundColor:"black"}}>
  <div className="container py-5 h-100">
    <div className="row d-flex justify-content-center align-items-center h-100">
      <div className="col col-xl-10">
        <div className="card" style={{borderRadius: "1rem;"}}>
          <div className="row g-0">
            <div className="col-md-6 col-lg-5 d-none d-md-block">
            {/* src="https://mdbcdn.b-cdn.net/img/Photos/new-templates/bootstrap-login-form/img1.webp" */}
              <img src= {image}
                alt="login form" className="img-fluid vh-100" style={{borderRadius: "1rem 0 0 1rem;"}} />
            </div>
            <div className="col-md-6 col-lg-7 d-flex align-items-center">
              <div className="card-body p-4 p-lg-5 text-black">

                <form>

                  <div className="d-flex align-items-center mb-3 pb-1">
                    {/* <i className="fas fa-cubes fa-2x me-3" style={{color: "#ff6219;"}}></i> */}
                    <span className="h1 fw-bold mb-0">
                        <img className='w-75' src={logo}/>
                    </span>
                  </div>

                  <h5 className="fw-normal mb-3 pb-3" >Sign into your account</h5>

                  <div className="form-outline mb-4">
                    <input type="email"
                     id="form2Example17"
                     value={username}
                     name="username"
                     onChange={(e)=>{
                        setUsername(e.target.value)
                     }}
                      className="form-control form-control-lg" />
                    <label className="form-label" for="form2Example17">Email address</label>
                  </div>

                  <div className="form-outline mb-4">
                    <input type="password"
                     id="form2Example27"
                     name='password'
                     onChange={(e)=>{
                        setPassword(e.target.value)
                     }}
                      className="form-control form-control-lg" />
                    <label className="form-label" for="form2Example27">Password</label>
                  </div>

                  <div className="pt-1 mb-4">
                    <button className="btn btn-dark btn-lg btn-block" type="button" onClick={login}>Login</button>
                  </div>

                  <a className="small text-muted" href="#!">Forgot password?</a>
                  <p className="mb-5 pb-lg-2" style={{color: "#393f81;"}}>Don't have an account? <Link to="/register"
                      style={{color: "#393f81;"}}>Register here</Link></p>
                  <a href="#!" className="small text-muted">Terms of use.</a>
                  <a href="#!" className="small text-muted">Privacy policy</a>
                </form>

              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>
      
    </>
  )
}

export default Login
