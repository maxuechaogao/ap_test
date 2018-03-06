# coding:utf-8
__author__ = 'xcma'

from src.controll.AboutTestcase import TestCase
from src.func.helper.log import log
log = log()
class Heart(TestCase):


    def test_a_jump_user(self):
        '''umac为空，uip错误'''

        self.udp(self.getParam().jump_user_a)


    def test_b_jump_user(self):
        '''uip为空，umac无效'''
        self.udp(self.getParam().jump_user_b)


    def test_c_jump_user(self):
        '''控制用户跳转|参数为空'''
        self.udp(self.getParam().jump_user_c)


    def test_d_jump_user(self):
        '''控制用户跳转|cmd错误'''
        self.udp(self.getParam().jump_user_d)


    def test_e_jump_user(self):
        '''umac类型错误'''
        self.udp(self.getParam().jump_user_e)


    def test_f_jump_user(self):
        '''umac格式错误'''
        self.udp(self.getParam().jump_user_f)


    def test_h_jump_user(self):
        '''uip类型错误'''
        self.udp(self.getParam().jump_user_g1)
