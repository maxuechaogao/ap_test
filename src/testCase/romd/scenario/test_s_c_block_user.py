# coding:utf-8
__author__ = 'xcma'

from src.controll.AboutTestcase import TestCase
from src.func.helper.log import log
log = log()
class BlockUser(TestCase):

    def test_a_block_user(self):
        '''禁止用户上网'''
        self.udp(self.getParam().block_user)

    def test_b_get_user(self):
        '''获取用户用网状态'''
        self.getInparam(self.getParam().get_user)
        self.rep_value(self.expect, 'usingstate', 3)
        self.udp_compare()

    def test_c_get_all_user(self):
        '''获取全部用户用网状态'''
        self.udp(self.getParam().get_all_user)
        data = self.res['result']['data']
        umac_list = []
        for i in data:
            umac_ = i['umac']
            usingstate = i['usingstate']
            umac_list.append(umac_)
            umac_list.append(usingstate)
        for i in range(0, len(umac_list)):
            if self.umac == umac_list[i]:
                self.assertEqual(umac_list[i + 1], 1)