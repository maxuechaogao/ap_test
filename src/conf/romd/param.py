# coding:utf-8
__author__ = 'xcma'

syn = {
    'info': {
        "casename": "test_syn",
        "comment": "用例编号：4.1|三次握手，发送的第一个包"
    },
    'param': {"cmd": "syn",
              "params": {"pack_name": "supervcloud", "pack_ver": "v1.0.2", "pack_author": "supervcloud",
                         "pack_date": "2017-12-28", "pack_description": "supervcloud", "ifversionlist": ["v1"]}}
}
syn_a = {
    'info': {
        "casename": "test_syn",
        "comment": "用例编号：4.1|三次握手，发送的第一个包|cmd错误"
    },
    'param': {"cmd": "ssyn",
              "params": {"pack_name": "supervcloud", "pack_ver": "v1.0.2", "pack_author": "supervcloud",
                         "pack_date": "2017-12-28", "pack_description": "supervcloud", "ifversionlist": ["v1"]}},
    'expect': {'status': 400, 'id': 72, 'result': {'msg': '', 'code': 5003}}

}
syn_b = {
    'info': {
        "casename": "test_syn",
        "comment": "用例编号：4.1|三次握手，发送的第一个包|参数pack_name为空"
    },
    'param': {"cmd": "syn",
              "params": {"pack_name": "", "pack_ver": "v1.0.2", "pack_author": "supervcloud",
                         "pack_date": "2017-12-28", "pack_description": "supervcloud", "ifversionlist": ["v1"]}}
}
syn_c = {
    'info': {
        "casename": "test_syn",
        "comment": "用例编号：4.1|三次握手，发送的第一个包|参数ifversionlist值类型错误"
    },
    'param': {"cmd": "syn",
              "params": {"pack_name": "supervcloud", "pack_ver": "v1.0.2", "pack_author": "supervcloud",
                         "pack_date": "2017-12-28", "pack_description": "supervcloud", "ifversionlist": 1}},
    'expect': {'status': 400, 'id': 72, 'result': {'msg': '', 'code': 5005}}

}

syn_d = {
    'info': {
        "casename": "test_syn",
        "comment": "用例编号：4.1|三次握手，发送的第一个包|参数ifversionlist=['v10']值错误"
    },
    'param': {"cmd": "syn",
              "params": {"pack_name": "supervcloud", "pack_ver": "v1.0.2", "pack_author": "supervcloud",
                         "pack_date": "2017-12-28", "pack_description": "supervcloud", "ifversionlist": ["v10"]}},
    'expect': {'status': 400, 'id': 72, 'result': {'msg': '', 'code': 5006}}

}
syn_e = {
    'info': {
        "casename": "test_syn",
        "comment": "用例编号：4.1|三次握手，发送的第一个包|参数ifversionlist=['v1','v2','v10']"
    },
    'param': {"cmd": "syn",
              "params": {"pack_name": "supervcloud", "pack_ver": "1.0.2", "pack_author": "supervcloud",
                         "pack_date": "2017-12-28", "pack_description": "supervcloud", "ifversionlist": ['v1','v2','v10']}},

}
ack = {
    'info': {
        "casename": "test_ack",
        "comment": "用例编号:4.1|三次握手，发送的第二个包"
    },
    'param': {"cmd": "ack",
              "status":200,
              "params": {"ifversion": "v1", "code": 0, "msg": ""}
              }
}
ack_a = {
    'info': {
        "casename": "test_ack",
        "comment": "用例编号:4.1|三次握手，发送的第二个包|cmd错误"
    },
    'param': {"cmd": "acks",
              "status":200,
              "params": {"ifversion": "v1", "code": 0, "msg": ""}
              }
}
ack_b = {
    'info': {
        "casename": "test_ack",
        "comment": "用例编号:4.1|三次握手，发送的第二个包|ifversion=1类型错误"
    },
    'param': {"cmd": "ack",
              "status":200,
              "params": {"ifversion": 1, "code": 0, "msg": ""}
              }
}
ack_c = {
    'info': {
        "casename": "test_ack",
        "comment": "用例编号:4.1|三次握手，发送的第二个包|ifversion=v2协商失败"
    },
    'param': {"cmd": "ack",
              "status":400,
              "params": {"ifversion": "v2", "code": 5006, "msg": ""}
              }
}
set302 = {
    'info': {
        "casename": "test_set302",
        "comment": "用例编号：4.3|设置302跳转页面"
    },
    'param': {"id": 72, "cmd": "set_s302", "params": {"s302url": "http://192.168.1.1:86/s302.html"}},
    'expect': {'status': 200, 'id': 72, 'result': {'msg': '', 'code': 0}}
}

set302_a = {
    'info': {
        "casename": "test_set302",
        "comment": "用例编号：4.3|设置302跳转页面|| cmd错误"
    },
    'param': {"id": 72, "cmd": "set_s30", "params": {"s302url":  "http://192.168.1.1:86/s302.html"}},
    'expect': {'status': 400, 'id': 72, 'result': {'msg': '', 'code': 5003}}
}
set302_b = {
    'info': {
        "casename": "test_set302",
        "comment": "用例编号：4.3|设置302跳转页面|| s302url=1类型错误"
    },
    'param': {"id": 72, "cmd": "set_s302", "params": {"s302url": 1}},
    'expect': {'status': 400, 'id': 72, 'result': {'msg': '', 'code': 5005}}
}

