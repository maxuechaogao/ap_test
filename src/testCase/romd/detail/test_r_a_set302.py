# coding:utf-8
__author__ = 'xcma'

from src.controll.AboutTestcase import TestCase
from src.func.helper.log import log
log = log()
class set302(TestCase):


    def test_a_main_process(self):
        '''设置302'''
        self.udp(self.getParam().set302)


    def _b_main_process(self):
        '''s302url报文cmd错误'''
        self.udp(self.getParam().set302_a)

    def _c_main_process(self):
        '''s302url=1类型错误'''
        self.udp(self.getParam().set302_b)

    def test_d_main_process(self):
        '''s302url值为空'''

        self.udp(self.getParam().set302_d)

    def test_e_main_process(self):
        '''s302url值格式错误'''
        self.udp(self.getParam().set302_c)

    def test_f_main_process(self):
        '''s302url_json格式错误'''
        self.udp(self.getParam().set302_e)


