function send(section) {
    var name = document.getElementById("name").value;
    var subject = document.getElementById("subject").value;
    var para = document.getElementById("para").value;
    document.getElementById("section").innerHTML =
        "<h2>" + subject + "</h2><p>" + para + "</p><p>posted by " + name + " in " + section + "</p>";
}
