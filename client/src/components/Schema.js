import * as yup from "yup";

const passwordRules = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{5,}$/;
// min 5 characters, 1 upper case letter, 1 lower case letter, 1 numeric digit.

export const basicSchema = yup.object().shape({
  firstName: yup.string()
  .required('firstname is required')
  .max(15, 'First name must be at most 15 characters long'),
  lastName: yup.string()
  .required('lastname is required')
  .max(15, 'LastName must be at most 15 characters long'),
  email: yup.string().email("Please enter a valid email").required("Required"),
  username: yup.string().required('Username is required'),
  user_role: yup.string().required('Please select user role'),

  password: yup
    .string()
    .min(5)
    .matches(passwordRules, { message: "Please create a stronger password" })
    .required("Required"),
  confirmPassword: yup
    .string()
    .oneOf([yup.ref("password"), null], "Passwords must match")
    .required("Required"),
});