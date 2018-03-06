# coding:utf-8
__author__ = 'xcma'

import logging
import logging.handlers
import time, os,sys
import inspect
from src.func.readConfig import getconfig
import platform
rq = time.strftime('%Y%m%d', time.localtime(time.time()))

reload(sys)
sys.setdefaultencoding('utf-8')

field = getconfig()['log']['field']
def ABSpath():
    """获取当前的绝对路径"""
    ABSPATH = os.path.abspath(sys.argv[0])
    ABSPATH = os.path.dirname(ABSPATH)
    return ABSPATH

Config_value = getconfig('config')
# 定义log存储路径
alog = Config_value['log']
# 建立Log目录
sysstr = platform.system()
if(sysstr =="Windows"):
    path = ABSpath()+alog['win_relative_path']
elif(sysstr == "Linux"):
    path = alog['lin_path']
else:
    path = ABSpath()+alog['mac_relative_path']
if not os.path.isdir(path):
    os.makedirs(path)

handlers = {logging.NOTSET: ""+path+"Notset_" + rq + ".log",
            logging.DEBUG: ""+path+"Debug_" + rq + ".log",
            logging.INFO: ""+path+"Info_" + rq + ".log",
            logging.WARNING: ""+path+"Warning_" + rq + ".log",
            logging.ERROR: ""+path+"Error_" + rq + ".log",
            logging.CRITICAL: ""+path+"Critical_" + rq + ".log"}

def levelasnum():
    """
    组装日志等级字典
    :return:
    """
    dic = {
        'n':'NOTSET',
        'notset':'NOTSET',
        'd':'DEBUG',
        'debug':'DEBUG',
        'i':'INFO',
        'info':'INFO',
        'w':'WARNING',
        'warning':'WARNING',
        'e':'ERROR',
        'error':'ERROR',
        'c':'CRITICAL',
        'critical':'CRITICAL'
    }
    dic_2 = {
        'n':0,
        'notset':0,
        'd':10,
        'debug':10,
        'i':20,
        'info':20,
        'w':30,
        'warning':30,
        'e':40,
        'error':40,
        'c':50,
        'critical':50
    }
    return dic_2

def createHandlers():
    """
    创建全局handle
    :return:
    """
    logLevels = handlers.keys()
    for level in logLevels:
        path = os.path.abspath(handlers[level])
        handlers[level] = logging.FileHandler(path)

def consoleprintHandlers():
    """
    单独控制控制台输出
    """
    level_in = Config_value['log']['console_print_level']
    logLevels = handlers.keys()
    if level_in:
        if level_in == 'all':
            for level_ in logLevels:
                handlers[level_] = logging.StreamHandler()
        elif level_in in levelasnum().keys():
            level_ = levelasnum()[level_in]  # 对应等级的数字
            values_lsit = levelasnum().values()
            print_num_list = []
            for i in values_lsit:
                if level_ <=i:
                    print_num_list.append(i)
            for level_ in print_num_list:
                handlers[level_] = logging.StreamHandler()

# 加载模块时创建全局变量
createHandlers()
consoleprintHandlers()
class log(object):
    """
    存在问题：不能同时在控制台输出 并且将日志记录在文件中
    """
    def __init__(self, level=logging.NOTSET):
        self.__loggers = {}

        logLevels = handlers.keys()
        for level in logLevels:
            logger = logging.getLogger(str(level))
            # 如果不指定level，获得的handler似乎是同一个handler?
            logger.addHandler(handlers[level])
            logger.setLevel(level)
            self.__loggers.update({level: logger})

    def printfNow(self):
        return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

    def getLogMessage(self, level, message):

        frame, filename, lineNo, functionName, code, unknowField = inspect.stack()[2]
        '''日志格式：[时间] [类型] [记录代码] 信息'''
        filename = filename.split('/')[-1]
        filename = filename.split('\\')[-1]

        # return "[%s] [%s] [%s - line:%s - %s] -- %s" % (self.printfNow(), level, filename, lineNo, functionName, message)
        if field==1:
            return "%s" % ( message)
        elif field==2:
            return "%s - %s" % (self.printfNow(), message)
        else:
            return "%s -%s- %s[line:%s]-%s: %s" % (self.printfNow(), level, filename, lineNo, functionName, message)

    def notset(self, message='start'):
        message = self.getLogMessage("notset", message)
        self.__loggers[logging.NOTSET].notset(message)

    def debug(self, message='start'):
        message = self.getLogMessage("debug", message)
        self.__loggers[logging.DEBUG].debug(message)

    def info(self, message='start'):
        message = self.getLogMessage("info", message)
        self.__loggers[logging.INFO].info(message)

    def error(self, message):
        message = self.getLogMessage("error", message)
        self.__loggers[logging.ERROR].error(message)

    def warning(self, message):
        message = self.getLogMessage("warning", message)
        self.__loggers[logging.WARNING].warning(message)

    def critical(self, message):
        message = self.getLogMessage("critical", message)
        self.__loggers[logging.CRITICAL].critical(message)
