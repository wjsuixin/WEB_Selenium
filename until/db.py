# -*- coding: utf-8 -*-
# author： wujiang
# datetime： 2021/12/23 13:59
from until.read_ini import ReadIni
from dbutils.pooled_db import PooledDB
import pymysql
import configparser
from base.logger import Logger
import os,sys
base_path=os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_path)
# 创建一个日志实例
logger = Logger(logger="MySQLConnection").getlog()
read_ini=ReadIni()
class MySQLConnection:
    """
    数据库连接池相关
    """
    def __init__(self,dbName="master"):
        config=configparser.ConfigParser()
        path=os.path.dirname(os.path.dirname(__file__))+"/config/db.conf"
        config.read(path,encoding="UTF-8")
        sections=config.sections()
        #数据库工厂
        dbFactory={}
        for dbName in sections:
            #读取相关属性
            maxconnections=config.get(dbName,"maxconnections")
            mincached=config.get(dbName,"mincached",)
            maxcached=config.get(dbName,"maxcached")
            host=config.get(dbName,"host")
            port=config.get(dbName,"port")
            user=config.get(dbName,"user")
            password=config.get(dbName,"password")
            database=config.get(dbName,"database")
            databasePooled=PooledDB(creator=pymysql,
                                    maxconnections=int(maxconnections),
                                    maxcached=int(maxcached),
                                    mincached=int(mincached),
                                    blocking=True,
                                    cursorclass=pymysql.cursors.DictCursor,
                                    host=host,
                                    port=int(port),
                                    user=user,
                                    password=password,
                                    database=database)
            dbFactory[dbName]=databasePooled
            self.connect=dbFactory[dbName].connection()
            self.cursor=self.connect.cursor()
            logger.info(f"获取数据库连接对象成功，连接池对象：{self.connect}")

    def query(self,sql):
        """
        查询数据库
        """
        self.cursor.execute(sql)
        result=self.cursor.fetchall()
        return result

if __name__ == '__main__':
    mysql=MySQLConnection()
    for i in mysql.query("吴姜-wujiang"):

        print(i)
