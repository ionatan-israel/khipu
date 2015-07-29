# Python wrapper for the Khipu API

[Khipu](https://khipu.com/home) es un servicio que facilita los cobros y la facturación web en **Chile**.

Para comenzar a escribir el código me base en la biblioteca php https://github.com/Tifon-/Khipu

La documentación de Khipu.com se puede ver desde aquí: [http://khipu.com/page/api](http://khipu.com/page/api)

## Instalación
```shell
pip install git+https://github.com/jrperdomoz/khipu
```

## Ejemplos

##### 1) Verificar Estado de una cuenta Khipu

Este servicio permite consultar el estado de una cuenta khipu, la cual retorna
un json mencionando el ambiente en que se encuentra y si puede recibir pagos.
A continuación un ejemplo:

```python
from khipu import Khipu
api = Khipu('receiver_id', 'secret_key')
api.service('ReceiverStatus')
>> {u'type': u'production', u'ready_to_collect': True}
```
---

##### 2) Crear URL para un pago
Con esta opción puedes crear un pago desde tu servidor y obtener la URL para enviar a pagar a tus pagadores (tanto en escritorios como aplicaciones móviles).

```python
from khipu import Khipu
api = Khipu('receiver_id', 'secret_key')
data = {
    'subject': 'El asunto del cobro',
    'body': 'Descripción del cobro',
    'amount': '200',
    'payer_email': 'jrperdomoz@gmail.com',
    'bank_id': '',
    'expires_date': 'Formato Unix timestamp. Debe corresponder a una fecha en el futuro.',
    'transaction_id': 'T-1000',
    'custom': '',
    'notify_url': 'http://yourwebsite.cl/notificame/',
    'return_url': 'http://yourwebsite.cl/exito/',
    'cancel_url': '',
    'picture_url': ''
}
result = api.service('CreatePaymentURL', **data)
print result
>> {
    "id":"5wb665tyvm1p",
    "bill-id":"SSRwa",
    "url":"https://khipu.com/payment/show/5wb665tyvm1p",
    "manual-url":"https://khipu.com/payment/manual/5wb665tyvm1p",
    "mobile-url":"khipu:///pos/5wb665tyvm1p",
    "ready-for-terminal":false
  }
```
