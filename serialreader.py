class SerialReader:
    """ A serial connection reader """

    def __init__(self, connection):
        """ Initialise a reader with the given serial connection """
        self.connection = connection
        self._latest_data = "0, 0"
        self._return_status = "new"

    def get_serial_data(self):
        """ Return usable velocity-position data """
        raw_data = self.read_serial_data()
        data = [int(val) for val in raw_data.split(',')]
        return {
            'velocity': data[0],
            'position': data[1],
            'status': self._return_status,
        }

    def read_serial_data(self):
        """ Read the latest velocity-position pair """
        try:
            data = self.connection.read_all().splitlines()[-1].decode()
            self._latest_data = data
            self._return_status = "new"
            return data
        except IndexError:
            self._return_status = "cached"
            return self._latest_data

    def close_serial_connection(self):
        """ Close serial connection """
        self.connection.close()
