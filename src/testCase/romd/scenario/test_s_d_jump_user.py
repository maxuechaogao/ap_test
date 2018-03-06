# coding:utf-8
__author__ = 'xcma'

from src.controll.AboutTestcase import TestCase
from src.func.helper.log import log
log = log()
class JumpUser(TestCase):
    def test_a_jump_user(self):
        '''跳转'''
        self.udp(self.getParam().jump_user)

    def test_b_get_user(self):
        '''获取用户用网状态'''
        self.getInparam(self.getParam().get_user)
        self.rep_value(self.expect, 'usingstate', 2)
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