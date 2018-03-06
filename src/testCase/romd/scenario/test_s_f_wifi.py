# coding:utf-8
__author__ = 'xcma'

from src.controll.AboutTestcase import TestCase
from src.func.helper.log import log
log = log()
class wifi(TestCase):

    def test_a_set_wifi(self):
        '''设置WiFi'''
        self.getInparam(self.getParam().set_wifi)
        self.txpower = self.misc().generate_id(99)
        self.in_param['params']['data'][0]['txpower'] = self.txpower
        self.udp_compare()

    def test_b_get_wifi(self):
        '''获取wifi'''
        self.getInparam(self.getParam().set_wifi)
        self.channel = self.in_param['params']['data'][0]['channel']
        self.biisolation = self.in_param['params']['data'][0]['biisolation']
        self.txpower = self.in_param['params']['data'][0]['txpower']
        self.type = self.in_param['params']['data'][0]['type']
        self.in_ssidlist = self.in_param['params']['data'][0]['ssidlist']

        enable_list = []
        encrypt_list = []
        ssid_list = []
        isolation_list = []
        key_list = []
        widx_list = []
        for i in self.in_ssidlist:
            enable = i['enable']
            enable_list.append(enable)
            encrypt = i['encrypt']
            encrypt_list.append(encrypt)
            ssid = i['ssid']
            ssid_list.append(ssid)
            isolation = i['isolation']
            isolation_list.append(isolation)
            key = i['key']
            key_list.append(key)
            widx = i['widx']
            widx_list.append(widx)

        self.udp(self.getParam().get_wifi)
        self.assertEqual(self.res['status'], 200)
        afchannel = self.res['result']['data'][0]['channel']
        aftxpower = self.res['result']['data'][0]['txpower']
        afbiisolation = self.res['result']['data'][0]['biisolation']
        aftype = self.res['result']['data'][0]['type']
        self.assertEqual(self.channel,afchannel)
        self.assertEqual(self.biisolation,afbiisolation)
        self.assertEqual(self.txpower,aftxpower)
        self.assertEqual(self.type,aftype)

        self.out_ssidList = self.res['result']['data'][0]['ssidlist']
        for j in range(0,len(self.in_ssidlist)):
            enable = self.out_ssidList[j]['enable']
            self.assertEqual(enable,enable_list[j])
            encrypt = self.out_ssidList[j]['encrypt']
            self.assertEqual(encrypt,encrypt_list[j])
            ssid = self.out_ssidList[j]['ssid']
            self.assertEqual(ssid,ssid_list[j])
            isolation = self.out_ssidList[j]['isolation']
            self.assertEqual(isolation,isolation_list[j])
            key = self.out_ssidList[j]['key']
            if encrypt !=0:
                self.assertEqual(key,key_list[j])
            widx = self.out_ssidList[j]['widx']
            self.assertEqual(widx,widx_list[j])

