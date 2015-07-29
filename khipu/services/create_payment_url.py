# -*- coding: utf-8 -*-
from collections import OrderedDict
from common import KhipuService


class KhipuServiceCreatePaymentURL(KhipuService):
    """
    Con esta opción puedes crear un pago desde tu servidor y obtener la URL
    para enviar a pagar a tus pagadores
    (tanto en escritorios como aplicaciones móviles).
    
    Parámetors que debe recibir la clase
    ====================================
    subject -> el asunto del cobro. Con un máximo de 255 caracteres.
    body -> descripción del cobro.
    amount -> el monto del cobro.
    notify_url ->
        la dirección de tu web service que utilizará khipu para
        notificarte de un pago realizado.
        ver: https://khipu.com/page/api#notification-instantanea
    return_url ->
        la dirección URL a donde enviar al cliente cuando el pago está
        siendo verificado
    cancel_url ->
        la dirección URL a donde enviar al cliente si se arrepiente
        de hacer la transacción
    transaction_id ->
        en esta variable puedes enviar un identificador propio de tu
        transacción, como un número de factura.
    expires_date ->
        fecha de expiración del cobro. Pasada esta fecha el cobro es inválido.
        Formato Unix timestamp. Debe corresponder a una fecha en el futuro.
    payer_email ->
        es el correo del pagador. Si lo envias, su correo aparecerá
        pre-configurado en la página de pago
    bank_id ->
        el código del banco.
        Puedes obtener los códigos usando la llamada receiverBanks
    picture_url ->
        una dirección URL de una foto de tu producto o servicio
        para mostrar en la página del cobro
    custom ->
        en esta variable puedes enviar información personalizada de la
        transacción, como por ejemplo, instrucciones de preparación
        o dirección de envio.
    
    Para el cálculo del parámetro hash debes referirte a la documentación
    de cálculo del hash. El orden de los parámetros es:
    >> receiver_id, subject, body, amount, payer_email, bank_id, expires_date,
    transaction_id, custom, notify_url, return_url, cancel_url, picture_url.
    """
    def __init__(self, receiver_id, secret, service_name, **kwargs):
        super(KhipuServiceCreatePaymentURL, self).__init__(
            receiver_id, secret, service_name, **kwargs)
        self.data = OrderedDict([
            ('receiver_id', receiver_id),
            ('subject', kwargs.pop('subject')),
            ('body', kwargs.pop('body')),
            ('amount', kwargs.pop('amount')),
            ('payer_email', kwargs.pop('payer_email')),
            ('bank_id', kwargs.pop('bank_id')),
            ('expires_date', kwargs.pop('expires_date')),
            ('transaction_id', kwargs.pop('transaction_id')),
            ('custom', kwargs.pop('custom')),
            ('notify_url', kwargs.pop('notify_url')),
            ('return_url', kwargs.pop('return_url')),
            ('cancel_url', kwargs.pop('cancel_url')),
            ('picture_url', kwargs.pop('picture_url'))
        ])
