# coding:utf-8
__author__ = 'xcma'

from src.controll.AboutTestcase import TestCase
from src.func.helper.log import log
log = log()
class Heart(TestCase):


    def test_a_main_process(self):
        '''设置302'''
        self.udp(self.getParam().set302)



