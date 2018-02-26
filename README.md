### Plot serial data on a web browser

The application back-end is implemented in Python, so Python (Python 3, of course) is required.

#### Configuration

* Install requirements (ideally on a virtual environment): `pip install -r requirements.txt`
* Connect your device to your computer. You can use an Arduino and `serial_source.ino` for testing.
* Find which port your device is connected to and change `PORT` variable in `server.py` accordingly.

#### Running

* Run local web server which reads serial data and publishes: `FLASK_APP=server.py flask run`
* Open `graph.html` in your favorite web browser and enjoy!