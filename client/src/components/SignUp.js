import React,{useState} from 'react'
import {useFormik } from 'formik'
import { useNavigate } from 'react-router-dom';
import { basicSchema } from "./Schema"
import '../stylesheets/SignUp.css'
import { ToastContainer, toast } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';


function SignUp() {
    const navigate = useNavigate();
    const [flag, setFlag] = useState(1)
    const notify = () => toast("Sign-Up successful!");
    
    const formik = useFormik({
        initialValues: {
          firstname : '',
          lastname : '',
          email : '',
          anonymous: '',
          username: '',
          password : '',
          confirmPassword : ''
        },
        validationSchema :basicSchema,
        onSubmit: (values) => {
          fetch("/signup", {
            method: "POST",
            headers: {
              "Content-Type": "application/json",
              'Accept': 'application/json',
            },
            body: JSON.stringify(values, null, 2),
          }).then((res) => {
            if (res.status === 201) {
              notify();
              setTimeout(function(){
                navigate("/login");
             }, 5000);
              setFlag(1);
            }else{
              setFlag(2);   // This will display error 422 Unprocessable Entity 
            }
          });
        },
      })

  return (
  <div className='sign-app'>
    <div className='sign_container'>
      <h1> Sign Up</h1>
      <form onSubmit={formik.handleSubmit} autoComplete="off">
      
        <div className='input-container'>
          <label htmlFor="firstname">First name</label>
          <input 
          id='firstname' 
          name='firstname' 
          type='text' 
          placeholder='firstname' 
          onChange={formik.handleChange}
          onBlur={formik.handleBlur}
          value={formik.values.firstname}
          className={formik.errors.firstname && formik.touched.firstname ? "input-error" : ""}
          />
          {formik.touched.firstname && formik.errors.firstname ? <p className='error'>{formik.errors.firstname}</p> : null}
        </div>

        <div className='input-container'>
          <label htmlFor="lastname">Last name </label>
          <input 
          id='lastname' 
          name='lastname' 
          type='text' 
          placeholder='lastname' 
          onChange={formik.handleChange} 
          onBlur={formik.handleBlur}
          value={formik.values.lastname}
          className={formik.errors.lastname && formik.touched.lastname ? "input-error" : ""}
          />
          {formik.touched.lastname && formik.errors.lastname ? <p className='error'>{formik.errors.lastname}</p> : null}
        </div>

        <div className='input-container'>
          <label htmlFor="email">E-mail</label>
          <input 
          id='email' 
          name='email' 
          type='email' 
          placeholder='email' 
          onChange={formik.handleChange}
          onBlur={formik.handleBlur}
          value={formik.values.email}
          className={formik.errors.email && formik.touched.email ? "input-error" : ""}/>
          {formik.touched.email && formik.errors.email ? <p className='error'>{formik.errors.email}</p> : null}
        </div>

        <div className='input-container'>
          <label htmlFor="username">Username </label>
          <input 
          id='username' 
          name='username' 
          type='text' 
          placeholder='username' 
          onChange={formik.handleChange} 
          onBlur={formik.handleBlur}
          value={formik.values.username}
          className={formik.errors.username && formik.touched.username ? "input-error" : ""}/>
          {formik.touched.username && formik.errors.username ? <p className='error'>{formik.errors.username}</p> : null}
        </div>

        <div className='input-container'>
          <label htmlFor="password">Password</label>
          <input 
          id='password' 
          name='password' 
          type='password' 
          placeholder='password' 
          autoComplete="off" 
          onChange={formik.handleChange} 
          onBlur={formik.handleBlur}
          value={formik.values.password} 
          className={formik.errors.password && formik.touched.password ? "input-error" : ""}
          />
          {formik.touched.password && formik.errors.password? <p className='error'>{formik.errors.password}</p> : null}
        </div>

        <div className='input-container'>
          <label htmlFor="confirmPassword">Confirm Password</label>
          <input 
          id="confirmPassword" 
          type="password" 
          autoComplete="off" 
          placeholder="Confirm password" 
          value={formik.values.confirmPassword} 
          onChange={formik.handleChange} 
          onBlur={formik.handleBlur} 
          className={formik.errors.confirmPassword && formik.touched.confirmPassword ? "input-error" : ""}
          />
          {formik.errors.confirmPassword && formik.touched.confirmPassword && (
            <p className="error">{formik.errors.confirmPassword}</p>
          )}
        </div>

        <div className='input-container'>
          <label htmlFor="anonymous">Anonymous? </label>
          <input 
          id='anonymous' 
          name='anonymous' 
          type='text' 
          placeholder='Yes/No' 
          onChange={formik.handleChange} 
          onBlur={formik.handleBlur}
          value={formik.values.anonymous}
          className={formik.errors.anonymous && formik.touched.anonymous ? "input-error" : ""}
          />
          {formik.touched.anonymous && formik.errors.anonymous ? <p className='error'>{formik.errors.anonymous}</p> : null}
        </div>

        <button type="submit">
          Register 
        </button>

        { flag === 2 && <p style={{ color: 'red', lineHeight : 3, paddingTop: '0.5em', fontSize: "large", fontWeight: "bold" }}>Error 422: Unprocessable Entity!</p>}

        <ToastContainer />

      </form>
    </div>
  </div>    
  )
}

export default SignUp