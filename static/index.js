document.addEventListener('DOMContentLoaded', function() {
    function createmessage(event) {
        event.preventDefault();
        const thing = document.createElement('p')
        var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);
        socket.on('connect', function() {
            /**
            const message = document.querySelector('#new_message').value;
            const username = localStorage.getItem('user');
            const channel = localStorage.getItem('channel');
            socket.emit('submit message', {'channel': channel, 'username': username, 'message':message});
            */
            socket.emit('submit message');
        });
    });

    socket.on('announce message', function(data) {
        /**
        const p = document.createElement('p');
        p.innerHTML = `${data.username}: ${data.message} ${data.timestamp}`;
        document.querySelector('#messages').append(p);
        */
        console.log("SOCKET IO WORKKSSSSSIUFERIUIRUEHIURG");
    });
});
