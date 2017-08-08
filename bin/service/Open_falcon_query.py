#!/usr/bin/env python
# !-*- coding:utf-8 -*-
import tornado.web

from bin.service import Outer_services
from bin.logic.Service_Mail import *
from bin.until import Logger
from bin.until import PR
import json

L = Logger.getInstance()
operator = \
    {
        "sendMail": Outer_services().open_falcon_send_mail
    }

class Query(tornado.web.RequestHandler):
    '''
    @author:windyStreet
    @time:2017年8月8日10:54:28
    @version:V0.1.0
    @func:"用于查询"
    @param:data:{
        } json #(not null)
    @notice:"用于open-falcon邮件发送内容"
    @return:None
    '''
    def get(self):
        _PR = PR.getInstance()
        try:
            method="open_falcon_send_mail"
            method = self.get_argument('method', '__error__')
            if method == "__error__":
                _PR.setCode(PR.Code_METHODERROR)
                _PR.setMsg("method ERROR , not give the method or get the method is __error__")
                return self.write(_PR.getPRBytes())

            # 需要重新进行单独处理数据数据结构
            data = json.loads(self.get_argument('data', None))

            L.debug("the service request method : " + str(method))
            L.debug("the service request parameter : " + str(data))
            self.write(operator.get(method)(data))
        except Exception as e:
            _PR.setCode(PR.Code_EXCEPTION)
            _PR.setMsg("exception ERROR :" + str(e))
            self.write(_PR.getPRBytes())
        pass
    def post(self):
        self.get()