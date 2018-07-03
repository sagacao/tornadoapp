# coding=utf-8

from tornado.options import options
from config import config

#  从命令行读取配置，如果这些参数不传，默认使用config.py的配置项
def init_options():
    options.define("port", help="run server on a specific port", type=int)
    options.define("log_console", help="print log to console", type=bool)
    options.define("log_file", help="print log to file", type=bool)
    options.define("log_file_path", help="path of log_file", type=str)
    options.define("log_level", help="level of logging", type=str)
    # 集群中最好有且仅有一个实例为master，一般用于执行全局的定时任务
    options.define("master", help="is master node? (true:master / false:slave)", type=bool)
    # sqlalchemy engine_url, 例如pgsql 'postgresql+psycopg2://mhq:1qaz2wsx@localhost:5432/blog'
    options.define("engine_url", help="engine_url for sqlalchemy", type=str)

    # 读取 项目启动时，命令行上添加的参数项
    options.logging = None  # 不用tornado自带的logging配置
    options.parse_command_line()
    # 覆盖默认的config配置
    if options.port is not None:
        config['port'] = options.port
    if options.log_console is not None:
        config['log_console'] = options.log_console
    if options.log_file is not None:
        config['log_file'] = options.log_file
    if options.log_file_path is not None:
        config['log_file_path'] = options.log_file_path
    if options.log_level is not None:
        config['log_level'] = options.log_level
    if options.master is not None:
        config['master'] = options.master
    if options.engine_url is not None:
        config['database']['engine_url'] = options.engine_url

