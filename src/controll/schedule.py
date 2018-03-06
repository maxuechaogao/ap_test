# coding:utf-8
import datetime

__author__ = 'xcma'

from src.func.helper.misc import Misc
from src.func.readConfig import getconfig
from src.func.helper.HTMLTestRunner import HTMLTestRunner
import unittest
from src.func.helper.globalValue import *
import run

reload(sys)
sys.setdefaultencoding('utf-8')

g_map = GlobalMap()

report = run.report
class schedule:

    def move_case(self, main_case_path, case_name, test_dir):
        """
        移动case文件
        :param main_case_path:
        :param case_name:
        :param test_dir:
        :return:
        """
        if type(main_case_path) == list:
            for path in main_case_path:
                # 寻找将执行用例的文件名称
                log.debug('case_name:%s' % case_name)
                find_case_path = Misc.ABSpath() + path
                # 寻找将执行用例的路径
                log.debug('find_case_path:' + str(find_case_path))
                case_path = find_case_path + case_name
                # 找到要执行的用例文件路径
                log.debug('case_path:' + str(case_path))
                Misc.copy_file(case_path, test_dir)
        else:
            log.debug('case_name:%s' % case_name)
            find_case_path = Misc.ABSpath() + main_case_path
            # 寻找将执行用例的路径
            log.debug('find_case_path:' + str(find_case_path))
            case_path = find_case_path + case_name
            # 找到要执行的用例文件路径
            log.debug('case_path:' + str(case_path))
            Misc.copy_file(case_path, test_dir)

    def generate_case_suite(self, test_dir):
        """
        1.读取用例集配置文件，并将需要执行的用例复制到执行目录中
            who = ui / api
        2.根据传入参数run_case，将制定用例移入test_dir文件夹中
        :param test_dir:
        :return:
        """
        try:
            test_dir = str(test_dir)
            category = "apiCase"
            case_main = getconfig('config')[category]

            # 全部可执行用例集及相应路径=》case_main
            log.debug('case_main:%s' % case_main)
            if case_main:
                # 通过用例小名进行测试
                for main_name, main_case_path in case_main.items():
                    # 根据平台选择执行用例[pc,m]
                    case = getconfig(category)[main_name]
                    try:
                        for case_key, case_name in case.items():
                            self.move_case(main_case_path, case_name, test_dir)
                    except:
                        log.warning("%s is null" % main_name)
            else:
                log.warning('case_main is Null')
        except Exception as msg:
            log.error(u'generate_case_suite=》fail')
            raise msg

    def generate_report(cls, test_dir, test_Report_path):
        """
        主套件执行方法
        :param test_dir:
        :param test_Report_path:
        :return:
        """
        try:
            test_dir = str(test_dir)
            test_Report_path = str(test_Report_path)
            now = datetime.datetime.now().strftime("%Y%m%d.%H%M%S.%f")[:-4]
            if report:
                filename = test_Report_path + now + '_report.html'
                fp = open(filename, 'wb')
                name = "API Automated test report"
                # 定义测试报告
                runner = HTMLTestRunner(stream=fp,
                                        title=name,
                                        description='General situation of testcase')
                log.debug(u'BY=>HtmlTestRunner')
            elif not report:
                runner = unittest.TextTestRunner()
                log.debug('BY=>Unittest')

            # 控制执行路径
            result_run = '<unittest.runner.TextTestResult run=0 errors=0 failures=0>'
            if os.listdir(test_dir):
                discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
                r = runner.run
                result_run = r(discover)
                run_case_total, run_pass_total, run_failures_total, run_error_total = parsing_string(str(result_run))
                log.debug(result_run)
                # 传递运行结果
                g_map.set(result_run=result_run)
                g_map.set(run_case_total=run_case_total)
                g_map.set(run_pass_total=run_pass_total)
                g_map.set(run_failures_total=run_failures_total)
                g_map.set(run_error_total=run_error_total)
            else:
                log.warning(u'test_dir is empty')

            if report:
                fp.close()
        except Exception as msg:
            log.error(u'Runner=》ERROR')
            raise msg


