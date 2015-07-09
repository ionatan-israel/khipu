# -*- coding: utf-8 -*-
import requests

from common import KhipuService


class KhipuServiceReceiverStatus(KhipuService):
    
    def data_to_string(self):
        return "receiver_id=" + self.receiver_id

    def request(self):
        self.data['receiver_id'] = self.receiver_id
        self.data['hash'] = self.do_hash(self.data_to_string())
        return requests.post(self.get_url_service(), self.data).json()