set302_c = {
    'info': {
        "casename": "test_set302",
        "comment": "用例编号：4.3|设置302跳转页面|| s302url值错误"
    },
    'param': {"id": 72, "cmd": "set_s302", "params": {"s302url": "192.168.1.1"}},
    'expect': {'status': 400, 'id': 72, 'result': {'msg': '', 'code': 5005}}
}
set302_d = {
    'info': {
        "casename": "test_set302",
        "comment": "用例编号：4.3|设置302跳转页面|| s302url值为空"
    },
    'param': {"id": 72, "cmd": "set_s302", "params": {"s302url": ""}},
    'expect': {'status': 400, 'id': 72, 'result': {'msg': '', 'code': 5004}}
}
set302_e = {
    'info': {
        "casename": "test_set302",
        "comment": "用例编号：4.3|设置302跳转页面|| s302url_json格式错误"
    },
    'param': {'in_param': {"id": 72, "cmd": "set_s302", "params": {"s302url": "http://192.168.1.1:86/s302.html"}}},
    'expect': {'status': 400, 'id': 72, 'result': {'msg': '', 'code': 5006}},

}

get_gwinfo = {
    'info': {
        "casename": "test_get_gwinfo",
        "comment": "用例编号：4.4|获取网关信息"
    },
    'param': {"id": 94, "cmd": "get_gwinfo", "params": {}},
    "except": {"status": 200, "id": 94, "result": {"code": 0, "msg": "", "data": {"rip": "172.16.16.1", "dialup": 1, "dns_server":["", ""], "vlan": {"lan1": [1], "lan2": [1], "lan3": [50, 70], "lan4": [50, 70], "wan1": [2, 50, 70]}, "itv": ["lan3", "lan4"]}}}
}

get_gwinfo_a = {
    'info': {
        "casename": "test_get_gwinfo",
        "comment": "用例编号：4.4|获取网关信息|cmd错误"
    },
    'param': {"id":94,"cmd":"get_gwinffo","params":{}},
    #王益写的   ：
    # "except": {"status": 400, "id": 5003, "result": {"code": 0, "msg": "", "data": {"rip": "172.16.16.1", "dialup": 1, "dns_server":["", ""], "vlan": {"lan1": [1], "lan2": [1], "lan3": [50, 70], "lan4": [50, 70], "wan1": [2, 50, 70]}, "itv": ["lan3", "lan4"]}}}
    #超哥写的：
    'expect': {'status': 400, 'id': 72, 'result': {'msg': '', 'code': 5003}},


}

get_gwinfo_b = {
    'info': {
        "casename": "test_get_gwinfo",
        "comment": "用例编号：4.4|获取网关信息|params参数错误"
    },
    'param': {"id":94,"cmd":"get_gwinfo","params":{'a':1}},
    #王益写的：
    #"except": {"status": 200, "id": 94, "result": {"code": 0, "msg": "", "data": {"rip": "172.16.16.1", "dialup": 1, "dns_server":["", ""], "vlan": {"lan1": [1], "lan2": [1], "lan3": [50, 70], "lan4": [50, 70], "wan1": [2, 50, 70]}, "itv": ["lan3", "lan4"]}}}
    #超哥写的：
    'expect': {'status': 200, 'id': 94, 'result': {'msg': '', 'code': 0}}
}
pass_user = {
    'info': {
        "casename": "test_pass_user",
        "comment": "用例编号：4.5|放行指定终端有效mac,"
    },
    'param': {"id": 94, "cmd": "pass_user", "params": {"uip": "", "umac": "000EC6D38EC1"}},
    'expect': {'status': 200, 'id': 94, 'result': {'msg': '', 'code': 0}}
}
pass_user_a = {
    'info': {
        "casename": "test_pass_user",
        "comment": "用例编号：4.5|放行指定终端mac|uip错误，umac为空"
    },
    'param': {"id": 94, "cmd": "pass_user", "params": {"uip": "192.145.1.1", "umac": ""}},
    'expect': {'status': 400, 'id': 72, 'result': {'msg': '', 'code': 5006}}
}

