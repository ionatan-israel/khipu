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
k = Khipu('receiver_id', 'secret_key')
k.service('ReceiverStatus')
>> {u'type': u'production', u'ready_to_collect': True}
```

Pronto más funcionalidad!
