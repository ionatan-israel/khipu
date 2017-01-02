# -*- coding: utf-8 -*-
from .common import KhipuService


class KhipuServiceReceiverStatus(KhipuService):

    def __init__(self, receiver_id, secret, service_name, **kwargs):
        super(
            KhipuServiceReceiverStatus, self).__init__(
                receiver_id, secret, service_name, **kwargs)
        self.data = {'receiver_id': receiver_id}