pass_user_b = {
    'info': {
        "casename": "test_pass_user",
        "comment": "用例编号：4.5|放行指定终端mac|uip/umac都为空"
    },
    'param': {"id": 94, "cmd": "pass_user", "params": {"uip": "", "umac": ""}},
    'expect': {'status': 400, 'id': 72, 'result': {'msg': '', 'code': 5004}}
}
pass_user_c = {
    'info': {
        "casename": "test_pass_user",
        "comment": "用例编号：4.5|放行指定终端mac|cmd为错误"
    },
    'param': {"id": 94, "cmd": "", "params": {"uip": "192.145.1.1", "umac": "000EE6DDDDA1"}},
    'expect': {'status': 400, 'id': 72, 'result': {'msg': '', 'code': 5003}}
}
pass_user_d = {
    'info': {
        "casename": "test_pass_user",
        "comment": "用例编号：4.5|放行指定终端mac|uip为空，umac错误"
    },
    'param': {"id": 94, "cmd": "pass_user", "params": {"uip": "", "umac": "000EE6DDDDC1"}},
    'expect': {'status': 400, 'id': 72, 'result': {'msg': '', 'code': 5006}}
}
pass_user_e = {
    'info': {
        "casename": "test_pass_user",
        "comment": "用例编号：4.5|放行指定终端mac|umac类型错误"
    },
    'param': {"id": 94, "cmd": "pass_user", "params": {"uip": "192.145.1.1", "umac": 123213123456}},
    'expect': {'status': 400, 'id': 72, 'result': {'msg': '', 'code': 5005}}
}
pass_user_e1 = {
    'info': {
        "casename": "test_pass_user",
        "comment": "用例编号：4.5|放行指定终端mac|umac类型错误"
    },
    'param': {"id": 94, "cmd": "pass_user", "params": {"uip": "192.145.1.1", "umac": 1232131}},
    'expect': {'status': 400, 'id': 72, 'result': {'msg': '', 'code': 5005}}
}
pass_user_e2 = {
    'info': {
        "casename": "test_pass_user",
        "comment": "用例编号：4.5|放行指定终端mac|umac类型错误"
    },
    'param': {"id": 94, "cmd": "pass_user", "params": {"uip": "192.145.1.1", "umac": 12321312345611}},
    'expect': {'status': 400, 'id': 72, 'result': {'msg': '', 'code': 5005}}
}
pass_user_f = {
    'info': {
        "casename": "test_pass_user",
        "comment": "用例编号：4.5|放行指定终端mac|umac格式错误"
    },
    'param': {"id": 94, "cmd": "pass_user", "params": {"uip": "192.145.1.1", "umac": "E6DDDDW1"}},
    'expect': {'status': 400, 'id': 94, 'result': {'msg': '', 'code': 5005}}
}
pass_user_g = {
    'info': {
        "casename": "test_pass_user",
        "comment": "用例编号：4.5|放行指定终端mac|uip格式错误"
    },
    'param': {"id": 94, "cmd": "pass_user", "params": {"uip": "192.145.1", "umac": "000EE6DDDDC1"}},
    'expect': {'status': 400, 'id': 72, 'result': {'msg': '', 'code': 5005}}
}
pass_user_g1 = {
    'info': {
        "casename": "test_pass_user",
        "comment": "用例编号：4.5|放行指定终端mac|uip格式错误288"
    },
    'param': {"id": 94, "cmd": "pass_user", "params": {"uip": "192.168.1.288", "umac": "000EE6DDDDC1"}},
    'expect': {'status': 400, 'id': 94, 'result': {'msg': '', 'code': 5005}}
}
pass_user_g2 = {
    'info': {
        "casename": "test_pass_user",
        "comment": "用例编号：4.5|放行指定终端mac|uip类型错误"
    },
    'param': {"id": 94, "cmd": "pass_user", "params": {"uip": 192, "umac": "000EE6DDDDC1"}},
'expect': {'status': 400, 'id': 72, 'result': {'msg': '', 'code': 5005}}
}
jump_user = {
    'info': {
        "casename": "test_jump_user",
        "comment": "用例编号：4.6|控制用户跳转"
    },
    'param': {"id": 105, "cmd": "jump_user", "params": {"uip": "192.145.1.3", "umac": "000EE6DDDDC1"}},
    'expect': {'status': 200, 'id': 94, 'result': {'msg': '', 'code': 0}}
}
jump_user_a = {
    'info': {
        "casename": "test_jump_user",
        "comment": "用例编号：4.6|控制用户跳转|umac为空，uip错误"
    },
    'param': {"id": 105, "cmd": "jump_user", "params": {"uip": "192.145.1.3", "umac": ""}},
    'expect': {'status': 400, 'id': 72, 'result': {'msg': '', 'code': 5006}}
}
jump_user_b1 = {
    'info': {
        "casename": "test_jump_user",
        "comment": "用例编号：4.6|控制用户跳转|uip为空，umac错误"
    },
    'param': {"id": 105, "cmd": "jump_user", "params": {"uip": "", "umac": "000EE6DDDDA1"}},
    'expect': {'status': 400, 'id': 105, 'result': {'msg': '', 'code': 5006}}
}
jump_user_b = {
    'info': {
        "casename": "test_jump_user",
        "comment": "用例编号：4.6|控制用户跳转|uip为空，umac无效"
    },
    'param': {"id": 105, "cmd": "jump_user", "params": {"uip": "", "umac": "000EE6DDDDC1"}},
    'expect': {'status': 400, 'id': 105, 'result': {'msg': '', 'code': 5006}}
}
jump_user_c = {
    'info': {
        "casename": "test_jump_user",
        "comment": "用例编号：4.6|控制用户跳转|参数为空"
    },
    'param': {"id": 105, "cmd": "jump_user", "params": {"uip": "", "umac": ""}},
    'expect': {'status': 400, 'id': 72, 'result': {'msg': '', 'code': 5004}}
}
jump_user_d = {
    'info': {
        "casename": "test_jump_user",
        "comment": "用例编号：4.6|控制用户跳转|cmd错误"
    },
    'param': {"id": 105, "cmd": "jump_uer", "params": {"uip": "192.145.1.3", "umac": "000EE6DDDDC1"}},
    'expect': {'status': 400, 'id': 72, 'result': {'msg': '', 'code': 5003}}
}
jump_user_e = {
    'info': {
        "casename": "test_jump_user",
        "comment": "用例编号：4.6|控制用户跳转|umac类型错误"
    },
    'param': {"id": 105, "cmd": "jump_user", "params": {"uip": "", "umac": 31231}},
    'expect': {'status': 400, 'id': 105, 'result': {'msg': '', 'code': 5005}}
}
jump_user_f = {
    'info': {
        "casename": "test_jump_user",
        "comment": "用例编号：4.6|控制用户跳转|umac格式错误"
    },
    'param': {"id": 105, "cmd": "jump_user", "params": {"uip": "192.145.1.3", "umac": "0E6DDDDW1"}},
    'expect': {'status': 400, 'id': 105, 'result': {'msg': '', 'code': 5005}}
}
jump_user_g = {
    'info': {
        "casename": "test_jump_user",
        "comment": "用例编号：4.6|控制用户跳转|uip格式错误"
    },
    'param': {"id": 105, "cmd": "jump_user", "params": {"uip": "192.145.3", "umac": "000EE6DDDDC1"}},
    'expect': {'status': 400, 'id': 105, 'result': {'msg': '', 'code': 5005}}
}
jump_user_g1 = {
    'info': {
        "casename": "test_jump_user",
        "comment": "用例编号：4.6|控制用户跳转|uip类型错误"
    },
    'param': {"id": 105, "cmd": "jump_user", "params": {"uip": 192, "umac": "000EE6DDDDC1"}},
    'expect': {'status': 400, 'id': 105, 'result': {'msg': '', 'code': 5005}}
}
block_user = {
    'info': {
        "casename": "test_block_user",
        "comment": "用例编号：4.7|禁止用户上网"
    },
    'param': {"id":16,"cmd":"block_user","params":{"uip":"","umac":"000EE6DDDDC1"}},
    'expect': {'status': 200, 'id': 94, 'result': {'msg': '', 'code': 0}}

}
block_user_a = {
    'info': {
        "casename": "test_block_user",
        "comment": "用例编号：4.7|禁止用户上网|umac为空，uip错误"
    },
    'param': {"id":16,"cmd":"block_user","params":{"uip":"192.145.1.1","umac":""}},
    'expect': {'status': 400, 'id': 72, 'result': {'msg': '', 'code': 5006}}
}
block_user_b = {
    'info': {
        "casename": "test_block_user",
        "comment": "用例编号：4.7|禁止用户上网|uip为空，umac错误"
    },
    'param': {"id":16,"cmd":"block_user","params":{"uip":"","umac":"000ecDD38ec1"}},
    'expect': {'status': 400, 'id': 72, 'result': {'msg': '', 'code': 5006}}
}
block_user_c = {
    'info': {
        "casename": "test_block_user",
        "comment": "用例编号：4.7|禁止用户上网|参数为空"
    },
    'param': {"id":16,"cmd":"block_user","params":{"uip":"","umac":""}},
    'expect': {'status': 400, 'id': 72, 'result': {'msg': '', 'code': 5004}}
}
block_user_d = {
    'info': {
        "casename": "test_block_user",
        "comment": "用例编号：4.7|禁止用户上网|cmd错误"
    },
    'param': {"id":16,"cmd":"block_usr","params":{"uip":"192.168.125.3","umac":"000EE6DDDDC1"}},
    'expect': {'status': 400, 'id': 72, 'result': {'msg': '', 'code': 5003}}
}
block_user_e = {
    'info': {
        "casename": "test_block_user",
        "comment": "用例编号：4.7|禁止用户上网|umac类型错误"
    },
    'param': {"id":16,"cmd":"block_user","params":{"uip":"192.168.125.3","umac":2311232112}},
    'expect': {'status': 400, 'id': 72, 'result': {'msg': '', 'code': 5005}}
}
block_user_f = {
    'info': {
        "casename": "test_block_user",
        "comment": "用例编号：4.7|禁止用户上网|umac格式错误"
    },
    'param': {"id":16,"cmd":"block_user","params":{"uip":"192.168.125.3","umac":"006DDDDW1"}},
    'expect': {'status': 400, 'id': 72, 'result': {'msg': '', 'code': 5005}}
}
block_user_g = {
    'info': {
        "casename": "test_block_user",
        "comment": "用例编号：4.7|禁止用户上网|uip格式错误"
    },
    'param': {"id":16,"cmd":"block_user","params":{"uip":"192.141.1","umac":"000EE6DDDDC1"}},
    'expect': {'status': 400, 'id': 72, 'result': {'msg': '', 'code': 5005}}
}

