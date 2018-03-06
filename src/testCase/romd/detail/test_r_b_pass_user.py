# coding:utf-8
__author__ = 'xcma'

from src.controll.AboutTestcase import TestCase
from src.func.helper.log import log
log = log()
class pass_user(TestCase):


    def test_b_pass_user(self):
        '''设置参数为空'''

        self.udp(self.getParam().pass_user_b)

    def test_c_pass_user(self):
        '''设置cmd为错误值'''
        self.udp(self.getParam().pass_user_c)

    def test_d_pass_user(self):
        '''设置uip为空，umac错误'''
        self.udp(self.getParam().pass_user_d)

    def test_e_pass_user(self):
        '''#umac类型错误'''
        self.udp(self.getParam().pass_user_e)

    def test_e_pass_user1(self):
        '''umac类型错误1232131'''
        self.udp(self.getParam().pass_user_e1)

    def test_e_pass_user2(self):
        '''umac类型错误12321312345611'''
        self.udp(self.getParam().pass_user_e2)

    def test_f_pass_user(self):
        '''umac格式错误'''
        self.udp(self.getParam().pass_user_f)

    def test_g_pass_user(self):
        '''uip格式错误'''
        self.udp(self.getParam().pass_user_g)

    def test_g_pass_user1(self):
        '''uip格式错误"uip": "192.168.1.288"'''
        self.udp(self.getParam().pass_user_g1)

    def test_h_pass_user(self):
        '''uip类型错误'''
        self.udp(self.getParam().pass_user_g2)



