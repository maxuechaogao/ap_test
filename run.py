# coding=utf-8
__author__ = 'xcma'

import os, sys, getopt, json
from src.func.readConfig import getconfig
reload(sys)
sys.setdefaultencoding('utf8')

def ABSpath():
    """获取当前的绝对路径"""
    ABSPATH = os.path.abspath(sys.argv[0])
    ABSPATH = os.path.dirname(ABSPATH)
    return ABSPATH

msg = "ParameterError:参数错误，You can get help in this way:[-h]"

# 若依赖的binary文件放在系统PATH下(如/usr/local/bin)，1. 安装起来比较分散，2. 因权限等出了毛病难定位
# 故，放在当前目录的bin下，用脚本自动安装
os.environ["PATH"] += (os.pathsep + ABSpath() + '/bin')

Init_config_path_ym = "init"
value_all = getconfig(Init_config_path_ym)['value_all']

# 读value
level_value = value_all['level_value']
report_value = value_all['report_value']
del_value = value_all['del_value']
email_value = value_all['email_value']
send_email_value = value_all['send_email_value']

# 初始值设置：
environment = getconfig(Init_config_path_ym)['Environment']['environment']
category_local = "Local"
category_production = "Production"
category = ""
if environment in category_local:
    print ("""本地环境""")
    category = category_local

elif environment in category_production:
    print ("""部署环境""")
    category = category_production

config = getconfig(Init_config_path_ym)[category]
log = config['log']
report = config['report']
del_report = config['del_report']
email = config['email']
send_who = config['send_who']
run_case = config['run_case']
all_case_name = config['all_case_name']
run_case_by_filename = config['run_case_by_filename']

# 读取全部可执行用例名称
ApiCaseSummary_path_ym = "apiCase"

def usage():
    """使用说明"""
    print ("""
    参数使用说明:
        -l  """+str(level_value)+"""
        -r  """+str(report_value)+"""
        -d  """+str(del_value)+"""
        -e  """+str(email_value)+"""
        -s  """+str(send_email_value)+"""
        -c  [ 用例小名字      ]
     --acn  [ 打印所有用用例名称     ]
      --fn  [ 制定执行用例文件名称：test_a.py        ]
    !**
        -l: log                 default: """ + log + """
        -r: report              default: """ + str(report) + """
        -d: del_report          default: """ + str(del_report) + """
        -e: email               default: """ + str(email) + """
        -s: send_email_who      default: """ + send_who + """
        -c: run_case_shortname  default: """ + run_case + """
     --acn: all_case_name       default: """ + all_case_name + """
      --fn: run_case_file_name  default: """ + run_case_by_filename + """
    eg: python Run.py -l info -b chrome -r true
        python Run.py --db local_mysql
    """)


# 检查传入参数是否正确
inputparameter = []
for i in range(1, len(sys.argv)):
    parameter = sys.argv[i]
    inputparameter = inputparameter + [parameter]

# 参数设置，【必须在参数后面添加冒号】，如果不加冒号则对应的参数值会进入到args[]中
opts, args = getopt.getopt(sys.argv[1:], 'hl:b:r:d:u:m:s:e:c:p:',['db=','fn=','url=','acn='])
"""说明：参数h为开关，l：为日志级别输出参数；如果新增p参数，则可以'hl:p:'这样写"""
if '-h' not in inputparameter and sys.argv == []:
    if not opts:
        print ('-h:' + msg)
        sys.exit()

# 命令行q
for op, value in opts:
    # 选择日志在控制台的输出级别
    if op == '-l':
        if value in level_value:
            log = value
        else:
            print ('level:' + str(msg))
            print ('level:' + str(level_value))
            sys.exit()


    # 是否生成测试报告
    elif op == '-r':
        if value in report_value:
            report = value
        else:
            print ('report:' + msg)
            print ('report_value:' + str(report_value))
            sys.exit()

    # 删除测试报告
    elif op == '-d':
            if value in del_value:
                del_report = value
            else:
                print ('del_report:' + msg)
                print ('del_report_value:' + str(del_value))
                sys.exit()

    # 是否发送邮件
    elif op == '-e':
        if value in email_value:
            email = value
        else:
            print ("Email:" + msg)
            print ("Email_value:" + email_value)
            sys.exit()

    # 发送给谁
    elif op == '-s':
        if value in send_email_value:
            send_who = value
        else:
            print ("receive_email_name:" + msg)
            print ("receive_email_name:" + str(send_email_value))
            sys.exit()

    # 指定运行case， value
    elif op == '-c':
        if ',' not in value:
            run_case = value
        else:
            run_case = value.split(',')

    # 打印全部可执行用例名称
    elif op == '--acn':
        all_case_name = value
        if all_case_name in "api":
            ApiCaseSummary = json.dumps(getconfig(ApiCaseSummary_path_ym), indent=4)
            print (ApiCaseSummary)


    # 通过用例文件名进行测试
    elif op == '-fn':
        if ',' not in value:
            run_case_by_filename = value
        else:
            run_case_by_filename = value.split(',')

    elif op == '-h':
        usage()
        sys.exit()

import src.main_controll