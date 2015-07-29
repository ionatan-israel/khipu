# -*- coding: utf-8 -*-
import hashlib
import hmac
import requests

VERSION_KHIPU_SERVICE = '1.3'


class KhipuService(object):
    """
    A client for the Khipu API.
    """
    # Url del servicio
    api_url = 'https://khipu.com/api/%s/' % VERSION_KHIPU_SERVICE
    # diccionario de datos que se enviarán al servicio
    data = None
    # mensaje en caso de error u otro evento
    message = None
    requests = requests
    
    def __init__(self, receiver_id, secret, service_name, **kwargs):
        """
        Por defecto iniciamos el servicio identificando al cobrador.
        """
        # id del cobrador
        self.receiver_id = receiver_id
        # Llave del cobrador
        self.secret = secret
        # Nombre del servicio
        self.service_name = service_name

    def set_parameter(self, name, value):
        """
        Método para adjuntar el valor a uno de los elementos que
        contempla el diccionario self.data. Esta función solo registrará los
        valores que estan definidos en el arreglo
        """
        if 'name' in self.data:
            self.data[name] = value
    
    def set_parameters(self, values):
        """
        Método para guardar, desde un diccionario, todos los elementos que debe
        tener el diccionario data
        """
        for name, value in values.iteritems():
            self.set_parameter(name, value)

    def do_hash(self):
        """
        Genera el Hash que requiere khipu.
        """
        return hmac.new(self.secret, self.concatenated(), hashlib.sha256).hexdigest()
        
    def concatenated(self):
        cad = ''
        for key, value in self.data.iteritems():
            cad += '{0}={1}&'.format(key, value)
        return cad[0:-1]
    
    def get_url_service(self):
        return self.api_url + self.service_name

    def request(self):
        self.data['hash'] = self.do_hash()
        return self.requests.post(self.get_url_service(), self.data).json()
