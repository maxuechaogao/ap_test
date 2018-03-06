# coding:utf-8
__author__ = 'xcma'

from src.controll.AboutTestcase import TestCase
from src.func.helper.log import log
log = log()
class Getwifi(TestCase):

    def test_a_get_wifi(self):
        '''获取wifi配置'''
        self.udp(self.getParam().get_wifi)
        self.assertEqual(self.res['status'],200)
        data = self.res['result']['data']
        if data:
            for i in data:
                txpower = i['txpower']
                type = i['type']
                biisolation = i['biisolation']
                channel = i['channel']
                self.assertLessEqual(txpower,100)
                self.assertIn(type,[2,5])
                self.assertIn(biisolation,[0,1])
                self.assertLessEqual(channel,13)
                self.assertNotEqual(channel,0)
                ssidlist = i['ssidlist']
                for j in ssidlist:
                    enable = j['enable']
                    encrypt = j['encrypt']
                    isolation = j['isolation']
                    widx = j['widx']
                    self.assertIn(enable, [0,1])
                    self.assertIn(encrypt, [0,1])
                    self.assertIn(isolation, [0,1])
                    self.assertIn(widx, [0,1,2,3,4])

            log.debug('assert is ok')
        else:
            log.debug('data is null')

    def test_b_get_wifi(self):
        '''cmd错误'''
        self.udp(self.getParam().get_wifi_a)

    def test_c_get_wifi(self):
        '''参数错误'''
        self.udp(self.getParam().get_wifi_b,switch=False)
        self.assertEqual(self.res['status'],200)



