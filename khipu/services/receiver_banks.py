# -*- coding: utf-8 -*-
from .common import KhipuService


class KhipuServiceReceiverBanks(KhipuService):

    def __init__(self, receiver_id, secret, service_name, **kwargs):
        super(
            KhipuServiceReceiverBanks, self).__init__(
                receiver_id, secret, service_name, **kwargs)
        self.data = {'receiver_id': receiver_id}