get_all_user = {
    'info': {
        "casename": "test_get_all_user",
        "comment": "用例编号：4.8|获取所有在线用户用网策略"
    },
    'param':{"id":12,"cmd":"get_all_users","params":{}},
    "except": {"status": 200, "id": 12, "result": {"code": 0, "msg": "", "data": [{"onway":1, "widx":0, "ssid":"SuperVcloud WiFi", "uip":"", "umac":"AB00EF11DD99", "usingstate":1 }, {"onway":2, "uip":"", "umac":"AB00EF11DD98", "usingstate":2}]}}
}
get_all_user_a = {
    'info': {
        "casename": "test_get_all_user",
        "comment": "用例编号：4.8|获取所有在线用户用网策略|cmd错误"
    },
    'param':{"id":12,"cmd":"get_all_ussers","params":{}},
    #王益写的：
    #"except": {"status": 400, "id": 12, "result": {"code": 5003, "msg": "", "data": [{"onway":1, "widx":0, "ssid":"SuperVcloud WiFi", "uip":"", "umac":"AB00EF11DD99", "usingstate":1 }, {"onway":2, "uip":"", "umac":"AB00EF11DD98", "usingstate":2}]}}
    #超哥写的：
    'expect': {'status': 400, 'id': 72, 'result': {'msg': '', 'code': 5003}}
}
get_all_user_b = {
    'info': {
        "casename": "test_get_all_user",
        "comment": "用例编号：4.8|获取所有在线用户用网策略|参数错误"
    },
    'param':{"id":12,"cmd":"get_all_users","params":{'a':1}},
    #王益写的：
    #"except": {"status": 200, "id": 12, "result": {"code": 0, "msg": "", "data": [{"onway":1, "widx":0, "ssid":"SuperVcloud WiFi", "uip":"", "umac":"AB00EF11DD99", "usingstate":1 }, {"onway":2, "uip":"", "umac":"AB00EF11DD98", "usingstate":2}]}}
    #超哥写的：
    'expect': {'status': 200, 'id': 72, 'result': {'msg': '', 'code': 0}}
}
get_user = {
    'info': {
        "casename": "test_get_user",
        "comment": "用例编号：4.9|获取指定在线用户用网策略"
    },
    'param':{"id":138,"cmd":"get_user","params":{"umac":"000EE6DDDDC1"}},
    'expect':{'status': 200, 'id': 138, 'result': {'msg': '', 'code': 0, 'data': {'umac': '', 'ssid': '', 'onway': 2, 'uip': '', 'usingstate': 10, 'widx': 0}}}
}
get_user_e = {
    'info': {
        "casename": "test_get_user",
        "comment": "用例编号：4.9|获取指定在线用户用网策略|参数umac错误"
    },
    'param':{"id":138,"cmd":"get_user","params":{"umac":"000EE6DDDDC1"}},

}
get_user_a = {
    'info': {
        "casename": "test_get_user",
        "comment": "用例编号：4.9|获取指定在线用户用网策略|cmd错误"
    },
    'param': {"id": 138, "cmd": "get_usser","params": {"umac": "000EE6DDDDC1"}},
    #王益写的：
    #"except": {"status": 400, "id": 138, "result": {"code": 5003, "msg": "", "data": {"onway": 1, "widx": 0, "ssid":"SuperVcloud WiFi", "uip":"", "umac":"AB00EF11DD99", "usingstate":1}}}
    #超哥写的
    'expect': {'status': 400, 'id': 72, 'result': {'msg': '', 'code': 5003}}
}

