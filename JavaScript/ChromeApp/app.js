const loginForm = document.querySelector("#login-form");
const loginInput = document.querySelector("#login-form input");
const greeting = document.querySelector("#greeting");

const link = document.querySelector("a");

function onUserNameSubmit(event) {
  event.preventDefault();
  loginForm.classList.add("hidden");
  const userName = loginInput.value;
  greeting.innerText = "Hello " + userName;
  greeting.classList.remove("hidden");
}

loginForm.addEventListener("submit", onUserNameSubmit);
