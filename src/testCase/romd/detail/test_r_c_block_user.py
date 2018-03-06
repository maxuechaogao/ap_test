# coding:utf-8
__author__ = 'xcma'

from src.controll.AboutTestcase import TestCase
from src.func.helper.log import log
log = log()
class BlockUser(TestCase):


    def test_a_block_user(self):
        '''umac为空，uip错误'''
        self.udp(self.getParam().block_user_a)

    def test_b_block_user(self):
        '''uip为空，umac错误'''
        self.udp(self.getParam().block_user_b)

    def test_c_block_user(self):
        '''参数为空'''
        self.udp(self.getParam().block_user_c)

    def test_d_block_user(self):
        '''cmd错误'''
        self.udp(self.getParam().block_user_d)

    def test_e_block_user(self):
        '''umac类型错误'''
        self.udp(self.getParam().block_user_e)

    def test_f_block_user(self):
        '''umac格式错误'''
        self.udp(self.getParam().block_user_f)

    def test_g_block_user(self):
        '''uip格式错误'''
        self.udp(self.getParam().block_user_g)


