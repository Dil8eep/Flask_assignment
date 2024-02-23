from flask import Flask, render_template
from flask_socketio import SocketIO

app = Flask(__name__)
socketio = SocketIO(app)

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('update_data')
def handle_update_data(data):
    # Do something with the updated data (e.g., store it in a database)
    print(f"Received updated data: {data}")

    # Broadcast the updated data to all connected clients
    socketio.emit('updated_data', data)

if __name__ == '__main__':
    socketio.run(app, host="0.0.0.0",port=5050)