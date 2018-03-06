#coding:utf-8
import json

__author__ = 'xcma'
import socket

from src.func.helper.log import log
from src.func.helper.misc import Misc
from src.func.readConfig import getconfig

log=log()

class udp_client:

    def __init__(self):
        self.addr = getconfig('config')['udp']['addr']
        self.port = getconfig('config')['udp']['port']
        self._conn()

    def _conn(self):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            self.address = (self.addr, self.port)
            self.client_socket.settimeout(30)
            log.debug('_conn succ:{}'.format(self.address))
        except:
            log.error('_conn fail')

    def recv(self):
        self.receive_data, self.sender_address = self.client_socket.recvfrom(2048)
        try:
            res = Misc.strtojson(self.receive_data)
            log.debug("recv data: {}".format(res))
            if not isinstance(res,dict):
                log.error('res is not dict:500')
            return res
        except BaseException as msg:
            log.error('recv data:{}'.format(self.receive_data))
            raise msg
        except:
            msg = 'recv timeout'
            log.error(msg)

    def send(self,send_data):
        send_data = Misc.jsonToStr(send_data)
        try:
            log.debug("send data：{}".format(send_data))
            # 发送成功响应值是发送数据的长度
            send_len = self.client_socket.sendto(send_data, self.address)
            # res = self.client_socket.sendto('sdfasfd', ('172.16.16.1',2048))
            log.debug('send succ [len:{}]'.format(send_len))
            return send_len
        except:
            log.error('send error')
            return 0
