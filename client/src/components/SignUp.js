import React,{useState} from 'react'
import {useFormik } from 'formik'
import { useNavigate } from 'react-router-dom';
import { basicSchema } from "./Schema"
import '../stylesheets/SignUp.css'


function SignUp() {
    const navigate = useNavigate();
    const [isLoading, setIsLoading] = useState(false)
    const onSubmit = async (values, actions) => {
      setIsLoading(true); 
      console.log(values);
      console.log(actions);
      await new Promise((resolve) => setTimeout(resolve, 1000));
      actions.resetForm();
      setIsLoading(false);
      navigate('/login');
    };
    const { values,
      errors,
      touched,
      isSubmitting,
      handleBlur,
      handleChange,
      handleSubmit,} = useFormik({
        initialValues: {
          firstName : '',
          lastName : '',
          email : '',
          password : '',
          confirmPassword : ''
        },
        validationSchema :basicSchema,
        onSubmit,
      })

  return (
  <div className='sign-app'>
  <div className='container'>
    <h1> Create Account</h1>
    <form onSubmit={handleSubmit} autoComplete="off">
     
    <div className='input-container'>
    <label htmlFor="firstname">FirstName</label>
      <input id='firstName' name='firstName' type='text' placeholder='firstname' 
      onChange={handleChange}
      onBlur={handleBlur}
      value={values.firstName}
      className={errors.firstName && touched.firstName ? "input-error" : ""}/>
      {touched.firstName && errors.firstName ? <p className='error'>{errors.firstName}</p> : null}
    </div>

    <div className='input-container'>
    <label htmlFor="lastname">lastName </label>
      <input id='lastName' name='lastName' type='text' placeholder='lastname' 
       onChange={handleChange} 
       onBlur={handleBlur}
       value={values.lastName}
       className={errors.lastName && touched.lastName ? "input-error" : ""}/>
      {touched.lastName && errors.lastName ? <p className='error'>{errors.lastName}</p> : null}
     </div>

     <div className='input-container'>
     <label htmlFor="email">Email</label>
      <input id='email' name='email' type='email' placeholder='email' 
       onChange={handleChange}
       onBlur={handleBlur}
       value={values.email}
       className={errors.email && touched.email ? "input-error" : ""}/>
      {touched.email && errors.email ? <p className='error'>{errors.email}</p> : null}
      </div>

      <div className='input-container'>
      <label htmlFor="password">Password</label>
      <input id='password' name='password' type='password' placeholder='password'
       onChange={handleChange}
       onBlur={handleBlur}
       value={values.password}
       className={errors.password && touched.password ? "input-error" : ""}/>
       {touched.password && errors.password? <p className='error'>{errors.password}</p> : null}
      </div>

      <div className='input-container'>
      <label htmlFor="confirmPassword">Confirm Password</label>
      <input
        id="confirmPassword"
        type="password"
        placeholder="Confirm password"
        value={values.confirmPassword}
        onChange={handleChange}
        onBlur={handleBlur}
        className={
          errors.confirmPassword && touched.confirmPassword ? "input-error" : ""
        }
      />
      {errors.confirmPassword && touched.confirmPassword && (
        <p className="error">{errors.confirmPassword}</p>
      )}
      </div>
      <button disabled={isSubmitting || isLoading} type="submit">
                        {isLoading ? "Registering..." : "Register"} </button>

     </form>
     </div>
     </div>
  
    
  )
}

export default SignUp