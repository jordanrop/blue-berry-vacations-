// const signUpButton = document.getElementById('signUp');
// const signInButton = document.getElementById('signIn');
// const container = document.getElementById('container');

// signUpButton.addEventListener('click', () => {
// 	container.classList.add("right-panel-active");
// });

// signInButton.addEventListener('click', () => {
// 	container.classList.remove("right-panel-active");
// });

const togglePassword = document.querySelector('#togglePassword');
          
const password = document.querySelector('#id_password');

togglePassword.addEventListener('click', function (e) {

	// Toggle the type attribute
	const type = password.getAttribute(
		'type') === 'password' ? 'text' : 'password';
	password.setAttribute('type', type);
	

	// Toggle the eye slash icon
	if (togglePassword.src.match(
		"https://media.geeksforgeeks.org/wp-content/uploads/20210917145551/eye.png")) {
		togglePassword.src =
		"https://media.geeksforgeeks.org/wp-content/uploads/20210917150049/eyeslash.png";
	} else {
		togglePassword.src =
		"https://media.geeksforgeeks.org/wp-content/uploads/20210917145551/eye.png";
	}
});
