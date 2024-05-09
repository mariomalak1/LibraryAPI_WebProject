function loginB() {
  let UN = document.getElementById("username").value;
  let pass = document.getElementById("password").value;
  let isadmin = document.getElementById("is-admin").checked;

  let storedUsers = localStorage.getItem("user");
  if (storedUsers) {
    let users = JSON.parse(storedUsers);
    let matchingUser = users.find(
      (user) => user.username === UN && user.password === pass
    );
    if (matchingUser) {
      if (isadmin && matchingUser.isAdmin) {
        window.location.href = "Admin.html";
      } else if (isadmin && !matchingUser.isAdmin) {
        alert("You are not authorized to log in as an admin.");
      } else if (!isadmin && matchingUser.isAdmin) {
        alert("No User ");
      } else {
        window.location.href = "User.html";
      }
    } else {
      alert("Incorrect username or password.");
    }
  } else {
    alert("No users found. Please sign up.");
  }
}
