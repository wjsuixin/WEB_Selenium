# -*- coding: utf-8 -*-
# author： wujiang
# datetime： 2021/12/6 10:23
import configparser
from base.logger import Logger
import os,sys
base_path=os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_path)
# 创建一个日志实例
logger = Logger(logger="until").getlog()
class ReadIni:
    """
    操作配置文件
    """
    def load_ini(self,filename=None):
        """
        加载配置文件
        """
        #if filename==None:
            #file_path=base_path+"/config/config.ini"
        #else:
        file_path=base_path+filename
        cf=configparser.ConfigParser()
        cf.read(file_path,encoding="utf-8")
        return cf

    def get_ini_data(self,section,key,filename):
        """
        获取配置文件中某个section下的key对应的值
        """
        try:
            logger.info(filename)
            value=self.load_ini(filename).get(section,key)
            logger.info(f"获取到{section}下的{key}对应值{value}。")
            return value
        except Exception as e:
            logger.error(f"请检查数据是否正确，未能检测到{section}下存在{key}，错误信息：{e}")

    def write_data(self,section,key,value,filename):
        """
        在某一个文件中的section中写入key=value
        """
        cf=self.load_ini(filename)
        if section not in cf.sections():
            cf.add_section(section)
        cf.set(section=section,option=key,value=value)
        fo=open(filename,"w",encoding="UTF-8")
        cf.write(fo)
        fo.close()
        logger.info(f"在{section}中写入{key}的值{value}成功。")

if __name__ == '__main__':
    read=ReadIni()
    data=read.get_ini_data("browser_type","browser","/config/config.ini")
    print(data)
