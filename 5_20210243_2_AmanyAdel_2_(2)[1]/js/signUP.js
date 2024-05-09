const UN = document.getElementById("username");
const pass = document.getElementById("password");
const confirmPassword = document.getElementById("confirm-password");
const email = document.getElementById("email");
const isAdmin = document.getElementById("is-admin");
let UserContainer = [];

if (localStorage.getItem("user") != null) {
  UserContainer = JSON.parse(localStorage.getItem("user"));
}

function SignUP() {
  if (!validateUsername(UN.value)) {
    alert("Enter a valid username (3-10 characters, letters only)");
    return;
  }

  if (!validateEmail(email.value)) {
    alert("Enter a valid email");
    return;
  }

  if (!validatePassword(pass.value)) {
    alert("Enter a valid password (6-16 characters)");
    return;
  }

  if (pass.value !== confirmPassword.value) {
    alert("Passwords do not match");
    return;
  }

  const User = {
    username: UN.value,
    password: pass.value,
    Email: email.value,
    isAdmin: isAdmin.checked,
  };

  UserContainer.push(User);
  localStorage.setItem("user", JSON.stringify(UserContainer));
  window.location.href = "login.html";
}

function validateUsername(username) {
  const nameregex = /^[A-Za-z]{3,10}$/; 
  return nameregex.test(username);
}

function validateEmail(email) {
  const emailRegex = /^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$/;
  return emailRegex.test(email);
}

function validatePassword(password) {
  const passregex = /^[a-zA-Z0-9!@#$%^&*]{6,16}$/;
  return passregex.test(password);
}
