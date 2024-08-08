document.addEventListener('DOMContentLoaded', function () {
    // Walidacja email
    const emailInput = document.getElementById('id_email');
    const emailError = document.getElementById('email-error');

    if (emailInput) {
        emailInput.addEventListener('input', function () {
            const email = emailInput.value;
            if (!validateEmail(email)) {
                emailError.textContent = 'Please enter a valid email address.';
                emailError.style.display = 'block';
            } else {
                emailError.textContent = '';
                emailError.style.display = 'none';
            }
        });
    }

    function validateEmail(email) {
        const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        return re.test(String(email).toLowerCase());
    }

    // Walidacja hasła
    const passwordInput = document.getElementById('id_password1');
    const passwordError = document.getElementById('password-error');

    if (passwordInput) {
        passwordInput.addEventListener('input', function () {
            const password = passwordInput.value;
            if (password.length < 8) {
                passwordError.textContent = 'Password must be at least 8 characters long.';
                passwordError.style.display = 'block';
            } else {
                passwordError.textContent = '';
                passwordError.style.display = 'none';
            }
        });
    }

    // Walidacja zgodności haseł
    const confirmPasswordInput = document.getElementById('id_password2');
    const confirmPasswordError = document.getElementById('confirm-password-error');

    if (confirmPasswordInput) {
        function validatePasswords() {
            if (passwordInput.value !== confirmPasswordInput.value) {
                confirmPasswordError.textContent = 'Passwords do not match.';
                confirmPasswordError.style.display = 'block';
            } else {
                confirmPasswordError.textContent = '';
                confirmPasswordError.style.display = 'none';
            }
        }

        passwordInput.addEventListener('input', validatePasswords);
        confirmPasswordInput.addEventListener('input', validatePasswords);
    }
});
