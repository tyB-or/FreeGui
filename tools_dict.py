#!/usr/bin/python3
# coding=utf-8

import os
import configparser
import json

styleIniPath = os.path.dirname(os.path.abspath(__file__))
styleIniPath = f"{styleIniPath}\config\config.ini"

conf_style = configparser.ConfigParser()
conf_style.read(filenames=styleIniPath, encoding="utf-8")

funlist = conf_style.get("tool", "funList")
funlist = json.loads(funlist)


def tools_root_path():
    rootPath = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
    return rootPath


def toolsDir(type_mark=funlist[0][1]):
    tools_dict = {}
    tool_type_root_dir = tools_root_path()
    tool_type_dir = sorted([
        i for i in os.listdir(tool_type_root_dir)
        if (os.path.isdir(f"{tool_type_root_dir}\{i}")
            and i.count(type_mark) == 1)
    ])

    for toolType in tool_type_dir:
        tools = sorted([
            i for i in os.listdir(f'{tool_type_root_dir}\{toolType}')
            if os.path.isdir(f'{tool_type_root_dir}\{toolType}\{i}')
        ])
        tools_dict[toolType] = tools
    return tools_dict


if __name__ == '__main__':
    print(toolsDir())
