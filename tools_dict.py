#!/usr/bin/python3
# coding=utf-8

import os
from config import mark


# 获取工具类别的主目录
def tools_root_path():
    rootPath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    return rootPath


# 自动读取工具类别的列表,  特征识别:包含"--"的目录,平时做好分类
# 返回工具名称字典，格式{toolTYPE:[tools]}
def toolsDir():
    tools_dict = {}
    tool_type_root_dir = tools_root_path()  #工具主目录
    tool_type_dir = sorted([
        i for i in os.listdir(tool_type_root_dir)
        if (os.path.isdir(f"{tool_type_root_dir}\{i}")
            and i.count(mark.toolsTypeDirMark) == 1)
    ])
    #工具类别目录
    for toolType in tool_type_dir:
        tools = sorted([
            i for i in os.listdir(f'{tool_type_root_dir}\{toolType}')
            if os.path.isdir(f'{tool_type_root_dir}\{toolType}\{i}')
        ])  #
        tools_dict[toolType] = tools
    return tools_dict


if __name__ == '__main__':
    print(toolsDir())
