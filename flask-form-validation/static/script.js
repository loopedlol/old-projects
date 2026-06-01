function validation() {
    var username = document.getElementById("username");
    var error_username = document.getElementById("error_username");
    if (username.value == "") {
        username.style.border = "1px solid red";
        username.style.color = "red";
        error_username.textContent = "username is required";
        error_username.style.color = "red";
        username.focus();
        return false;
    }
    else {
        if (username.value.length <= 5) {
            error_username.innerHTML = "username is too short";
            error_username.style.color = "red";
            return false;
        }
        else {
            username.style.border = "1px solid green";
            username.style.color = "green";
            error_username.textContent = "";
        }
    }
}