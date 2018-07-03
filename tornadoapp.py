# coding: utf-8
import sys
import concurrent.futures
import tornado.ioloop
import tornado.web
import os.path
import logging

from config import config
from app.base import BaseHandler
from app.urls import handlers
import model.db
import app.log
import app.optional

# tornado server相关参数
settings = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    compress_response=config['compress_response'],
    xsrf_cookies=config['xsrf_cookies'],
    cookie_secret=config['cookie_secret'],
    debug=config['debug'],
    default_handler_class=BaseHandler,
)

logger = logging.getLogger(__name__)

class Application(tornado.web.Application):
    def __init__(self):
        super(Application, self).__init__(handlers, **settings)
        self.thread_executor = concurrent.futures.ThreadPoolExecutor(config['max_threads_num'])
        self.db_pool = model.db.create_db_pool()


if __name__ == "__main__":
    if len(sys.argv) >= 2:
        if sys.argv[1] == 'upgradedb':
            # 更新数据库结构，初次获取或更新版本后调用一次python main.py upgradedb即可
            # from alembic.config import main
            # main("upgrade head".split(' '), 'alembic')
            exit(0)
    # 加载命令行配置
    app.optional.init_options()
    # 加载日志管理
    app.log.init(config['port'], config['log_console'], config['log_file'], config['log_file_path'], config['log_level'])
    # 创建application
    application = Application()
    logger.info('====== web server starting at http://0.0.0.0:{0} ======'.format(config['port']))                                                                             
    application.listen(config['port'])
    # 全局注册application
    config['application'] = application
    if config['debug']:
        logger.info('web server running mode is debug')
    tornado.ioloop.IOLoop.current().start()
    