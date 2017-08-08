#!/usr/bin/env python
# !-*- coding:utf-8 -*-
import sys

# add zhushi
sys.path.append(sys.path[0].replace("/bin", ""))  # 初始化项目路径

import tornado
from bin.service.Html_service import index
from bin.service import Service
from bin.service import Open_falcon_query as Qfq
from tornado.options import define, options
from bin.init import Init
from bin.until import Path
from bin.until import Logger
from bin import init

P = Path.getInstance()
L = Logger.getInstance()

if __name__ == "__main__":
    Init.Init().init()  # 系统初始化
    port = init.CONF_INFO["server"]["port"]
    context = init.CONF_INFO["server"]["context"]
    define("port", default=port, help="run on the given port", type=int)
    tornado.options.parse_command_line()
    app = tornado.web.Application(
        handlers=[(r"/" + context + "/service", Service),
                  (r"/" + context + "/open-falcon/mail/query", Qfq),
                  (r"/" + context + "/index.html", index)
                  ],
        template_path=P.htmlPath,
        static_path=P.webPath,
        debug=False
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    L.info("serer started , port is : %s , context is : %s ", port, context)
    tornado.ioloop.IOLoop.instance().start()
