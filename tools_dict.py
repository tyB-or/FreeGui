#!/usr/bin/python3
# coding=utf-8


import os
import configparser
import json

# 读取style ini 配置，类外部引用conf_style，不是类内部self.config_style
styleIniPath = os.path.dirname(os.path.abspath(__file__))  #获取本py文件的所在目录（父目录）
styleIniPath = f"{styleIniPath}\config\config.ini"  # 拼接路径，获取style ini 文件路径
# print("config.ini文件的路径是：", styleIniPath)
conf_style = configparser.ConfigParser()  #下面是读取文件
conf_style.read(filenames=styleIniPath,
                encoding="utf-8")  #注意编码，读取config ini 配置

# 读取配置文件中的功能菜单并装换成列表，ini中应该是这样：fun = [[1,2],["q",1,"5"]]
funlist = conf_style.get("tool","funList")  #str
funlist = json.loads(funlist)  #去除引号，恢复列表
# print(funlist)
# print(funlist[1])

# funlist1 = conf_style.get("tool","fun")  #str
# funlist1 = json.loads(funlist1)  #去除引号，恢复列表
# print(funlist1,type(funlist1))
# print(funlist1[1][1],type(funlist1[1]))

# 获取工具类别的主目录
def tools_root_path():
    rootPath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    return rootPath


# 自动读取工具类别的列表,  特征识别:包含"--"的目录,平时做好分类
# 返回工具名称字典，格式{toolTYPE:[tools]}
# print(conf_style["tool"]["funList"])

# 获取目录时会根据标识符进行识别不同类目的子目录。例如：工具目录标识：--，笔记目录标识：~~
def toolsDir(type_mark = funlist[0][1]): #列表是二维列表，前名称后标识
    tools_dict = {}
    tool_type_root_dir = tools_root_path()  #工具主目录
    tool_type_dir = sorted([
        i for i in os.listdir(tool_type_root_dir)   if (os.path.isdir(f"{tool_type_root_dir}\{i}") and i.count(type_mark) == 1) ])
    #工具类别目录
    for toolType in tool_type_dir:
        tools = sorted(
            [i for i in os.listdir(f'{tool_type_root_dir}\{toolType}')  if os.path.isdir(f'{tool_type_root_dir}\{toolType}\{i}')])  #
        tools_dict[toolType] = tools
    return tools_dict

if __name__ == '__main__':
    print(toolsDir())


# 改造说明：
# 开发工具框架中的顶上的功能扩展位置，因为想最小化改动（偷懒），所以就不动变量名字了，只修改逻辑让代码通用。
# 修改思路：主目录仍在一起，但是获取目录时会根据标识符进行识别不同类目的子目录。例如：工具目录标识：--，笔记目录标识：~~
