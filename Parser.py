from os.path import abspath, exists
from logging import error
from configparser import ConfigParser


class Parser:
    def __init__(self, file):
        self.file = file

    @property
    def file(self):
        return self.__file

    @file.setter
    def file(self, file):
        path = abspath(file)
        if exists(path):
            self.__file = path
        else:
            error("Error: path '{}' is not valid.".format(path))
            self.__file = None

    def read_ini(self):
        data_dict = {}
        if self.file is not None:
            config = ConfigParser()
            config.read(self.file)
            try:
                for key, value in config['DEFAULT'].items():
                    data_dict[key] = value
                return data_dict
            except (KeyError, AttributeError):
                error("Error: Wrong section name - {}".format('DEFAULT'))
        else:
            error("Error: Cannot find file {}.".format(self.file))

    def read_setting_value(self, expression):
        if self.file is not None:
            config_parser = ConfigParser()
            config_parser.read(self.file)
            default = config_parser['DEFAULT']
            for setting in default:
                if setting == expression:
                    return default[setting]
        else:
            error("Error: Cannot find file {}.".format(self.file))

    def save_data(self, data):
        config = ConfigParser()
        config['DEFAULT'] = data
        with open(self.file, 'w') as configfile:
            config.write(configfile)
