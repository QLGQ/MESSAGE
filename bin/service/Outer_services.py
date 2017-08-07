#!/usr/bin/env python
# !-*- coding:utf-8 -*-

from bin.logic import Msg_logic

# 对外发布接口
class Outer_services(object):
    def __init__(self):
        pass

    def send_msg(self,data):
        return Msg_logic.getInstance(data).send_msg()
        pass