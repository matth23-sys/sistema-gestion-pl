document.addEventListener("DOMContentLoaded", () => {

    const passwordInput =
        document.getElementById("id_password");

    const passwordToggle =
        document.getElementById("passwordToggle");


    if (!passwordInput || !passwordToggle) {
        return;
    }


    passwordToggle.addEventListener("click", () => {

        const hidden =
            passwordInput.type === "password";


        passwordInput.type =
            hidden
                ? "text"
                : "password";


        passwordToggle.textContent =
            hidden
                ? "Hide"
                : "Show";


        passwordToggle.setAttribute(
            "aria-label",
            hidden
                ? "Hide password"
                : "Show password"
        );

    });

});