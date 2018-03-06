# coding:utf-8
__author__ = 'xcma'

from src.controll.AboutTestcase import TestCase
from src.func.helper.log import log
log = log()
class pass_user(TestCase):
    """
       测试这里的时候要使用真实的mac地址，比如本机的mac地址，将全局mac开关打开
    """
    def test_a_pass_user(self):
        '''放行用户A上网|放行指定终端mac'''
        self.udp(self.getParam().pass_user)

    def test_b_get_user(self):
        '''获取用户A用网状态|获取指定在线用户用网策略'''
        self.getInparam(self.getParam().get_user)
        self.rep_value(self.expect,'usingstate',1)
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
        for i in range(0,len(umac_list)):
            if self.umac== umac_list[i]:
                self.assertEqual(umac_list[i+1],1)

