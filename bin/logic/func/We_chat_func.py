#!/usr/bin/env python
# !-*- coding:utf-8 -*-
import json

import requests

MSG_CODE_TYPE=2
class We_chat_func(object):
    def __init__(self):
        self.appID = "wx0412ca50b0a56b5b"
        self.appsecret = "0991bc9f8ea275f156b7058e679c1af0"
        self.access_token = None
        self.template_id = None
        self.data = None
        pass

    def get_access_token(self):
        params = {'appid': self.appID, 'secret': self.appsecret}
        try:
            url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential"
            rs = requests.get(url, params=params)
            rs.close()
            self.access_token = rs.json()['access_token']
            print(self.access_token)
        except Exception as e:
            print("get access_token error! : %s", e)

    def message(self, touser, message):
        data = json.dumps({
            "touser": touser,
            "template_id": "yZYhsYandvjnrmSupG8H_XI08s-0HoQDbSsI_k02v0E",
            "url": "",
            "topcolor": "#FF0000",
            "data": {"mail_info": {"value": message, "color": "#173177"}}
        }, ensure_ascii=True)
        return data

    def send_we_chat(self, read_msg):
        if read_msg is None:
            print("not message to send")
        else:
            # touser = "oNlAk1PjqXbAipWb_GHIzwJmuVgM"#民工
            touser = "oNlAk1I6ZEUkjVh1qKv1dTDsIN8A"  # windyStreet
            message = read_msg
            try:
                print(self.access_token)
                url = 'https://api.weixin.qq.com/cgi-bin/message/template/send?access_token=' + self.access_token
                data = self.message(touser, message)
                print(data)
                res = requests.post(url, data=data)
                print(res.json())
                res.close()
            except Exception as e:
                print(e)
                print('send error!')


def getInstance():
    return We_chat_func()


def main():
    wc = We_chat_func()
    wc.get_access_token()
    while True:
        read_msg = input("输入break退出消息发送:")
        if read_msg == "break":
            break
        wc.send_we_chat(read_msg)


if __name__ == "__main__":
    main()
