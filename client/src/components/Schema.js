import * as yup from "yup";

const passwordRules = /^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{5,}$/;
// min 5 characters, 1 upper case letter, 1 lower case letter, 1 numeric digit.

export const basicSchema = yup.object().shape({
  firstname: yup.string()
  .required('First name is required')
  .max(15, 'First name must be at most 15 characters long'),
  lastname: yup.string()
  .required('Last name is required')
  .max(15, 'Last name must be at most 15 characters long'),
  email: yup.string().email("Please enter a valid email").required("Required"),
  username: yup.string().required('Username is required'),
  anonymous: yup.string().required("Required"),

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