get_user_b = {
    'info': {
        "casename": "test_get_user",
        "comment": "用例编号：4.9|获取指定在线用户用网策略|参数格式错误|umac=E6DDDDW1"
    },
    'param':{"id":138,"cmd":"get_user","params":{"umac":"E6DDDDW1"}},
    #王益写的：
    #"except": {"status": 400, "id": 138, "result": {"code": 5005, "msg": "","data": {"onway": 1, "widx": 0, "ssid": "SuperVcloud WiFi", "uip": "", "umac": "AB00EF11DD99", "usingstate": 1}}}
    #超哥写的：
    'expect': {'status': 400, 'id': 72, 'result': {'msg': '', 'code': 5005}}
}

get_user_c = {
    'info': {
        "casename": "test_get_user",
        "comment": "用例编号：4.9|获取指定在线用户用网策略|参数类型错误|umac=12312"
    },
    'param':{"id":138,"cmd":"get_user","params":{"umac":12312}},
    #王益写的：
    #"except": {"status": 400, "id": 138, "result": {"code": 5005, "msg": "","data": {"onway": 1, "widx": 0, "ssid": "SuperVcloud WiFi","uip": "", "umac": "AB00EF11DD99", "usingstate": 1}}}
    #超哥写的：
    'expect': {'status': 400, 'id': 72, 'result': {'msg': '', 'code': 5005}}
}
get_user_d = {
    'info': {
        "casename": "test_get_user",
        "comment": "用例编号：4.9|获取指定在线用户用网策略|参数为空|umac=''"
    },
    'param':{"id":138,"cmd":"get_user","params":{"umac":""}},
    #王益写的：
    #"except": {"status": 400, "id": 138, "result": {"code": 5004, "msg": "","data": {"onway": 1, "widx": 0, "ssid": "SuperVcloud WiFi", "uip": "", "umac": "AB00EF11DD99", "usingstate": 1}}}
    #超哥写的：
    'expect': {'status': 400, 'id': 72, 'result': {'msg': '', 'code': 5004}}
}

