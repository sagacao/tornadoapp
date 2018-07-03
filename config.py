# coding=utf-8

# 数据库配置
database_config = dict(
    engine=None,
    # engine_url='postgresql+psycopg2://mhq:1qaz2wsx@localhost:5432/blog',
    # 如果是使用mysql+mysqldb，在确认所有的库表列都是uft8编码后，依然有字符编码报错，
    # 可以尝试在该url末尾加上queryString charset=utf8
    engine_url='mysql+mysqldb://root:123456@localhost:3306/serverdb?charset=utf8',
    engine_setting=dict(
        echo=False,  # print sql
        echo_pool=False,
        # 设置7*60*60秒后回收连接池，默认-1，从不重置
        # 该参数会在每个session调用执行sql前校验当前时间与上一次连接时间间隔是否超过pool_recycle，如果超过就会重置。
        # 这里设置7小时是为了避免mysql默认会断开超过8小时未活跃过的连接，避免"MySQL server has gone away”错误
        # 如果mysql重启或断开过连接，那么依然会在第一次时报"MySQL server has gone away"，
        # 假如需要非常严格的mysql断线重连策略，可以设置心跳。
        # 心跳设置参考https://stackoverflow.com/questions/18054224/python-sqlalchemy-mysql-server-has-gone-away
        pool_recycle=25200,
        pool_size=20,
        max_overflow=20,
    ),
)

# 站点相关配置以及tornado的相关参数
config = dict(
    debug=True,
    log_level="DEBUG", #WARNING
    log_console=True,
    log_file=True,
    log_file_path="logs/log",  # 末尾自动添加 @端口号.txt_日期
    compress_response=True,
    xsrf_cookies=False,
    cookie_secret="kjsdhfweiofjhewnfiwehfneiwuhniu",
    port=8008,
    max_threads_num=500,
    database=database_config,
    master=True,  # 是否为主从节点中的master节点, 整个集群有且仅有一个,(要提高可用性的话可以用zookeeper来选主,该项目就暂时不做了)
    navbar_styles={"inverse": "魅力黑", "default": "优雅白"},  # 导航栏样式
    default_avatar_url="identicon",
    application=None,  # 项目启动后会在这里注册整个server，以便在需要的地方调用，勿修改
)