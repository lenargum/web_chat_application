from flask import Flask, render_template
from flask_socketio import SocketIO
from time import localtime, time, strftime
from urllib.parse import unquote
from pymongo import MongoClient, ASCENDING
from bson import ObjectId
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = 'jttyncG!cvisjrtu234512er~'
socketio = SocketIO(app)

in1 = "34.229.99.127"
in2 = "34.227.177.83"
in3 = "52.23.153.161"

client = MongoClient('mongodb://{0}:27017,{1}:27017,{2}:27017/?replicaSet=rs0'.format("in1", "in2", "in3"))
db = client['test']
collection = db['messages']


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


@app.route('/')
def sessions():
    return render_template("session.html")


def messageReceived(methods=['GET', 'POST']):
    print('message was received!!!')


@socketio.on('message')
def handle_my_custom_event(json, methods=['GET', 'POST']):
    if json['user_name'] == 'lenargum' and json['message'] == 'reset':
        collection.delete_many()
        print('[INFO]:'.ljust(14, " ") + "Database reset")
        socketio.emit('response', {}, callback=messageReceived)
    else:
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

    for message in collection.find().sort([("timestamp", ASCENDING)]):
        del message['_id']
        loaded_json = message
        print('[DEBUG]:'.ljust(14, " ") + str(type(loaded_json)) + ":" + unquote(str(loaded_json)))
        socketio.emit('response', loaded_json, callback=messageReceived)


if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0')
