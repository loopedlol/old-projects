$(document).ready(function(){

    const socket = io("/test");

    socket.on("a_new_message", function(msg) {
        $("#log").append(`<p>Received: ${msg.data}</p>`)
    });

    $("form#message").on("submit", function(e){
        e.preventDefault();

        socket.emit("form_submitted", { data: $("#message_data").val() });

        document.getElementById("message").reset();
    });
})