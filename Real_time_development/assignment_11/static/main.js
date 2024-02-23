document.addEventListener('DOMContentLoaded', () => {
    var socket = io.connect('http://' + document.domain + ':' + location.port);

    socket.on('message', data => {
        var ul = document.getElementById('messages');
        var li = document.createElement('li');
        li.appendChild(document.createTextNode(data));
        ul.appendChild(li);
    });

    document.querySelector('form').onsubmit = () => {
        socket.emit('message', document.getElementById('input').value);
        document.getElementById('input').value = '';
        return false;
    };
});