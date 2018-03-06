# coding:utf-8
__author__ = 'xcma'

from src.controll.AboutTestcase import TestCase
from src.func.helper.log import log
log = log()
class whiteList(TestCase):

    def test_a_add_whiteList(self):
        '''cmd错误'''
        self.udp(self.getParam().add_whitelist_a)
    def test_b_add_whiteList(self):
        '''参数为空| list=[""]'''
        self.udp(self.getParam().add_whitelist_b)

    def test_d_add_whiteList(self):
        '''list多个重复参数值'''
        self.udp(self.getParam().add_whitelist_d)

    def test_e_add_whiteList(self):
        '''list多个不同参数值'''
        self.udp(self.getParam().add_whitelist_e)

    def test_e_add_whiteList1(self):
        '''list多个不同格式参数值'''
        self.udp(self.getParam().add_whitelist_e1)

    def test_f_add_whiteList(self):
        '''list参数类型错误'''
        self.udp(self.getParam().add_whitelist_f)




