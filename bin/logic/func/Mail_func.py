#!/usr/bin/env python
# !-*- coding:utf-8 -*-
from bin.until import Logger

L = Logger.getInstance()




class Mail_func(object):
    def send_mail(self, data):
        try:
            pass
        except Exception as e:
            L.error("send_mail error , msg :%s", e)

        print("发送邮件")
        pass


def getInstance():
    return Mail_func()
