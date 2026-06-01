var socket = io();

socket.on('connect', function() {
    console.log('Connected to WebSocket server');
    socket.send('Hello, server!');
});

socket.on('message', function(msg) {
    console.log('Received from server: ' + msg);
});