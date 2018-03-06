# coding:utf-8
__author__ = 'xcma'

from src.controll.AboutTestcase import TestCase
from src.func.helper.log import log
log = log()

class ack(TestCase):

    """
    协商失败后，请求其他接口无响应
    """
    def test_a_ack(self):
        '''ifversion=v2协商失败，此时其他接口请求应该无响应'''
        self.udp(self.getParam().syn)
        self.udp(self.getParam().ack_c)

    def test_b_ack(self):
        '''查看get_gwinfo接口'''
        try:
            self.udp(self.getParam().get_gwinfo,switch=False)
        except BaseException as msg:
            if 'timeout' in msg:
                pass
            else:
                raise msg
