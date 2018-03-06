# coding:utf-8
import time
import types

__author__ = 'xcma'

import unittest
from src.controll.udp_client import *
from src.conf.romd import param
from src.func.helper.misc import Misc
from src.func.helper.dicthelper import ditchelper
# 引入入参模板
udp_client = udp_client()
dh = ditchelper()
class TestCase(unittest.TestCase):
    umac = ''
    txpower =  ''
    expect = {}
    in_param = {}
    res = {}
    path = []
    ssid = ''
    casename = ''
    def setUp(self):
        log.debug('用例开始')
        conf_value = getconfig('config')
        always_syn = conf_value['base']['always_syn']
        self.start = self.misc().getTimeStamp()
        if always_syn:
            self.udp(self.getParam().syn)
            self.getInparam(self.getParam().ack)
            self.udp_only_send()

    def getInparam(self, new_parm):
        """拿入参"""
        self.case_name = ''
        try:
            conf_value = getconfig('config')
            umac_enable = conf_value['base']['umac_enable']
            uip_enable = conf_value['base']['uip_enable']
            if new_parm:
                in_param_up =new_parm
                if isinstance(in_param_up, dict):
                    info = in_param_up['info']
                    self.case_name = info['casename']
                    for key, value in info.items():
                        log.debug('{}:{}'.format(key,value))
                    self.in_param = in_param_up['param']
                    try:
                        self.expect = in_param_up['expect']
                    except:
                        pass
                    try:
                        umac = conf_value['base']['umac']
                    except:
                        umac = 'not found'
                    if self.dict_has_key(self.in_param,'umac') and umac_enable:
                        self.rep_value(self.in_param, 'umac', umac)

                    if self.expect and self.dict_has_key(self.expect,'umac') and umac_enable:
                        self.rep_value(self.expect,'umac',umac)
                    try:
                        uip = conf_value['base']['uip']
                    except:
                        uip = 'not found'
                    if self.dict_has_key(self.in_param,'uip') and uip_enable:
                        self.rep_value(self.in_param,'uip',uip)

                    if self.expect and self.dict_has_key(self.expect,'uip') and uip_enable:
                        self.rep_value(self.expect,'uip',uip)
                    id = Misc.generate_id()
                    if self.dict_has_key(self.in_param,'id'):
                        self.rep_value( self.in_param,'id',id)
                    if self.expect and self.dict_has_key(self.expect,'id'):
                        self.rep_value(self.expect, 'id', id)

                    return {'in_param':self.in_param,'expect':self.expect}
        except BaseException as msg:
            log.error(msg)

    def compareDict(self,a='',b=''):
        """
        比较a,b之间的差异
        :param parm_temp:
        :param new_parm:
        :return:
        """
        if not a or not b:
            a = self.res
            b = self.expect
        if isinstance(a, dict) and isinstance(b, dict):
            for x in range(len(a)):
                temp_key = a.keys()[x]
                temp_value = a[temp_key]
                if isinstance(b, dict) and temp_value:
                    if b.has_key(temp_key):
                        bv = b[temp_key]
                        if isinstance(temp_value,dict) and isinstance(bv,dict):
                            if self.dict_has_key(temp_value,'msg') and self.dict_has_key(bv,'msg'):
                                self.rep_value(temp_value,'msg','')
                                self.rep_value(bv,'msg','')
                            self.assertDictEqual(temp_value,bv)

                        elif isinstance(temp_value,list) and isinstance(bv,list):
                            self.assertListEqual(temp_value,bv)
                        else:
                            self.assertEqual(temp_value,bv)
        else:
            log.error('{{} or {}} is not set'.format(b,a))

    def sleep(self,num):
        time.sleep(num)

    def misc(self):
        return Misc

    def getParam(self):
        return param

    def udp_recv(self):
        return udp_client.recv()

    def rep_value(self,dic,key,value):
        return dh.replace_value(dic,key,value)

    def dict_has_key(self,dic,key):
        """
        判断是否包含这个key
        :param dic:
        :param key:
        :param value:
        :return:
        """
        result = dh.dict_get(dic,key)[0]
        return result

    def udp(self, in_param, data='', switch=True):
        """
        组合方法，拿到入参，直接发送请求
        :param new_parm:
        :param data : 如果data有值，则new_parm 不生效
        :return:
        """
        self.getInparam(in_param)
        self.udp_compare(data=data,switch=switch)
        return self.res

    def udp_send(self,data):
        """
        发送入参，并拿到响应值
        :param data:
        :return:
        """
        times = 1
        goon = True
        conf_value = getconfig('config')
        recv_num = int(conf_value['base']['recv_num'])
        if isinstance(data,dict) and data.has_key('id'):
            id = data['id']
            if isinstance(id,int):
                while times<=recv_num and goon and id:
                    times +=1
                    udp_client.send(data)
                    self.res = udp_client.recv()
                    if isinstance(self.res, dict) and self.res.has_key('id'):
                        if self.res['id']==id:
                            goon = False
                    else:
                        log.warning('res is not dict or no id')
                if times==recv_num:
                    self.assertEqual(self.res['id'],id)
            else:
                msg = 'id type is not int'
                log.error(msg)
                raise msg
        else:
            udp_client.send(data)
            self.res = udp_client.recv()
        return self.res

    def udp_compare(self, data='',switch=True):
        """
        组合方法，拿到响应值后，进行比较响应值与期望值
        :param data:
        :return:
        """

        try:
            if not data:
                data = self.in_param

            try:
                self.udp_send(data)
            except BaseException as msg:
                log.error(msg)
                raise msg
            finally:
                log.debug('expect:{}'.format(self.expect))
            if self.expect and switch:
                self.compareDict()
            return self.res
        except BaseException as msg:
            raise msg

    def udp_only_send(self,data=''):
        if not data:
            data = self.in_param
        return udp_client.send(data)

    def tearDown(self):
        log.debug('tearDown')
        self.end = self.misc().getTimeStamp()
        re = self.misc().getTime(self.start, self.end)
        log.debug('{}，耗时：{}ms'.format(self.case_name,re))