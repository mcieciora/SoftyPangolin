from requests import get
from logging import info


class Request:
    def __init__(self, url, call_data, verified=False):
        self.url = url
        self.call_data = call_data
        self.__is_verified = verified

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url):
        self.__url = url

    @property
    def call_data(self):
        return self.__call_data

    @call_data.setter
    def call_data(self, data):
        if type(data) is dict:
            self.__call_data = data
            self.inject_data_into_url()

    def inject_data_into_url(self):
        data_list = []
        for key, value in self.call_data.items():
            data_list.append('{}={}'.format(key, value))
        self.url += '&'.join(data_list)

    def send(self):
        info("[INFO] Sending '{}' request...")
        return get(self.url)
