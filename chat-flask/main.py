from flask import Flask, render_template
from flask_socketio import SocketIO, send

#flask
app = Flask(__name__)

#socketio
app.config['SECRET_KEY'] = 'secret'
socketio = SocketIO(app)

@app.route('/')
def index():
   return render_template('index.html')

if __name__ == '__main__':
    socketio.run(app)