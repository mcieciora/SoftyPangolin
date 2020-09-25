from requests import get
from logging import info, error


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

    def verify_url(self):
        if (request := get(self.url)).status_code != 200:
            error('Error {}: {} at {}. Url or data is not valid.'.format(request.status_code, request.reason, self.url))
        else:
            info("[INFO] '{}' has been verified.".format(self.url))
            self.__is_verified = True

    def send(self):
        if self.__is_verified:
            info("[INFO] Sending '{}' request...")
            request = get(self.url)
            if request.status_code == 200:
                info('[SUCCESS] Code 200 received.')
                return request.json()['current']
        else:
            error("[ERR] Cannot send '{}' request, url or data is not valid.".format(self.url))
