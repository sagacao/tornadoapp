# coding=utf-8

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import config

# sqlalchemy连接池配置以及生成链接池工厂实例
def create_db_pool():
    engine_config = config['database']['engine_url']
    engine_setting = config['database']["engine_setting"]
    engine = create_engine(engine_config, **engine_setting)
    config['database']['engine'] = engine
    db_poll = sessionmaker(bind=engine)
    return db_poll