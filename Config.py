from configparser import ConfigParser
from os.path import abspath, exists
from sys import exit


class Config:
    def __init__(self, config_file, data_file):
        self.config_file = config_file
        self.data_file = data_file

    @property
    def config_file(self):
        return self.__config_file

    @config_file.setter
    def config_file(self, config_file_path):
        self.__config_file = self.set_file(config_file_path)

    @property
    def data_file(self):
        return self.__data_file

    @data_file.setter
    def data_file(self, data_file_path):
        self.__data_file = self.set_file(data_file_path)

    def set_file(self, file):
        path = abspath(file)
        if exists(path):
            return path
        else:
            # TODO find better way to handle this
            print('[ERROR] File {} does not exist'.format(path))
            exit(0)

    def save_data(self, data):
        config = ConfigParser()
        data['weather'] = data['weather'][0]['description']
        config['DEFAULT'] = data
        with open(self.data_file, 'w') as configfile:
            config.write(configfile)

    # TODO refactor
    def read_data(self):
        config = ConfigParser()
        config.read(self.data_file)
        default = config['DEFAULT']
        units = {
            'date': '',
            'weather': '',
            'temp': '°C',
            'feels_like': '°C',
            'pressure': 'hpa',
            'wind_speed': 'm/s',
            'clouds': '%',
            'humidity': '%'
        }
        ret_val = {}
        for k, v in default.items():
            try:
                if type(v) is int:
                    v = round(v, 1)
                a = units[k]
                ret_val[k] = v+a
            except KeyError:
                pass
        return ret_val

    def read_config(self):
        config = ConfigParser()
        config.read(self.config_file)
        data_dict = {}
        for section in config.sections():
            for key, value in config[section].items():
                data_dict[key] = value
        return data_dict
