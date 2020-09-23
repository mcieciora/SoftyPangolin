from requests import get


class Request:
    def __init__(self, url, data):
        self.url = url
        self.data = data

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data_dict):
        if type(data_dict) is dict:
            self.__data = data_dict
            self.set_url()

    def set_url(self):
        for k, v in self.data.items():
            self.url += '{}={}&'.format(k, v)

    # TODO refactor
    def send(self):
        r = get(self.url)
        if r.status_code == 200:
            return r.json()['current']
        else:
            return 'Error {}: {} at {}'.format(r.status_code, r.reason, r.url)
