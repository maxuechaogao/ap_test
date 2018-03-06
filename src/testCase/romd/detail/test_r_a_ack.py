# coding:utf-8
__author__ = 'xcma'

from src.controll.AboutTestcase import TestCase
from src.func.helper.log import log
log = log()

class ack(TestCase):

    """
    暂时不做校验
    """

    def test_c_ack(self):
        '''ifversion=v2协商失败，此时其他接口请求应该无响应'''

        self.udp(self.getParam().syn)
        self.udp_only_send(self.getParam().ack_c)


