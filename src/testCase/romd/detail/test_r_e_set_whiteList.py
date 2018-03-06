# coding:utf-8
__author__ = 'xcma'

from src.controll.AboutTestcase import TestCase
from src.func.helper.log import log
log = log()
class whiteList(TestCase):
    def test_a_set_whiteList(self):
        '''cmd错误'''
        self.udp(self.getParam().set_whitelist_a)

    def test_b_set_whiteList(self):
        '''list参数为空'''
        self.udp(self.getParam().set_whitelist_b)

    def test_d_set_whiteList(self):
        '''多个重复参数值'''
        self.udp(self.getParam().set_whitelist_d)

    def test_e_set_whiteList(self):
        '''多个不同参数值'''
        self.udp(self.getParam().set_whitelist_e)

    def _f_set_whiteList1(self):
        '''list多个不同格式参数值'''
        self.udp(self.getParam().set_whitelist_e1)

    def test_f_set_whiteList(self):
        '''参数格式错误list=1'''
        self.udp(self.getParam().set_whitelist_f)

