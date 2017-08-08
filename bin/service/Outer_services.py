#!/usr/bin/env python
# !-*- coding:utf-8 -*-

from bin.logic import Msg_logic


# 对外发布接口
class Outer_services(object):
    def __init__(self):
        pass

    '''
        @author:windyStreet
        @time:2017年8月7日17:38:47
        @version:V0.1.0
        @func:"信息发送"·
        @param:data:{
            "send_type":7([1:邮件发送,2:微信发送,4:短信发送],7=1+2+4 邮件、微信、短信均发送,default val 1) int,
            "sender":"发送者"(default MESSAGE@platform.com.cn),
            "receivers":["windyStreet","wuqiang"],
            "group_receiver":{
                "group_name":YXYBB",
                "receive_levle":"接收级别"
            }
            "msg":{
                "type":"消息类型", # 这个决定信息是进行模板化处理
                "title":"信息主题",
                "content":"信息内容"
            }
        } json #(not null)
        @notice:""
        @PR:{
            "code": code
            "msg":msg
            "result":None
        }
        @return:PR
    '''

    def send_msg(self, data):
        Msg_logic.getInstance(data).send_msg()

    def open_falcon_send_mail(self, data):
        Msg_logic.getInstance(data).send_msg()
