# coding:utf-8
__author__ = 'xcma'

from src.controll.AboutTestcase import TestCase
from src.func.helper.log import log
log = log()
class whiteList(TestCase):
    def test_a_set_whitelist(self):
        '''设置白名单'''
        self.udp(self.getParam().set_whitelist)

    def test_b_get_whitelist(self):
        '''获取白名单'''
        self.getInparam(self.getParam().get_whitelist)
        self.rep_value(self.expect, 'list', ['test.com'])
        self.udp_compare()

    def test_c_add_whitelist(self):
        '''增加白名单'''
        self.udp(self.getParam().add_whitelist)

    def test_d_get_whitelist(self):
        '''获取白名单'''
        self.getInparam(self.getParam().get_whitelist)
        self.rep_value(self.expect, 'list', ['test.com','3g.163.com'])
        self.udp_compare()

    def test_e_add_whitelist(self):
        '''增加已存在白名单的url'''
        self.udp(self.getParam().add_whitelist)

    def test_f_get_whitelist(self):
        '''获取白名单'''
        self.getInparam(self.getParam().get_whitelist)
        self.rep_value(self.expect, 'list', ['test.com','3g.163.com'])
        self.udp_compare()
