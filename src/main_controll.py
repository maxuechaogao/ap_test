# coding:utf-8
__author__ = 'xcma'

import run

import platform
import time

# from func.helper.email import sendemail
from func.helper.globalValue import *
from controll.schedule import schedule
from func.readConfig import getconfig
from src.func.helper.misc import Misc

"""
流程控制类
"""
# 实例化日志
g_map = GlobalMap()
schedule = schedule()
Config_path_ym = 'config'
conf_value = getconfig(Config_path_ym)
log_levl = getconfig('init')['Local']['log']


def __init__():
    # 读取配置信息
    read_test_dir = conf_value['path']['test_dir']
    read_test_report = conf_value['path']['test_report']
    read_send_report = conf_value['path']['send_report']

    # test_dir    : 用例执行目录
    test_dir = Misc.ABSpath() + read_test_dir
    Misc.mkdir(path=Misc.ABSpath() + '/output', name="Testdir")
    log.debug('test_dir:%s' % test_dir)

    # global_dir  : 存放中间数据的文件夹
    Misc.mkdir(path=Misc.ABSpath() + '/output', name="Global")

    # 统计主程序执行次数
    set_times()

    # 提前清空执行目录
    Misc.del_file(dir=test_dir, filename='l')
    log.debug('remove_testdir=>ok')

    # test_report_path :  测试报告存放
    test_Report_path = Misc.ABSpath() + read_test_report
    Misc.mkdir(path=Misc.ABSpath() + "/output", name='TestReport')
    log.debug('test_Report_path:%s' % test_Report_path)

    # send_Report_path  :   根据系统指定不同发送报告存放路径
    send_Report_path = Misc.ABSpath() + read_send_report
    Misc.mkdir(path=Misc.ABSpath() + "/output", name='SendReport')
    log.debug('send_Report_path:%s' % send_Report_path)
    self = {
        'test_dir': test_dir,
        'test_Report_path': test_Report_path,
    }
    return self

def main(test_dir, test_Report_path):
    # 生成测试报告，并运行用例
    try:
        schedule.generate_case_suite(test_dir)
        schedule.generate_report(test_dir, test_Report_path)

    except BaseException as msg:
        log.error(msg)
        raise

def del_caseFile(test_dir):
    # 删除执行目录中的用例
    try:
        delete_TestDir = "yes"
        if delete_TestDir == 'yes':
            Misc.del_file(dir=test_dir, filename='l')
            log.debug('remove=>ok')
        else:
            log.debug('remove=>No')
    except:
        msg = u'操作执行目录失败'
        log.error(msg)
        raise msg

# def email(test_Report_path):
#     # 发送邮件
#     report = run.report
#     if report not in 'false':
#         sendemail(test_Report_path)

def del_report(test_Report_path,maxFileNum):
    # 删除TestReport中文件
    try:
        delete_report = run.del_report
        log.debug('is_del_report:{},report_path:{}'.format(delete_report,test_Report_path))
        if delete_report:
            Misc.del_file_the_earliest(dir=test_Report_path,
                                       maxFileNum=maxFileNum)
            log.debug('remove TestReport=>ok')
        else:
            log.debug('remove TestReport=>No')
    except:
        msg = u'操作TestReport中文件失败'
        log.error(msg)

def del_log(key, maxFileNum):
    # 删除Log中文件
    try:
        path = conf_value['log']['path']
        if key:
            Misc.del_file_the_earliest(dir=path,
                                       maxFileNum=maxFileNum)
            log.debug('remove log=>ok')
        else:
            log.debug('remove log=>No')
    except:
        msg = u'操作Log中文件失败'
        log.error(msg)



# 组装流程
time_stamp = Misc.getTimeStamp_now()
g_map.set(time_stamp=time_stamp)
starttime = time.time()
run_start_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(starttime))
rep = __init__()
test_dir = rep['test_dir']
test_Report_path = rep['test_Report_path']
main(test_dir, test_Report_path)
del_caseFile(test_dir)
# email(test_Report_path)
del_report(test_Report_path,5)
del_log(True,5)
stoptime = time.time()
run_end_time = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(stoptime))
dotime = stoptime - starttime
g_map.set(run_total_time=str("%.2f"%dotime),run_end_time=run_end_time,run_start_time=run_start_time)
log.debug('execution time：%.2fS' % dotime)
