#!/usr/bin/env python
# !-*- coding:utf-8 -*-

import json

'''
        @author:windStreet
        @time:2017年8月7日15:32:42
        @version:V0.1.0
        @func:"PR CODE defined"
        @notice:
            Code_ERROR = "0"  # 错误
            Code_OK = "1"  # 成功
            Code_EXCEPTION = "2"  # 异常（exception 异常信息）
            Code_PARERROR = "000"  # 参数错误（传递参数为空或者无法取值）
            Code_DATAERROR = "001"  # 数据错误（数据解析过程错误）
            Code_METHODERROR = "002"  # 方法错误 （传递方法名称不存在）
        @return:
'''
Code_ERROR = "0"  # 错误
Code_OK = "1"  # 成功
Code_EXCEPTION = "2"  # 异常
Code_PARERROR = "000"  # 参数错误
Code_DATAERROR = "001"  # 数据错误
Code_METHODERROR = "002"  # 方法错误


class PR(object):
    def __init__(self, **kwargs):
        self.kwargs = kwargs
        self.code = Code_OK
        self.msg = "ok"
        self.result = None

    @property
    def json(self):
        """JSON format data."""
        json = {
            'code': self.code,
            'msg': self.msg,
            'result': self.result,
        }
        json.update(self.kwargs)
        return json

    def setCode(self, code=1):
        self.code = code
        return self

    def setMsg(self, msg="ok"):
        self.msg = msg
        return self

    def setResult(self, result):
        self.result = result
        return self

    def getCode(self):
        return self.code

    def getMsg(self):
        return self.msg

    def getResult(self):
        return self.result

    def getPRBytes(self):
        return bytes(self.getPRStr(), encoding='utf-8')

    def getPR(self):
        return self

    def getPRStr(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys=True, indent=4)


def getInstance():
    return PR()