get_user_f = {
    'info': {
        "casename": "test_get_user",
        "comment": "用例编号：4.9|获取指定在线用户用网策略|使用测试机mac地址和ip"
    },
    'param':{"id":138,"cmd":"get_user","params":{"umac":"F83441282481"}},
    "except": {"status": 200, "id": 138, "result": {"code": 0, "msg": "",
                                                    "data": {"onway": 1, "widx": 0, "ssid": "SuperVcloud WiFi",
                                                             "uip": "", "umac": "AB00EF11DD99", "usingstate": 1}}}
}
set_whitelist = {
    'info': {
        "casename": "test_set_whitelist",
        "comment": "用例编号：4.10|设置网站白名单"
    },
    'param':{"id":149,"cmd":"set_whitelist","params":{"list":["test.com"]}},
    'expect': {'status': 200, 'id': 94, 'result': {'msg': '', 'code': 0}}

}
set_whitelist_a = {
    'info': {
        "casename": "test_set_whitelist",
        "comment": "用例编号：4.10|设置网站白名单|cmd错误"
    },
    'param':{"id":149,"cmd":"set_whielist","params":{"list":["test.com"]}},
    'expect': {'status': 400, 'id': 94, 'result': {'msg': '', 'code': 5003}}

}
set_whitelist_b = {
    'info': {
        "casename": "test_set_whitelist",
        "comment": "用例编号：4.10|设置网站白名单|list参数为空"
    },
    'param':{"id":1510,"cmd":"set_whitelist","params":{"list":[""]}},
    'expect': {'status': 400, 'id': 94, 'result': {'msg': '', 'code': 5004}}

}

set_whitelist_d = {
    'info': {
        "casename": "test_set_whitelist",
        "comment": "用例编号：4.10|设置网站白名单|多个重复参数值"
    },
    'param':{"id":1510,"cmd":"set_whitelist","params":{"list":["3g.163.com","3g.163.com","3g.163.com","3g.163.com"]}},
    'expect': {'status': 200, 'id': 94, 'result': {'msg': '', 'code': 0}}

}
set_whitelist_e = {
    'info': {
        "casename": "test_set_whitelist",
        "comment": "用例编号：4.10|设置网站白名单|多个不同参数值"
    },
    'param':{"id":1510,"cmd":"set_whitelist","params":{"list":["3g.163.com","www.baidu.com","3g.163.cm","3g.163.om"]}},
    'expect': {'status': 200, 'id': 94, 'result': {'msg': '', 'code': 0}}

}
set_whitelist_e1 = {
    'info': {
        "casename": "test_set_whitelist",
        "comment": "用例编号：4.10|设置网站白名单|list多个不同格式参数值"
    },
    'param':{"id":1510,"cmd":"set_whitelist","params":{"list":["3g.163.com","www.baidu.com",("3g.163.cm","3g.163.om"),1]}},
    'expect': {'status': 200, 'id': 94, 'result': {'msg': '', 'code': 0}}

}
set_whitelist_f = {
    'info': {
        "casename": "test_set_whitelist",
        "comment": "用例编号：4.10|设置网站白名单|参数格式错误list=1"
    },
    'param':{"id":1510,"cmd":"set_whitelist","params":{"list":1}},
    'expect': {'status': 400, 'id': 94, 'result': {'msg': '', 'code': 5005}}

}

add_whitelist = {
    'info': {
        "casename": "test_add_whitelist",
        "comment": "用例编号：4.11|增加网站白名单"
    },
    'param':{"id":1510,"cmd":"add_whitelist","params":{"list":["3g.163.com"]}},
    'expect': {'status': 200, 'id': 94, 'result': {'msg': '', 'code': 0}}
}
add_whitelist_a = {
    'info': {
        "casename": "test_add_whitelist",
        "comment": "用例编号：4.11|增加网站白名单|cmd错误"
    },
    'param':{"id":1510,"cmd":"add_whittlist","params":{"list":["3g.163.com"]}},
    'expect': {'status': 400, 'id': 94, 'result': {'msg': '', 'code': 5003}}

}
add_whitelist_b = {
    'info': {
        "casename": "test_add_whitelist",
        "comment": "用例编号：4.11|增加网站白名单|参数为空|list:[""]"
    },
    'param':{"id":1510,"cmd":"add_whitelist","params":{"list":[""]}},
    'expect': {'status': 400, 'id': 94, 'result': {'msg': '', 'code': 5004}}

}

