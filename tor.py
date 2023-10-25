import stem.connection
from stem import Signal
from stem.control import Controller
import requests

class Tor:
    def __init__(self, tor_port=9051, tor_host="127.0.0.1", tor_socks_port=9050):
        self.tor_port = tor_port
        self.tor_host = tor_host
        self.tor_socks_port = tor_socks_port
        self.session = None

    def _create_session(self):
        self.session = requests.session()
        self.session.proxies = {
            "http": f"socks5://{self.tor_host}:{self.tor_socks_port}",
            "https": f"socks5://{self.tor_host}:{self.tor_socks_port}",
        }

    def _renew_identity(self):
        with Controller.from_port(port=self.tor_port) as controller:
            controller.authenticate()
            controller.signal(Signal.NEWNYM)

    def tor_get(self, url):
        self._create_session()
        response = self.session.get(url)
        return response.text

    def tor_post(self, url, data=None, json=None):
        self._create_session()
        response = self.session.post(url, data=data, json=json)
        return response

    '''
    # GET example
    tor_client = Tor()
    url_to_access = "https://duckduckgo.com/"
    response_text = tor_client.tor_get(url_to_access)
    print(response_text)

    
    # POST example
    data_to_post = {"key": "value"}
    url_to_post = "https://example.com/post"
    response_text = tor_client.tor_post(url_to_post, data=data_to_post)
    print(response_text)
    '''