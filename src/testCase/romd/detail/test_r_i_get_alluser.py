# coding:utf-8
__author__ = 'xcma'

from src.controll.AboutTestcase import TestCase
from src.func.helper.log import log
log = log()
class Heart(TestCase):


    def test_a_get_user(self):
        '''获取用户信息'''
        self.udp(self.getParam().get_all_user)
        self.assertEqual(self.res['status'], 200)
        self.assertEqual(self.res['id'], self.in_param['id'])
        data = self.res['result']['data']
        if data:
            for i in data:
                umac = i['umac']
                self.assertEqual(len(umac),12)
                self.assertNotIn(umac,'000000000000')
                self.assertTrue(self.misc().isValidMac(umac))  # 校验mac是否合法

                onway = i['onway'] # 连接路由器方式：wlan：1  lan口：2
                usingstate = i['usingstate'] # 连接路由器方式：wlan：1  lan口：2
                uip = i['uip']
                self.assertTrue(self.misc().judge_legal_ip(uip))  # 校验ip是否合法
                self.assertIn(onway,[1,2])
                self.assertIn(usingstate,[1,2,3])
                if onway==1:
                    widx = i['widx']  # ssid
                    self.assertIn(widx,[0,1,2,3,4])
                log.debug('assert ok')
        else:
            log.debug('data is null')

    def test_b_get_all_user(self):
        '''cmd错误'''
        self.udp(self.getParam().get_all_user_a)

    def test_c_get_all_user(self):
        '''参数错误'''
        self.udp(self.getParam().get_all_user_b,switch=False)
        self.assertEqual(self.res['status'],200)