add_whitelist_d = {
    'info': {
        "casename": "test_add_whitelist",
        "comment": "用例编号：4.11|增加网站白名单|list多个重复参数值"
    },
    'param':{"id":1510,"cmd":"add_whitelist","params":{"list":["3g.163.com","3g.163.com","3g.163.com","3g.163.com"]}},
    'expect': {'status': 200, 'id': 94, 'result': {'msg': '', 'code': 0}}

}
add_whitelist_e = {
    'info': {
        "casename": "test_add_whitelist",
        "comment": "用例编号：4.11|增加网站白名单|list多个不同参数值"
    },
    'param':{"id":1510,"cmd":"add_whitelist","params":{"list":["www.baidu.com","3g.163.cm","3g.163.om"]}},
    'expect': {'status': 200, 'id': 94, 'result': {'msg': '', 'code': 0}}

}
add_whitelist_e1 = {
    'info': {
        "casename": "test_add_whitelist",
        "comment": "用例编号：4.11|增加网站白名单|list多个不同格式参数值|list=['www.baidu.com','3g.163.cm',1]"
    },
    'param':{"id":1510,"cmd":"add_whitelist","params":{"list":["www.baidu.com",("3g.163.cm"),1]}},
    'expect': {'status': 400, 'id': 94, 'result': {'msg': '', 'code': 5005}}

}
add_whitelist_f = {
    'info': {
        "casename": "test_add_whitelist",
        "comment": "用例编号：4.11|增加网站白名单|list参数类型错误|list:1"
    },
    'param':{"id":1510,"cmd":"add_whitelist","params":{"list":1}},
    'expect': {'status': 400, 'id': 94, 'result': {'msg': '', 'code': 5005}}

}

get_whitelist = {
    'info': {
        "casename": "test_get_whitelist",
        "comment": "用例编号：4.12|获取全部白名单"
    },
    'param':{"id":1611,"cmd":"get_whitelist","params":{}},
}

get_whitelist_a = {
    'info': {
        "casename": "test_get_whitelist",
        "comment": "用例编号：4.12|获取全部白名单|cmd错误"
    },
    'param':{"id":1611,"cmd":"get_whtelist","params":{}},
    'expect': {'status': 400, 'id': 94, 'result': {'msg': '', 'code': 5003}}

}
get_whitelist_b = {
    'info': {
        "casename": "test_get_whitelist",
        "comment": "用例编号：4.12|获取全部白名单|参数错误"
    },
    'param':{"id":1611,"cmd":"get_whitelist","params":{'a':1}},
    'expect': {'status': 200, 'id': 94, 'result': {'msg': '', 'code': 0}}

}

set_wifi = {
    'info': {
        "casename": "test_set_wifi",
        "comment": "用例编号：4.13|设置无线参数"
    },
    'param': {"id": 1712, "cmd": "set_wifi",
              "params": {"data": [{"type": 2, "channel": 10, "biisolation": 0, 'txpower': 50,
                                   "ssidlist": [
                                       {"enable": 1, "widx": 0, "ssid": "one",
                                        "encrypt": 0, "key": "", "isolation": 0},
                                       {"enable": 1, "widx": 1, "ssid": "two",
                                        "encrypt": 1, "key": "12345678", "isolation": 1},
                                       {"enable": 0, "widx": 2, "ssid": "three",
                                        "encrypt": 0, "key": "12345678", "isolation": 0},
                                       {"enable": 1, "widx": 3, "ssid": "four",
                                        "encrypt": 0, "key": "12345678", "isolation": 0},
                                   ]}]}}
}
set_wifi_f = {
    'info': {
        "casename": "test_set_wifi",
        "comment": "用例编号：4.13|设置无线参数|设置2个ssid"
    },
    'param': {"id": 1712, "cmd": "set_wifi",
              "params": {"data": [{"type": 2, "channel": 10, "biisolation": 0, 'txpower': 50,
                                   "ssidlist": [
                                       {"enable": 1, "widx": 0, "ssid": "one",
                                        "encrypt": 0, "key": "", "isolation": 0},
                                       {"enable": 1, "widx": 1, "ssid": "two",
                                        "encrypt": 1, "key": "12345678", "isolation": 1},

                                   ]}]}},
    'expect': {'status': 200, 'id': 94, 'result': {'msg': '', 'code': 0}}

}
set_wifi_a = {
    'info': {
        "casename": "test_set_wifi",
        "comment": "用例编号：4.13|设置无线参数|cmd错误"
    },
    'param': {"id": 1712, "cmd": "set_witfi",
              "params": {"data": [{"type": 2, "channel": 10, "biisolation": 0, 'txpower': 50,
                                   "ssidlist": [
                                       {"enable": 1, "widx": 0, "ssid": "one",
                                        "encrypt": 0, "key": "", "isolation": 0},
                                       {"enable": 1, "widx": 1, "ssid": "two",
                                        "encrypt": 1, "key": "12345678", "isolation": 1},
                                       {"enable": 0, "widx": 2, "ssid": "three",
                                        "encrypt": 0, "key": "12345678", "isolation": 0},
                                       {"enable": 1, "widx": 3, "ssid": "four",
                                        "encrypt": 0, "key": "12345678", "isolation": 0},
                                   ]}]}},
    #王益的：
    #"except": {"status": 400, "id": 1712, "result": {"code":5003, "msg": ""}}
    #超哥写的：
    'expect': {'status': 400, 'id': 94, 'result': {'msg': '', 'code': 5003}}
}
set_wifi_b = {
    'info': {
        "casename": "test_set_wifi",
        "comment": "用例编号：4.13|设置无线参数|参数type=1值错误"
    },
    'param': {"id": 1713, "cmd": "set_wifi",
              "params": {"data": [{"type": 1, "channel": 11, "biisolation": 1, 'txpower': 40,
                                   "ssidlist": [
                                       {"enable": 1, "widx": 0, "ssid": "one",
                                        "encrypt": 1, "key": "", "isolation": 0},
                                       {"enable": 1, "widx": 1, "ssid": "two",
                                        "encrypt": 1, "key": "12345678", "isolation": 1},
                                       {"enable": 0, "widx": 2, "ssid": "three",
                                        "encrypt": 0, "key": "12345678", "isolation": 0},
                                       {"enable": 1, "widx": 3, "ssid": "four",
                                        "encrypt": 0, "key": "12345678", "isolation": 0},
                                   ]}]}},
    #王益写的：
    #"except": {"status": 400, "id": 1713, "result": {"code": 5006, "msg": ""}}
    #超哥写的：
    'expect': {'status': 400, 'id': 94, 'result': {'msg': '', 'code': 5006}}
}

