# coding:utf-8
__author__ = 'xcma'
from src.controll.AboutTestcase import TestCase
from src.func.helper.log import log
log = log()
class getGwInfo(TestCase):

    def test_a_get_gwinfo(self):
        '''获取网关信息'''

        self.getInparam(self.getParam().get_gwinfo)
        self.udp_compare()
        self.assertEqual(self.res['status'], 200)
        data = self.res['result']['data']
        dns_server_list = data['dns_server']
        dialup = data['dialup']
        vlan_dict = data['vlan']
        rip = data['rip']
        self.assertTrue(self.misc().judge_legal_ip(rip))  # 校验ip是否合法
        rip_split_list = rip.split('.')
        for i in range(0,len(dns_server_list)):
            self.assertTrue(self.misc().judge_legal_ip(dns_server_list[i]))  # 校验ip是否合法
            if rip_split_list[0] in dns_server_list[0]:  # 校验网关172.16.16.1在跟第一个dns的第一个网段一致时，那么dns的第二位、第三位应该一致
                dns_split_list = dns_server_list[0].split('.')
                self.assertEqual(rip_split_list[1],dns_split_list[1])
                self.assertEqual(rip_split_list[2],dns_split_list[2])

        self.assertTrue(dns_server_list.count('114.114.114.114'))
        self.assertTrue(dns_server_list.count('8.8.8.8'))

        key = []
        value = []
        for k,v in vlan_dict.items():
            key.append(k)
            self.assertTrue(isinstance(v,list))
        self.assertIn('lan1',key)

        try:
            self.assertIn('wan1',key)
        except:
            self.assertIn('wan', key)

        try:
            self.assertTrue(data.has_key('itv1'))
        except:
            self.assertTrue(data.has_key('itv'))
        self.assertIn(dialup,[0,1,2,3])

