const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const containerLogin = document.getElementById('containerLogin');

signUpButton.addEventListener('click', () => {
	containerLogin.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	containerLogin.classList.remove("right-panel-active");
});