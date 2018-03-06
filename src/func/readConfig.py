# coding=utf-8
import os
import sys
__author__ = 'xcma'
import yaml


def ABSpath():
    """获取当前的绝对路径"""
    ABSPATH = os.path.abspath(sys.argv[0])
    ABSPATH = os.path.dirname(ABSPATH)
    return ABSPATH

ConfigPath =  ABSpath()+"/src/conf/sys_config.yml"
ApiCaseConfPath = ABSpath()+ "/src/conf/caseSummary.yml"
InitParameterConfPath = ABSpath()+"/src/conf/init_param.yml"

def getconfig(confName='config'):
    try:
        path = ''
        if confName == 'apiCase':
            path = ApiCaseConfPath
        elif confName == 'init':
            path = InitParameterConfPath
        elif confName == 'config':
            path = ConfigPath
        f = open(path)
        dataMap = yaml.load(f)
        f.close()
        return dataMap
    except Exception as msg:
        raise msg
