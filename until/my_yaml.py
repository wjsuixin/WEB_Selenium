# -*- coding: utf-8 -*-
# author： wujiang
# datetime： 2021/12/6 16:47
import os,sys
base_path=os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_path)
import yaml
from base.logger import Logger

# 创建一个日志实例
logger = Logger(logger="read_yaml").getlog()

class ReadYmal:
    """
    yaml数据的操作
    """
    def load_yaml(self,files=None):
        """
        加载yaml文件
        """
        if files==None:
            files="/config/locator_element.yaml"
        try:
            fs=open(base_path+files,"r",encoding="utf-8")
            return yaml.load(fs,Loader=yaml.FullLoader)
        except:
            logger.error(f"该配置文件：'{base_path+files}'不存在。")

    def get_data(self,key,files=None):
        """
        获取key对应的数据
        """
        data=self.load_yaml(files)
        if key in data.keys():
            tmp=data.get(key)
            if tmp !=None:
                return tmp
        else:
            logger.error(f"'{key}'值不存在,请检查传递参数的正确性！")

    def write_yaml(self,data,files=None):
        """
        写入数据到yaml文件中
        """
        if files==None:
            files="/config/locator_element.yaml"
        try:
            fs=open(base_path+files,"a",encoding="utf-8")
            yaml.dump(data,fs) #装载数据
            return self.load_yaml(base_path + files)
        except:
            logger.error(f"该配置文件：'{base_path + files}'不存在,无法写入。")

    def split(self,data):
        """
        分离元素的定位信息，返回定位类型：type,定位值：value
        """
        split_data=self.get_data(data)
        if split_data!=None :
            if ">" in split_data:
                return split_data.split(">")
            else:
                logger.error(f"元素'{data}'的定位信息：'{split_data}'录入存在问题，请检查！")

read_yaml=ReadYmal()

if __name__ == '__main__':
    ry=ReadYmal()
    file="/config/test_data.yaml"
    print(ry.load_yaml(file))
    print(ry.get_data("user",file)["valid"]["user"])


