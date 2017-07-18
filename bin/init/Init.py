#!/usr/bin/env python
# !-*- coding:utf-8 -*-

from bin.logic.func import Conf_func
from bin.until import Logger

L = Logger.getInstance()


class Init(object):
    def init(self):
        # 配置文件初始化
        L.info("conf file init ")

        L.info("conf init into memory , starting...")
        Conf_func.getInstance().init_conf()


