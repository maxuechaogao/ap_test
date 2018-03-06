# coding:utf-8
__author__ = 'xcma'
import socket

from src.func.helper.log import log

log =log()

class udp_server:

    def __init__(self):

        self.PORT = 9002
        self._conn()

    def _conn(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        address = ("127.0.0.1", self.PORT)
        self.server_socket.bind(address)

    def recv(self):
        self.receive_data, self.client_address = self.server_socket.recvfrom(1024)
        log.debug("接收到了客户端 %s 传来的数据: %s" % (self.client_address, self.receive_data.decode()))
        return self.receive_data

    def send(self,send_data):
        log.debug('send_data:{}'.format(send_data))
        self.server_socket.sendto(self.receive_data, self.client_address)


