# coding:utf-8
__author__ = 'xcma'

from src.controll.AboutTestcase import TestCase
from src.func.helper.log import log
log = log()
class getUser(TestCase):



    def test_b_get_user(self):
        '''cmd错误'''
        self.udp(self.getParam().get_user_a)

    def test_c_get_user(self):
        '''umac参数格式错误|umac=E6DDDDW1'''
        self.udp(self.getParam().get_user_b)

    def test_d_get_user(self):
        '''umac参数类型错误"'''
        self.udp(self.getParam().get_user_c)


    def test_e_get_user(self):
        '''umac参数为空"'''
        self.udp(self.getParam().get_user_d)

