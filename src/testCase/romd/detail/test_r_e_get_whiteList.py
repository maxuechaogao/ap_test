# coding:utf-8
__author__ = 'xcma'

from src.controll.AboutTestcase import TestCase
from src.func.helper.log import log
log = log()
class getwhiteList(TestCase):

    def test_b_add_whitelist(self):
        '''cmd错误'''
        self.udp(self.getParam().get_whitelist_a)

    def test_c_add_whitelist(self):
        '''参数错误'''
        self.udp(self.getParam().get_whitelist_b,switch=False)
        self.assertEqual(self.res['status'],200)

