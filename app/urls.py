# coding=utf-8
import app.index
import app.user
from tornado.web import url


# url映射
handlers = [
    url(r"/", app.index.MainHandler, name="index"),
    url(r"/user", app.user.UserHandler, name="user"),
]