import serial
from flask import Flask, jsonify
from flask_cors import CORS

from serialreader import SerialReader

PORT = '/dev/ttyUSB0'

app = Flask(__name__)
CORS(app)
ser = serial.Serial(port=PORT, baudrate=19200)
reader = SerialReader(connection=ser)


@app.route("/")
def serve():
    return jsonify(reader.get_serial_data())


if __name__ == '__main__':
    app.run()
