# coding=utf-8
import re
import types

__author__ = 'xcma'
import base64
import datetime
import json
import os
import random
import shutil
import sys
import time

import requests

from src.func.helper.log import log
from src.func.readConfig import getconfig

log = log()

def ABSpath():
    """获取当前的绝对路径"""
    ABSPATH = os.path.abspath(sys.argv[0])
    ABSPATH = os.path.dirname(ABSPATH)
    return ABSPATH

Config_value = getconfig('config')

class Misc:
    path = []

    def __getCurrentFilePath(cls, is_path='no'):
        """
        返回当前文件的名称、文件名及路径
        :param is_path:
        :return:
        """
        if is_path == 'no':
            return os.path.basename(__file__)
        else:
            return os.path.realpath(sys.argv[0])

    @classmethod
    def _updateDict(cls, parm_temp, new_parm):
        """
        更新字典
        :param parm_temp: 模板字典
        :param new_parm: 更新模板字典
        :return:
        """
        data = parm_temp
        if isinstance(data, dict):
            for x in range(len(data)):
                temp_key = data.keys()[x]
                temp_value = data[temp_key]
                if isinstance(new_parm, dict):
                    for y in range(len(new_parm)):
                        temp_key_b = new_parm.keys()[y]
                        temp_value_b = new_parm[temp_key_b]

                        if not isinstance(temp_value, (list, dict)) and not isinstance(temp_value_b,
                                                                                       (list, dict)) or not temp_value:
                            if temp_key == temp_key_b:
                                data[temp_key] = new_parm[temp_key_b]
                        Misc._updateDict(temp_value, temp_value_b)

        return data

    @classmethod
    def base64_encode(cls,str):
        """
        编码为base64
        :param str:
        :return:
        """
        return base64.encodestring(str)

    @classmethod
    def base64_decode(cls,str):
        """
        base64解码
        :param str:
        :return:
        """
        return base64.decodestring(str)
    @classmethod
    def ABSpath(cls):
        """获取当前的绝对路径"""
        ABSPATH = os.path.abspath(sys.argv[0])
        ABSPATH = os.path.dirname(ABSPATH)
        return ABSPATH

    @classmethod
    def setSleep(cls, seconds):
        """
        休眠指定seconds
        :param seconds:
        :return:
        """
        return time.sleep(seconds)

    @classmethod
    def getTimeNow(cls):
        """
        返回当前时间，日期格式：2016-12-12 18:07:30.124847
        :return:
        """
        return datetime.datetime.now()

    @classmethod
    def getTimeStamp(cls):
        """
        返回当前系统时间的毫秒级时间戳
        :return: 1498809121.94005
        """
        t = int(round(time.time() * 1000))
        return t

    @classmethod
    def getTime_format(cls):
        """
        格式化时间
        :return:  2017-08-22 20:30:23
        """
        return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    @classmethod
    def getTimeStamp_now(cls):
        """
        返回当前系统时间的时间戳,并且取整
        :return: 1498809121
        """
        return time.mktime(datetime.datetime.now().timetuple())
    @classmethod
    def getDateRelativeNow(cls,n):
        """
        返回当前日期：2016-12-12 加|减  n天
        :return: 
        """
        now_time = datetime.datetime.now()
        sum_time = now_time + datetime.timedelta(days=n)
        sum_time_format = sum_time.strftime('%Y-%m-%d')
        return sum_time_format

    @classmethod
    def getTime(cls, start=0, end=0):
        """
        计算2次时间戳只差
        :param start:
        :param end:
        :return:
        """
        t = end-start
        # l = '%.4f' % t
        # l = Misc.getFormatTime(t)
        return t

    @classmethod
    def compareTime(cls, first, second):
        """
        比较时间大小，
        :param second:入参格式为：'2017-08-22 20:30:23'
        :return:
        """

        try:
            result = time.mktime(time.strptime(first, '%Y-%m-%d %H:%M:%S')) - time.mktime(
                time.strptime(second, '%Y-%m-%d %H:%M:%S'))
            if float(result) > 0:
                result = True
            else:
                result = False
            return result
        except BaseException:
            msg = '入参错误'
            log.error(msg)

    @classmethod
    def getFormatTime(cls,timestamp):
        """
        时间戳转换成时间
        :return:
        """
        # 转换成localtime
        time_local = time.localtime(timestamp)
        # 转换成新的时间格式(2016-05-05 20:28:54)
        dt = time.strftime("%S:", time_local)
        return dt

    @classmethod
    def del_file(cls, dir, filename):
        """
        删除指定目录dir中与filename不同的文件
        :param dir:
        :param filename:
        :return:
        """
        cls.dir = str(dir)
        try:
            if os.listdir(dir):
                for file in os.listdir(cls.dir):
                    if file != filename:
                        os.remove(cls.dir + file)
                log.debug('del_file => ok')
        except Exception as msg:
            log.error('del_file => error')
            raise msg

    @classmethod
    def del_file_specific(cls, dir, filename):
        '''

        删除与参数相同的文件
        '''
        cls.dir = str(dir)
        for file in os.listdir(cls.dir):

            if file == filename:
                os.remove(cls.dir + file)
            else:
                continue

    @classmethod
    def del_file_the_earliest(cls, dir, maxFileNum):
        """
        当删除指定目录dir中文件总数>500,删除最早的一个文件
        :param dir:
        :param filename:
        :return:
        """
        log.debug(dir)

        cls.dir = str(dir)
        if not os.listdir(dir):
            log.debug(u'目录中没有文件')

        while len(os.listdir(dir)) > int(maxFileNum):
            try:
                lists = os.listdir(dir)
                lists.sort(key=lambda fn: os.path.getmtime(dir + '/' + fn))
                file_old0 = os.path.join(lists[0])
                file_old1 = os.path.join(lists[1])
                # 返回最早生成的文件名称
                log.debug('remove report file：%s' % file_old0)
                log.debug('remove report file：%s' % file_old1)
                os.remove(cls.dir + file_old0)
                os.remove(cls.dir + file_old1)
            except Exception as msg:
                log.error(msg)
                raise msg



    @classmethod
    def new_report_nopath(cls, reportpath):
        '''
        对test_report目录中文件进行排序，返回最新生成的html文件
        '''

        lists = os.listdir(reportpath)
        lists.sort(key=lambda fn: os.path.getmtime(reportpath + '/' + fn))

        if lists[-1] == ".DS_Store":
            file_new = os.path.join(lists[-2])
        else:
            file_new = os.path.join(lists[-1])
        return file_new

    @classmethod
    def new_report_path(cls, reportpath):
        '''
        对test_report目录中文件进行排序，返回最新生成的html文件
        '''

        lists = os.listdir(reportpath)
        lists.sort(key=lambda fn: os.path.getmtime(reportpath + '/' + fn))
        if lists[-1] == ".DS_Store":
            file_new = reportpath + os.path.join(lists[-2])
        else:
            file_new = reportpath + os.path.join(lists[-1])
        return file_new

    @classmethod
    def move_file(cls, oldpath, newpath):
        '''
        移动文件到目标路径
        '''
        try:

            shutil.move(oldpath, newpath)
        except BaseException as msg:
            print (msg)

    @classmethod
    def move_screenshot(cls, tarpath="Fail||Pass"):
        """
        移动截图到指定dirname目录中
        :return:tarpath = Fail||Pass
        """
        try:
            dirname = datetime.datetime.now().strftime("%Y%m%d.%H%M%S.%f")[:-3]
            old_path = Misc.ABSpath() + "/Output/Screenshot/" + tarpath + "/"
            path = Misc.ABSpath() + "/Output/Screenshot/"
            new_path_screen = path + dirname
            for root, dirs, files in os.walk(old_path):
                if len(files) != 0:
                    Misc.mkdir(old_path, new_path_screen)
                    log.debug(u'创建新路径')
                else:
                    log.debug(u'当前目录无文件，不创建新目录')
                if len(dirs) == 0:
                    for i in range(len(files)):
                        log.debug(u'查找file')
                        if files[i][-3:] == 'png':
                            log.debug(u'查找.png图片')
                            old_path_file = old_path + "/" + files[i]
                            new_path_screen_file = new_path_screen + "/" + files[i]
                            shutil.move(old_path_file, new_path_screen_file)
                            log.debug(u'执行移动')
                        else:
                            log.debug(u'当前路径无.png图片')
            log.debug(u'移动截图成功')
        except Exception as msg:
            log.error(u'移动截图失败')
            print msg
            raise

    @classmethod
    def mkdir(cls, path='../Output/', name=None):
        """
        路径中存在name,则do nothing;
        路径中不存在name,则新建name;
        :param path:
        :param name:
        :return:
        """
        try:

            new_dirname = name
            new_path = os.path.join(path, new_dirname)
            if not os.path.isdir(new_path):
                os.makedirs(new_path)
        except Exception as msg:
            print msg
            raise

    @classmethod
    def copy_file(cls, filepath, newpath):
        """
        复制指定文件到目标目录;
        :param filepath:
        :param newpath:
        :return:
        """
        try:
            shutil.copy(filepath, newpath)
            log.debug(u'copy=>ok')
        except BaseException as msg:
            print msg


    @classmethod
    def generate_phone(cls):
        """
        生成随机手机号
        :return:
        """
        phone = random.choice(['139', '188', '185', '136', '158', '151'])+"".join(random.choice("0123456789")
        for i in range(8))
        return phone

    @classmethod
    def generate_id(cls,max_num=1000):
        """
        生成随机数0-1000之间
        :return:
        """
        return random.randint(0, max_num)


    @classmethod
    def inter_validation(cls, r=None, phone=None, url=None):
        """
        验证接口返回值是否为1
        :param r:
        :param phone:
        :param url:
        :return:
        """
        u'a07接口,返回值为1,则代表该手机号为老用户;此时重新生成手机号,直到接口返回值为:0'
        parameter = {"r": r, "phone": phone, "user_type": "1"}
        r = requests.get(url, params=parameter)
        q = r.json()
        p = json.dumps(q, sort_keys=True)
        if p[-3] == '1':
            return False
        else:
            return True

    @classmethod
    def jsonToStr(cls,data):
        """
        将json、dict转换为utf8格式字符串
        :param data:
        :return:
        """
        return json.dumps(data, encoding="UTF-8", ensure_ascii=False)

    @classmethod
    def strtojson(cls,data,encode='gb2312'):
        if not isinstance(data,str):
            data = str(data)
        try:
            data = json.dumps(data)
            res = json.loads(data,encoding=encode)
        except:
            res = json.loads(data,encoding=encode)
        try:
            return eval(res)
        except:
            return res

    @classmethod
    def judge_legal_ip(cls, one_str):
        '''
        正则匹配方法
        判断一个字符串是否是合法IP地址
        '''
        compile_ip = re.compile('^((25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(25[0-5]|2[0-4]\d|[01]?\d\d?)$')
        if compile_ip.match(one_str):
            return True
        else:
            return False

    @classmethod
    def isValidMac(cls,mac):
        """
        正则匹配方法校验mac地址是否合法
        :param mac:
        :return:
        """
        if re.match(r"^\s*([0-9a-fA-F]{2,2}){5,5}[0-9a-fA-F]{2,2}\s*$", mac): return True
        return False
    @classmethod
    def compareDict(self,a='',b=''):
        """
        更新字典
        :param parm_temp: 模板字典
        :param new_parm: 更新模板字典
        :return:
        """
        try:
            if isinstance(a, dict) and b:
                for x in range(len(a)):
                    temp_key = a.keys()[x]
                    temp_value = a[temp_key]
                    if isinstance(b, dict) and temp_value:
                        for y in range(len(b)):
                            temp_key_b = b.keys()[y]
                            temp_value_b = b[temp_key_b]
                            if not isinstance(temp_value, (list, dict)) and not isinstance(temp_value_b,(list, dict)):
                                if temp_key == temp_key_b:
                                    if temp_value != temp_value_b:
                                        log.debug('recv:{{{0}:{1}}} != expect:{{{2}:{3}}}'.format(temp_key,temp_value,temp_key_b,temp_value_b))
                            self.compareDict(temp_value,temp_value_b)
        except BaseException as msg:
            raise msg


