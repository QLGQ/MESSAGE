#!/usr/bin/env python
# !-*- coding:utf-8 -*-

from bin.until import PR
from bin.until import Data
from bin.logic import Smtp_logic


class Msg_logic(object):
    def __init__(self, data):
        if data["msg_code_type"] is None or type(data["msg_code_type"]) != "interger":
            self.msg_code_types = [1]
        else:
            self.msg_code_types = Data.get_bin_add_Datas(data["msg_code_type"])
        self.content = data["content"]

    def send_msg(self):
        if Smtp_logic.MSG_CODE_TYPE in self.msg_code_types:
            data = None
            Smtp_logic.getInstance().send_msg(data)
        # if We_chat_func.MSG_CODE_TYPE in self.msg_code_types:
        #     data = None
        #     We_chat_func.getInstance().send_we_chat(data)
        pass


def getInstance(data):
    if data is None:
        pr = PR.getInstance()
        pr.setCode(PR.Code_PARERROR)
        pr.setMsg("not set the instance par")
        return pr
        # return PR.getInstance().setCode(PR.Code_PARERROR).setMsg("not set the instance par").setResult(data).getPRBytes()
    return Msg_logic(data)
