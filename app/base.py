# coding=utf-8

import tornado.web
from tornado import gen

from config import config

class BaseHandler(tornado.web.RequestHandler):

    def initialize(self):
        self.session = None
        self.db_session = None
        self.session_save_tag = False
        self.thread_executor = self.application.thread_executor
        self.async_do = self.thread_executor.submit

    @property
    def db(self):
        if not self.db_session:
            self.db_session = self.application.db_pool()
        return self.db_session

    def write_json(self, json):
        self.set_header("Content-Type", "application/json; charset=UTF-8")
        self.write(json)

    def write_error(self, status_code, **kwargs):
        if not config['debug']:
            if status_code == 403:
                self.render("403.html")
            elif status_code == 404 or 405:
                self.render("404.html")
            elif status_code == 500:
                self.render("500.html")
        if not self._finished:
            super(BaseHandler, self).write_error(status_code, **kwargs)

    @gen.coroutine
    def on_finish(self):
        if self.db_session:
            self.db_session.close()
            # print "db_info:", self.application.db_pool.kw['bind'].pool.status()
        if self.session is not None and self.session_save_tag:
            yield self.session.save(self.session_expire_time)

