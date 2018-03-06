# coding=utf-8
__author__ = 'xcma'

import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import run
from globalValue import *
from src.func.readConfig import getconfig
from log import log
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
log = log()
g_map = GlobalMap()
report = run.report
def send_mail(send_file_path, send_who):
    """
    :param send_file_path: 测试报告文件路径
    :return:
    """
    Config_value = getconfig('config')
    email = Config_value['email']
    smtpserver = email['mail_host']
    smtpuser = email['mail_user']
    password = email['mail_pass']
    try:
        if send_who:
            mailto = send_who

        else:
            # 拼装接收人
            receive_category = "email_receiver_local"
            mailto = Config_value[receive_category]
        log.debug("send_file_path：%s" % send_file_path)
        log.debug("smtpserver：%s" % smtpserver)
        log.debug("smtpuser：%s" % smtpuser)
        log.debug("password：%s" % password)
        log.debug("mailto:%s" % mailto)
        msg = MIMEMultipart()
        # 定义发送人
        msg['From'] = smtpuser

        # 定义接收邮件对象
        msg['To'] = ",".join(mailto)

        # 拼装邮件标题
        try:
            value = g_map.get('result_run')
        except:
            log.error(u"Runner fail =》Report.py,result error")
        run_case_total, run_pass_total, run_failures_total, run_error_total = parsing_string(value)
        log.warning("run_case_total:%s" % str(run_case_total))
        log.warning("run_error_total:%s" % str(run_error_total))
        log.warning("run_failures_total:%s" % str(run_failures_total))
        log.warning("run_pass_total:%s" % str(run_pass_total))
        title = "[C:" + str(run_case_total) + "|P:" + str(run_pass_total) + "|F:" + str(
            run_failures_total) + "|E:" + str(run_error_total) + "]"
        Subject = "%sAPI_Report" % title
        times = get_times()
        if times in [49, 50]:
            Subject1 = "=>System_Push"
        else:
            Subject1 = ''
        Subject = Subject + Subject1
        msg['Subject'] = Header(Subject, 'utf-8').encode()
        msg["Accept-Language"] = "zh-CN"
        msg["Accept-Charset"] = "ISO-8859-1,utf-8"

        # 取第三方库生成html报告
        # file_name = new_report(send_file_path)
        # sendfile = send_file_path + file_name
        # fp = open(sendfile, 'rb')

        # content = """<h3><a href = "http://god.com/">点击查看在线报告系统</a><h3><h3>测试环境：[""" + input_url + """"] <h3>"""

        # 将html中内容贴在邮件正文中
        # msg.attach(MIMEText(content + fp.read(), 'html', 'utf-8'))

        # 添加附件
        # part = MIMEApplication(fp.read())
        # part.add_header('Content-Disposition', 'attachment', filename=file_name)
        # msg.attach(part)

        # fp.close()

        # 发送邮件
        content = """
        <h3><a href = "http://god.com/">点击查看在线报告系统</a><h3><h3>] <h3>
        """

        msg.attach(MIMEText(content, 'html', 'utf-8'))

        # server = smtplib.SMTP()
        # 不加密形式
        # server.connect(smtpserver, 25)
        # 通过ssl形式发送邮件
        server = smtplib.SMTP_SSL(smtpserver, 465)
        log.debug(u'邮件日志'+str(server.set_debuglevel(1)))
        server.login(smtpuser, password)
        server.sendmail(smtpuser, mailto, msg.as_string())
        server.quit()
        log.debug(u'邮件发送成功')
    except smtplib.SMTPDataError as msg:
        log.error(msg)
        log.debug(u'邮件发送失败')
    except IOError as msg:
        log.error(msg)
        log.error(u'拼装邮件失败')



def new_report(testreport):
    '''
    将文件按照名字时间顺序排序,输出文件名字
    :param testreport:测试报告存放路径
    :return:
    '''

    try:
        lists = os.listdir(testreport)
        log.debug(u'当前路径中文件列表' + str(lists))
        lists.sort(key=lambda fn: os.path.getmtime(testreport + '/' + fn))
        file_new = os.path.join(lists[-1])
        # 返回最新生成的文件名称
        log.debug(u'将要发送的测试报告文件：' + file_new)
        return file_new
    except Exception as msg:
        raise msg


def sendemail(test_Report_path):
    # 第20次执行用例，主动报告测试情况

    sendemail = run.email
    send_who = run.send_who
    times = get_times()
    log.debug("times:%s" % times)

    send_msg = 'send_email=> fail'
    send_mail_msg = 'send_email=> No'

    # 邮件标题
    run_case_total = g_map.get('run_case_total')
    run_pass_total = g_map.get('run_pass_total')
    run_failures_total = g_map.get('run_failures_total')
    run_error_total = g_map.get('run_error_total')


    if sendemail:
        try:
            send_mail(test_Report_path, send_who)
        except Exception as msg:
            log.error(send_msg)
            log.error(msg)
            raise msg

    elif sendemail == 'misc':
        if times in [49, 50]:
            try:
                send_mail(test_Report_path, send_who)
            except Exception as msg:
                log.error(send_msg)
                log.error(msg)
                raise msg

        elif run_error_total != '0' or run_failures_total != '0':
            try:
                send_mail(test_Report_path, send_who)
            except Exception as msg:
                log.error(send_msg)
                log.error(msg)

        elif send_who != 'Null':
            try:
                send_mail(test_Report_path, send_who)
            except Exception as msg:
                log.error(send_msg)
                log.error(msg)
                raise msg
        else:
            log.warning(send_mail_msg)
    else:
        log.warning(send_mail_msg)
