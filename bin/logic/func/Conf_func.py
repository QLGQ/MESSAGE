#!/usr/bin/env python
# !-*- coding:utf-8 -*-

import os
from bin import init
from bin.until import Logger
from bin.until import JsonFileFunc
from bin.until import Path
from bin.until import Mongo

P = Path.getInstance()
L = Logger.getInstance()
J = JsonFileFunc.getInstance()


class Conf_func(object):
    # 初始化配置文件
    def init_conf(self):
        conf_path = P.confDirPath
        conf_json = {}
        for file_name in os.listdir(conf_path):
            if file_name == "conf.json":
                continue
            if file_name.endswith(".json"):
                conf_key = file_name.split(".")[0]
                conf_json[conf_key] = J.readFile(conf_path + os.sep + file_name)
        init.CONF_INFO = conf_json
        L.debug("init conf_json info is : %s", conf_json)
        J.createFile(conf_path + os.sep + "conf.json", conf_json)

def getInstance():
    return Conf_func()
