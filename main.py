from flask import Flask, render_template
from flask_socketio import SocketIO
from time import localtime, time, strftime
from urllib.parse import unquote
from pymongo import MongoClient

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jttyncG!cvisjrtu234512er~'
socketio = SocketIO(app)

in1 = "34.229.99.127"
in2 = "34.227.177.83"
in3 = "52.23.153.161"


client = MongoClient('mongodb://{0}:27017,{1}:27017,{2}:27017/?replicaSet=rs0'.format(in1, in2, in3))
db = client['test']
collection = db['messages']


@app.route('/')
def sessions():
    return render_template("session.html")


def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')


@socketio.on('message')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('[MESSAGE]:'.ljust(14, " ") + unquote(str(json)))
    cur_time = time()
    json['time'] = strftime('%Y.%m.%d %H:%M:%S', localtime(cur_time))
    json['timestamp'] = int(round(cur_time * 1000))
    socketio.emit('response', json, callback=messageReceived)
    collection.insert_one(json)


@socketio.on('connection')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    print('[CONNECTION]:'.ljust(14, " ") + str(json))
    socketio.emit('response', json, callback=messageReceived)
    for message in collection.find():
        print('[DEBUG]:'.ljust(14, " ") + unquote(str(message)))
        socketio.emit('response', message, callback=messageReceived)


if __name__ == '__main__':
    socketio.run(app, debug=True)