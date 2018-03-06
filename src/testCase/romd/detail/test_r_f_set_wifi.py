# coding:utf-8
__author__ = 'xcma'

from src.controll.AboutTestcase import TestCase
from src.func.helper.log import log
log = log()
class Setwifi(TestCase):

    def test_a_set_whitelist(self):
        '''cmd错误'''
        self.udp(self.getParam().set_wifi_a)

    def test_b_set_whitelist(self):
        '''参数type=1值错误'''
        self.udp(self.getParam().set_wifi_b)

    def test_c_set_whitelist(self):
        '''单频参数type=5'''
        self.udp(self.getParam().set_wifi_c)

    def test_d_set_whitelist(self):
        '''参数enable类型错误'''
        self.udp(self.getParam().set_wifi_d)
        self.assertEqual(self.res['status'], 400)
        self.assertIn(self.res['result']['code'], [5005,5006])

    def test_e_set_whitelist(self):
        '''参数ssid=1类型错误'''
        self.udp(self.getParam().set_wifi_e)
        self.assertEqual(self.res['status'], 400)
        self.assertIn(self.res['result']['code'], [5005,5006])

    def test_f_set_whitelist(self):
        '''设置2个ssid'''
        self.udp(self.getParam().set_wifi_f)
