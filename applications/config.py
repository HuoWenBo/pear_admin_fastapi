import os
import secrets
from typing import List


class Settings:
    BASEDIR = os.path.abspath(os.path.dirname(__file__))
    LOG_PATH = os.path.join(BASEDIR, 'logs')
    BACKEND_CORS_ORIGINS: List = ['*']

    # 数据库账号密码
    DB_HOST = '127.0.0.1'
    DB_PORT = 3306
    DB_USER = 'root'
    DB_PASSWORD = 'fastapivueblog12306'
    DB_NAME = 'FastAPIVueBlog'

    DATABASE_URI = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}'
    SQLALCHEMY_DATABASE_URI: str = f'mysql+aiomysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

    # 12 hours
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 12
    SECRET_KEY: str = secrets.token_urlsafe(32)
