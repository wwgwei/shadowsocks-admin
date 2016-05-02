#!/usr/bin/python
# -*- coding: utf-8 -*-
# author arrti

from __future__ import absolute_import, division, print_function, \
    with_statement

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.redis import Redis

from helper import Filters
from shadowsocks import Shadowsocks

app = Flask(__name__)
app.debug = True
app.config.from_pyfile('settings.py')
Filters(app.jinja_env).register() # 注册过滤器
ss = Shadowsocks()
if not ss.connect() or not ss.valid():
    ss = None

# database
db = SQLAlchemy(app)
redis = Redis(app)
from ss_admin import models

from ss_admin.views import dashboard # 路由必须在app的初始化之后
from ss_admin.views import manage
from ss_admin.views import add