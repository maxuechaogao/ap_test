# coding:utf-8
__author__ = 'xcma'

from src.controll.AboutTestcase import TestCase
from src.func.helper.log import log
log = log()

class syn(TestCase):

    def test_a_syn(self):
        '''cmd错误'''

        self.udp(self.getParam().syn_a)

    def test_c_syn(self):
        '''参数ifversionlist值类型错误'''
        self.udp(self.getParam().syn_c)

    def test_d_syn(self):
        '''参数ifversionlist=['v10']值错误'''
        self.udp(self.getParam().syn_d)

    def test_e_syn(self):
        '''参数ifversionlist=['v1','v2','v10']'''
        self.udp(self.getParam().syn_e,switch=False)
        self.assertEqual(self.res['status'], 200)
        self.assertEqual(self.res['params']['code'], 0)
        wifi_mac = self.res['params']['wifi_mac']
        lan_mac = self.res['params']['lan_mac']
        wan_mac = self.res['params']['wan_mac']
        dev_name= self.res['params']['dev_name']
        ifversion= self.res['params']['ifversion']
        release_date= self.res['params']['release_date']
        oemcode= self.res['params']['oemcode']
        sn= self.res['params']['sn']
        hw_ver= self.res['params']['hw_ver']
        dev_model= self.res['params']['dev_model']
        self.assertTrue(self.misc().isValidMac(wifi_mac))
        self.assertTrue(self.misc().isValidMac(lan_mac))
        self.assertTrue(self.misc().isValidMac(wan_mac))
        self.assertTrue(isinstance(dev_name, str))
        self.assertTrue(isinstance(ifversion, str))
        self.assertTrue(isinstance(release_date, str))
        self.assertTrue(isinstance(oemcode, str))
        self.assertTrue(isinstance(sn, str))
        self.assertTrue(isinstance(hw_ver, str))
        self.assertTrue(isinstance(dev_model, str))






