import React, { useState } from "react";
import { useFormik, Field, FormikProvider } from "formik";
import * as yup from "yup";
import { useNavigate, Link } from "react-router-dom";
import '../stylesheets/SignUp.css'


export default function Login() {
    const navigate = useNavigate();
    const [checked, setChecked] = useState(true);
    const [flag, setFlag] = useState(1)

    function handleCheckChange(event) {
      event.target.checked = false;
      setChecked(!checked);
    }
  
    const formSchema = yup.object().shape({
        username: yup.string().required("Username is required"),
        password: yup.string()
          .min(5, "Password must be at least 5 characters")
          .required("Password is required"),
        user_role: yup.string().required("User role is required"),
    });
      
    const formik = useFormik({
      initialValues: {
        username: "",
        password: "",
        user_role: "",
      },
      validationSchema: formSchema,
      onSubmit: (values) => {
        fetch("/login", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify(values, null, 2),
        }).then((res) => {
          if (res.status === 200) {
            alert(res.status + ": You are now Logged In!")
            navigate("/");
            sessionStorage.setItem("loginStatus", "true");
            sessionStorage.setItem("users",JSON.parse(JSON.stringify(values, null, 2)).username);   // store username
            window.location.reload(); // reload to change button text from login to logout
            setFlag(1);
          }else{
            setFlag(2);  // This will display invalid login 
          }
        });
      },
    });

    return(
      <FormikProvider value={formik}>

        <div className='sign-app'>
          <div className='container'>
            <h1>Please Login</h1>
            <form onSubmit={formik.handleSubmit} style={{ margin: "30px" }}>
                  
              {/* username */}
              <div className='input-container'>
                <label htmlFor="username">
                Username
                </label>
                <input
                    id="username"
                    type="text"
                    name="username"
                    placeholder='username'
                    onChange={formik.handleChange}
                    value={formik.values.username}
                />
                <p style={{ color: "red" }}> {formik.errors.username}</p>
              </div>

              {/* password */}
              <div className='input-container'>
                <label htmlFor="password">
                Password
                </label>
                <input
                    id="password"
                    type='password'
                    name="password"
                    placeholder="password"
                    onChange={formik.handleChange}
                    value={formik.values.password}
                />
                <p style={{ color: "red" }}> {formik.errors.password}</p>                    
              </div>

              {/* user role */}
              <div className='input-container'>
                  <label htmlFor="user_role">
                  Administrator / Donor
                  </label>
                  <Field
                    as="select"
                    name="user_role"
                    className="field"
                    onChange={formik.handleChange}
                  >
                    <option>Select User Role</option>
                    <option value="administrator">Administrator</option>
                    <option value="donor">Donor</option>
                  </Field>
                  <p style={{ color: "red" }}> {formik.errors.user_role}</p>
              </div>

              <button type="submit">
              Submit
              </button>

              {/* remember me */}
              <div className='input-container'>
                <label>
                  <input
                      type="checkbox"
                      checked={checked}
                      onChange={handleCheckChange}
                      name="rememberme"
                  />
                Remember me
                </label>
              </div>

              {/* Sign up */}
              <div className='input-container'>
                <Link to={"/signup"} className="signup">
                    Register Here
                </Link>
              </div>   

              {/* Forgot password */}
              <div className='input-container'>
                <span className="passwd"> Forgot
                  <a href="/#"> password?</a>
                </span>
              </div>

              { flag === 2 && <p style={{ color: 'red', lineHeight : 3, paddingTop: '0.5em', fontSize: "large", fontWeight: "bold" }}>Invalid login credentials, please try again!</p>}

            </form>
          </div>
        </div>
      </FormikProvider>
    );
    };



