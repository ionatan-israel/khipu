import hashlib
import hmac
import requests


from . import version
__version__ = version.__version__


class KhipuAPI(object):
    """
    A client for the Khipu API.
    """
    base_url = 'https://khipu.com/api/1.3/'
    
    def __init__(self, receiver_id=None, secret=None):
        self.receiver_id = receiver_id
        self.secret = secret
        self._hash = hmac.new(
            secret, "receiver_id=" + receiver_id, hashlib.sha256
        ).hexdigest()
        self.data = {
            'receiver_id': receiver_id,
            'hash': self._hash
        }
        
    def request(self, path):
        return requests.post(self.base_url + path, data=self.data)
