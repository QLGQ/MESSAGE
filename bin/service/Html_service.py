#!/usr/bin/env python
# !-*- coding:utf-8 -*-

import tornado.web
from bin.until import Path
import os

htmlPath = Path.getInstance().htmlPath + os.sep


class index(tornado.web.RequestHandler):
    def get(self):
        self.render(htmlPath + self.request.path)