# -*- coding: UTF-8 -*-

import os

root_path = os.path.dirname(os.path.abspath(__file__))

root_list = os.listdir(root_path)
for i in root_list:
    # print(os.path.join(root_path, i))
    for root, dirs, files in os.walk(os.path.join(root_path, i+'\\zh'), topdown=False):
        for name in files:
            if name.split(".")[-1] in ('md'):
                print(os.path.join(root, name))
                with open(os.path.join(root, name), "r+", encoding="utf-8") as f:
                    read_data = f.readlines()
                    # f.seek(0)
                    # f.truncate()   #清空文件
                    for i in read_data:
                        if i.find("](") >= 0:
                            if i.find("![") >= 0
                                pass
                            else:
                                print(i)
                            
                    # read_data.replace("** 示例： **", "**示例：**")
                    # f.write(read_data.replace("** 返回值描述： **", "**返回值描述：**"))
                    







