# -*- coding: utf-8 -*-

import imp
import os
import services


# Definimos la ruta de Khipu
# KHIPU_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Khipu(object):
    """
    Provee y centraliza la carga de los servicios que presta Khipu
    """
    # Corresponde al ID del cobrador.
    receiver_id = None
    # Corresponde a la llave del cobrador.
    secret = None
    
    # diccionario que contiene los nombres de los servicios que existen
    # y si requieren autenticación
    services = {
        'CreateEmail': True,
        'CreatePaymentPage': True,
        'CreatePaymentURL': True,
        'VerifyPaymentNotification': False,
        'ReceiverStatus': True,
        'SetBillExpired': True,
        'SetPaidByReceiver': True,
        'SetRejectedByPayer': True,
        'PaymentStatus': True,
        'UpdatePaymentNotificationUrl': True,
        'ReceiverBanks': True,
        'GetPaymentNotification': True
    }
    
    def authenticate(self, receiver_id, secret):
        """
        Identificar al cobrador que utilizara los servicios.
        No es necesario para utilizar el servicio VerifyPaymentNotification.
        """
        self.receiver_id = receiver_id
        self.secret = secret

    def load_service(self, service_name):
        """
        Carga el servicio y retorna el objecto, en caso de no existir
        el servicio, se invoca una excepcion
        """
        if service_name in self.services:
            # Es requerido identificarse para usar estos servicios
            if self.receiver_id and self.secret:
                class_name = 'KhipuService' + service_name
                return getattr(services, class_name)(self.receiver_id, self.secret, service_name)
            else:
                raise KhipuError(
                    "Is necessary to authenticate to use the service {0}".format(
                        service_name))
        else:
            # Invocamos un Exception
            raise KhipuError(
                "The service {0} does not exist".format(service_name))


class KhipuError(Exception):
    
    def __init__(self, result):
        Exception.__init__(self, result)