set_wifi_c = {
    'info': {
        "casename": "test_set_wifi",
        "comment": "用例编号：4.13|设置无线参数|单频参数type=5"
    },
    'param': {"id": 1713, "cmd": "set_wifi",
              "params": {"data": [{"type": 5, "channel": 11, "biisolation": 1, 'txpower': 40,
                                   "ssidlist": [
                                       {"enable": 1, "widx": 0, "ssid": "one",
                                        "encrypt": 1, "key": "", "isolation": 0},
                                       {"enable": 1, "widx": 1, "ssid": "two",
                                        "encrypt": 1, "key": "12345678", "isolation": 1},
                                       {"enable": 0, "widx": 2, "ssid": "three",
                                        "encrypt": 0, "key": "12345678", "isolation": 0},
                                       {"enable": 1, "widx": 3, "ssid": "four",
                                        "encrypt": 0, "key": "12345678", "isolation": 0},
                                   ]}]}},
    #王益写的：
    #"except": {"status": 400, "id": 1713, "result": {"code": 5006, "msg": ""}}
    #超哥写的：
    'expect': {'status': 400, 'id': 94, 'result': {'msg': '', 'code': 5006}}
}

set_wifi_d = {
    'info': {
        "casename": "test_set_wifi",
        "comment": "用例编号：4.13|设置无线参数|参数enable类型错误"
    },
    'param': {"id": 1713, "cmd": "set_wifi",
              "params": {"data": [{"type": 2, "channel": 11, "biisolation": 1, 'txpower': 40,
                                   "ssidlist": [
                                       {"enable": '1', "widx": 0, "ssid": "one",
                                        "encrypt": 1, "key": "", "isolation": 0},
                                       {"enable": 1, "widx": 1, "ssid": "two",
                                        "encrypt": 1, "key": "12345678", "isolation": 1},
                                       {"enable": 0, "widx": 2, "ssid": "three",
                                        "encrypt": 0, "key": "12345678", "isolation": 0},
                                       {"enable": 1, "widx": 3, "ssid": "four",
                                        "encrypt": 0, "key": "12345678", "isolation": 0},
                                   ]}]}},
    "except": {"status": 400, "id": 1713, "result": {"code": 5006, "msg": ""}}
}

set_wifi_e = {
    'info': {
        "casename": "test_set_wifi",
        "comment": "用例编号：4.13|设置无线参数|参数ssid=1类型错误"
    },
    'param': {"id": 1713, "cmd": "set_wifi",
              "params": {"data": [{"type": 2, "channel": 11, "biisolation": 1, 'txpower': 40,
                                   "ssidlist": [
                                       {"enable": 1, "widx": 0, "ssid": 1,
                                        "encrypt": 1, "key": "", "isolation": 0},
                                       {"enable": 1, "widx": 1, "ssid": "two",
                                        "encrypt": 1, "key": "12345678", "isolation": 1},
                                       {"enable": 0, "widx": 2, "ssid": "three",
                                        "encrypt": 0, "key": "12345678", "isolation": 0},
                                       {"enable": 1, "widx": 3, "ssid": "four",
                                        "encrypt": 0, "key": "12345678", "isolation": 0},
                                   ]}]}},
    "except": {"status": 400, "id": 1713, "result": {"code": 5006, "msg": ""}}
}
get_wifi = {
    'info': {
        "casename": "test_get_wifi",
        "comment": "用例编号：4.14|获取无线参数"
    },
    'param': {"id":1813,"cmd":"get_wifi","params":{}}
}
get_wifi_a = {
    'info': {
        "casename": "test_get_wifi",
        "comment": "用例编号：4.14|获取无线参数|cmd错误"
    },
    'param': {"id":1813,"cmd":"get_wwifi","params":{}},
    'expect': {'status': 400, 'id': 94, 'result': {'msg': '', 'code': 5003}}

}
get_wifi_b = {
    'info': {
        "casename": "test_get_wifi",
        "comment": "用例编号：4.14|获取无线参数|参数错误"
    },
    'param': {"id":1813,"cmd":"get_wifi","params":{'a':2}},
    'expect': {'status': 200, 'id': 94, 'result': {'msg': '', 'code': 0}}

}