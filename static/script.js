// Reminder form show/hide script
function showForm() {
    const form = document.getElementById('form');
    form.classList.toggle("show");
}

// Login form toggler script
function changeForm() {
    const login = document.getElementById('login');
    const register = document.getElementById('register');
    const loginVisible = window.getComputedStyle(login).display !== "none";
    const button = document.getElementById('toggle-button');

    if (loginVisible) {
        login.style.display = "none";
        register.style.display = "block";
        button.textContent = "Login";
    } else {
        login.style.display = "block";
        register.style.display = "none";
        button.textContent = "Register";
    }
}