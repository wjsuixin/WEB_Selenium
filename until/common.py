# -*- coding: utf-8 -*-
# author： wujiang
# datetime： 2021/12/10 15:10

import os,sys
base_path=os.path.dirname(os.path.dirname(__file__))
sys.path.append(base_path)
class Common():
    """
    def get_user(self,type):

        从配置文件中获取到

        file="/config/test_data.yaml"
        user=read_yaml.get_data("user",files=file)[type]["user"]
        password=read_yaml.get_data("user",files=file)[type]["password"]
        return user,password

    """
    def get_file(self):
        files=[]
        file_path=bath_path+"\\data\\file_type\\"
        for file in os.walk(file_path):
            for i in (file[2]):
                files.append(file_path+i)
        return files

if __name__ == '__main__':
    con=Common()
    print(con.get_file())

