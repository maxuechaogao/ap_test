# coding=utf-8
import json

__author__ = 'xcma'

import string
import os
import sys
from log import log

log = log()
def ABSpath():
    """获取当前的绝对路径"""
    ABSPATH = os.path.abspath(sys.argv[0])
    ABSPATH = os.path.dirname(ABSPATH)
    return ABSPATH

# 处理字符串类传参，主要适配run——result
def set_value(*input_value):
    global value
    value = input_value
def get_value():
    return value

def parsing_string(input_string):
    """解析用例运行结果字符串"""
    if input_string != '':

        try:
            if '=' in str(input_string):
                result_toup = input_string.split(' ')
                run_case_total = result_toup[1].split('=')[1]
                run_error_total = result_toup[2].split('=')[1]
                run_failures_total = result_toup[3].split('=')[1][0:1]
                run = string.atoi(run_case_total, 10)
                error = string.atoi(run_error_total, 10)
                fail = string.atoi(run_failures_total, 10)
                run_pass_total = run - error-fail
                return run_case_total, run_pass_total, run_failures_total, run_error_total
        except Exception as msg:
            log.error(msg)
            log.error('解析结果错误')
            raise
    else:
        run_case_total = 0
        run_pass_total = 0
        run_failures_total = 0
        run_error_total = 0
        return run_case_total, run_pass_total, run_failures_total, run_error_total

# 处理记录次数传参，主要适配当前程序执行次数
timesFile = ABSpath() + "/Output/Global/Times.txt"
def save_times_as_file(times):
    """
    将times保持在文件中
    :param times:
    :return:
    """
    fp = open(timesFile, 'w')
    try:
        fp.write(str(times))
    except IOError as msg:
        print msg
    finally:
        fp.close()

def read_times_file():
    """
    读取times保持文件中的内容
    :return:
    """
    fp = open(timesFile, 'r+')
    try:
        times = fp.read()
        return int(times)
    except IOError as msg:
        print msg
    finally:
        fp.close()


def del_file(dir, filename):
    """
    删除指定目录dir中与filename相同的文件
    :param dir:
    :param filename:
    :return:
    """
    dir = str(dir)
    if os.listdir(dir):
        for file in os.listdir(dir):
            if file == filename:
                os.remove(dir + file)
def set_times():
    try:
        times = read_times_file()
        if times >= 20:
            times = 0
    except:
        save_times_as_file(0)
        times = read_times_file()
    finally:
        times += 1
        save_times_as_file(times)

def get_times():
    try:
        times = read_times_file()
    except:
        save_times_as_file(0)
        times = read_times_file()
    finally:
        return times


class GlobalMap:
    # 拼装成字典构造全局变量  借鉴map  包含变量的增删改查
    map = {}

    def set_map(self, key, value):
        if(isinstance(value,dict)):
            value = json.dumps(value)
        self.map[key] = value
        log.debug(key + ":" + str(value))


    def set(self, **keys):
        try:
            for key_, value_ in keys.items():
                self.map[key_] = str(value_)
                log.debug(key_+":"+str(value_))
        except BaseException as msg:
            log.error(msg)
            raise msg

    def del_map(self, key):
        try:
            del self.map[key]
            return self.map
        except KeyError:
            log.error("key:'" + str(key) + "'  不存在")


    def get(self,*args):
        try:
            dic = {}
            for key in args:
                if len(args)==1:
                    dic = self.map[key]
                    log.debug(key+":"+str(dic))
                elif len(args)==1 and args[0]=='all':
                    dic = self.map
                else:
                    dic[key]=self.map[key]
            return dic
        except KeyError:
            log.warning("key:'" + str(key) + "'  不存在")
            return 'Null_'
