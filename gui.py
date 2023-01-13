#!/usr/bin/python3
# coding=utf-8

import ttkbootstrap as ttk
from ttkbootstrap.constants import *  #导入常量
from ttkbootstrap.scrolled import ScrolledText, ScrolledFrame  #滚动模块
from ttkbootstrap.dialogs.dialogs import Messagebox  #消息提示的模块
import subprocess
import configparser  # python  读取ini配置文件的模块
import json

# from tkinter import *

import os
import datetime

import tools_dict


class APP(ttk.Frame):

    # 界面的主要构建代码，框架，组件等
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        # 主目录信息，源字典信息
        self.rootPath = tools_dict.tools_root_path()  #获取主目录信息，工具类别的父目录
        print(f"调试信息: 1.工具的类别目录是：\n{self.rootPath}\n")
        self.toolsDic = tools_dict.toolsDir()  #获取目录的字典信息
        # self.startCommandDict = self.openStartCommandIniFile()  #name:command

        # 读取样式配置文件信息.
        self.config_ini_path1 = os.path.dirname(
            os.path.abspath(__file__))  #获取本文件所在的父目录
        self.config_ini_path = f"{self.config_ini_path1}\config\config.ini"  #config.ini文件路径
        print(f"调试信息: 2.config.ini文件路径是: \n{self.config_ini_path}\n")
        # 读取配置信息，后续的一些配置都是直接从ini文件获取，引用${section:option}
        self.config_style = configparser.ConfigParser()
        self.config_style.read(filenames=self.config_ini_path,
                               encoding="utf-8")
        # print(self.config_style["app"]["title"])

        # 设置工具内部工具框和笔记框的宽度占比，3:2
        # 先转换参数-str--int
        self.app_size_w = int(self.config_style["app"]["size_w"])  # 工具的总宽2550
        self.app_size_h = int(self.config_style["app"]["size_h"])  # 工具的总高1550
        self.average = int(self.config_style["app"]["average"])  # 工具等分多少份 5
        self.tool_aver = int(self.config_style["app"]["tool_aver"])  #工具框架占比 3
        self.note_aver = int(self.config_style["app"]["note_aver"])  #笔记框架占比 2

        print(
            f"调试信息: 3.工具框架的宽是:\n{int(self.app_size_w/self.average*self.tool_aver)}\n"
        )
        print(
            f"调试信息: 4.笔记框架的宽是:\n{int(self.app_size_w/self.average*self.note_aver)}\n"
        )

        # 根窗口的宽高
        # self.height = mark.appHeight
        # self.width = mark.appWidth

        # 工具框架-容器， #ScrolledFrame
        self.toolFra = ttk.LabelFrame(
            self,
            text=self.config_style["tool"]["title"],  #mark.toolFrameText
            bootstyle=self.config_style["tool"]
            ["theme"],  #bootstyle=mark.toolFrameBootstyle
            width=int(self.app_size_w / self.average *
                      self.tool_aver),  #width=mark.toolFrameWidth
            height=self.app_size_h,  #height=mark.toolFrameHeight
            labelanchor=NW,
            padding=7,
            border=10)
        self.toolFra.pack(side="left",
                          fill=BOTH,
                          ipadx=7,
                          ipady=10,
                          padx=10,
                          pady=20)  #expand=True
        self.toolFrame = ScrolledFrame(
            self.toolFra,
            autohide=True,
            width=int(self.app_size_w / self.average * self.tool_aver),
            height=self.app_size_h + 500,  # 加500把滚动条撑开
            bootstyle=self.config_style["tool"][
                "scrolled"]  #bootstyle=mark.toolFrameBootstyle_Scrolled
        )  #bootstyle='danger-round
        self.toolFrame.pack(fill=BOTH, anchor=NW)

        # 笔记框架-容器
        self.noteFrame = ttk.LabelFrame(
            self,
            text=self.config_style["note"]["title"],
            bootstyle=self.config_style["note"]
            ["theme"],  #mark.noteFrameBootstyle
            width=int(self.app_size_w / self.average * self.note_aver
                      ),  #int(self.app_size_w/self.average*self.note_aver)
            height=self.app_size_h,  #self.app_size_h,
            labelanchor=NW,
            padding=7,
            border=10)
        self.noteFrame.pack(
            side="left",
            # fill=BOTH,
            ipadx=7,
            ipady=10,
            padx=10,
            pady=20)  #expand=True

        # 笔记框架内部分配：上面添加一个框架，主要包含2个组件：label：显示工具信息，button：保存笔记的文件
        self.noteFrame_up = ttk.Frame(
            self.noteFrame,
            bootstyle=self.config_style["note"]["theme_up"])  #可以调颜色,上面框架的主题
        self.noteFrame_up.pack(side="top", fill="x", ipadx=7, ipady=10)

        # 20230109删除
        # self.noteFrameToolLabel = ttk.Label(
        #     self.noteFrame_up,
        #     text="  查看笔记：--toolInfo--  ",
        #     bootstyle=self.config_style["note"]["funBtnBootstyle"])
        # self.noteFrameToolLabel.pack(anchor=W,
        #                              side="left",
        #                              padx=2,
        #                              pady=2,
        #                              ipadx=10,
        #                              ipady=10)

        self.noteFrameTxtSaveBtn = ttk.Button(
            self.noteFrame_up,
            text=" 保存笔记 ",
            bootstyle=self.config_style["note"]["funBtnBootstyle"]
        )  # ,width=10，bootstyle=self.config_style["note"]["funBtnBootstyle"]
        self.noteFrameTxtSaveBtn.pack(anchor=W,
                                      padx=2,
                                      pady=2,
                                      ipadx=10,
                                      side="left",
                                      ipady=10)
        # 1209 优化：启动工具，打开目录按钮, 启动工具命令的快速添加
        self.noteFrameStartBtn = ttk.Button(
            self.noteFrame_up,
            text=" 打开目录 ",
            bootstyle=self.config_style["note"]["funBtnBootstyle"])  #,width=10
        self.noteFrameStartBtn.pack(anchor=W,
                                    side="left",
                                    padx=2,
                                    pady=2,
                                    ipadx=10,
                                    ipady=10)

        # 1209 优化：启动工具，打开目录按钮, 启动工具命令的快速添加，gui刷新按钮--暂时实现不了
        self.noteFrameRefreshBtn = ttk.Button(
            self.noteFrame_up,
            text=" 刷新GUI ",
            bootstyle=self.config_style["note"]
            ["funBtnBootstyle"])  #,width=10  ,command=self.refreshWin
        self.noteFrameRefreshBtn.pack(anchor=W,
                                      side="left",
                                      padx=2,
                                      pady=2,
                                      ipadx=10,
                                      ipady=10)  #side=CENTER
        self.noteFrameRefreshBtn["command"] = self.refresh  #  手动刷新工具界面方法

        # 1209 优化：启动工具，打开目录按钮, 启动工具命令的快速添加
        self.noteFrameOpenDirBtn = ttk.Button(
            self.noteFrame_up,
            text=" 启动工具 ",
            bootstyle=self.config_style["note"]["funBtnBootstyle"])  #,width=10
        self.noteFrameOpenDirBtn.pack(anchor=W,
                                      side="left",
                                      padx=2,
                                      pady=2,
                                      ipadx=10,
                                      ipady=10)

        # 1209 优化：启动工具，打开目录按钮, 启动工具命令的快速添加
        self.noteFrameCommandBtn = ttk.Button(
            self.noteFrame_up,
            text=" 编辑启动命令 ",
            bootstyle=self.config_style["note"]["funBtnBootstyle"])  #,width=10
        self.noteFrameCommandBtn.pack(anchor=W,
                                      side="left",
                                      padx=2,
                                      pady=2,
                                      ipadx=10,
                                      ipady=10)  #side=CENTER
        self.noteFrameCommandBtn[COMMAND] = self.openStartCommandIniFile

        # 20230112优化，增加参数自定义，并提供工具内修改。
        self.noteFrameStyleBtn = ttk.Button(
        self.noteFrame_up,
        text=" 样式修改 ",
        bootstyle=self.config_style["note"]["funBtnBootstyle"])  #,width=10
        self.noteFrameStyleBtn.pack(anchor=W,
                                      side="right",
                                      padx=2,
                                      pady=2,
                                      ipadx=10,
                                      ipady=10)  #side=CENTER
        self.noteFrameStyleBtn[COMMAND] = self.openStyleIniFile  #绑定修改方法

        # 笔记框架内部分配：下面添加一个滚动txt控件，显示笔记内容。
        self.noteFrame_down = ttk.LabelFrame(
            self.noteFrame,
            text=self.config_style["note"]
            ["txt_title"],  #mark.noteFrameDownTxt
            style=self.config_style["note"]
            ["noteFrameDownStyle"],  #mark.noteFrameDownStyle
            padding=5)
        self.noteFrame_down.pack(fill=BOTH, padx=3, pady=3)

        self.txtCount = ScrolledText(
            self.noteFrame_down,
            width=int(self.app_size_w / self.average * self.note_aver),
            height=self.app_size_h,
            bootstyle=self.config_style["note"]
            ["scrolledTextBootstyle"],  #mark.noteFrameDownScrolled,
            autohide=True)
        self.txtCount.pack(fill=BOTH, side=BOTTOM, anchor=NW)

        # 框架生成方法，界面构建，即是左边的工具布局，同时也包含了右边的一些事件，代码等
        self.toolFrameFun()

    # 左边工具布局
    def toolFrameFun(self):
        print("调试信息: 5.应用总宽-工具宽-笔记宽-工具列宽: \n ", self.app_size_w,
              int(self.app_size_w / self.average * self.tool_aver),
              int(self.app_size_w / self.average * self.note_aver),
              self.config_style["tool"]["columnWidth"])
        print()
        print("调试信息: 6.应用总高-工具高-笔记高:  \n", self.app_size_h, self.app_size_h,
              self.app_size_h)
        print()
        print(f'调试信息: 7.工具列数：\n{self.config_style["tool"]["toolColumn"]}\n')
        print(f'调试信息: 8.工具列宽：\n{self.config_style["tool"]["columnWidth"]}\n')
        
        # 读取配置文件中的功能菜单并装换成列表，ini中应该是这样：fun = [[1,2],["q",1,"5"]],数字不用加引号，字符串需要
        # 因为想要实时生效，需要放到函数里面，如果设置为类属性修改起来麻烦
        toolFunlist = self.config_style.get("tool","funList")  #str
        toolFunlist = json.loads(toolFunlist)  #去除引号，恢复列表

        #  后续功能拓展预留位置，采用Checkbutton按钮，同时也起到采用等宽靠左布局作用--20221213添加--success-toolbutton
        for i in range(int(self.config_style["tool"]["toolColumn"])):  #一行多少列
            self.Btnfr1 = ttk.Button(
                self.toolFrame,
                text=toolFunlist[i][0],  #功能键，2维列表，0名称，1标识，mark.funList
                width=self.config_style["tool"]["columnWidth"],  #mark.toolFrameToolColumnWidth
                bootstyle=self.config_style["tool"]["funBtnBootstyle"],
                command=lambda arg=toolFunlist[i][1]:
                self.toolFunBtn(arg)).grid(pady=2, row=0,column=i)  #,state="disabled"，方法绑定
        r = 1
        # 工具类别按钮
        for k in self.toolsDic.keys(
        ):  ## width=20,#bootstyle="danger-outline，success-link"  （不设置20会自己撑开）
            self.btnToolType = ttk.Button(
                self.toolFrame,
                text=k,
                bootstyle=self.config_style["tool"]
                ["typeBtnBootstyle"],  #mark.toolTypeBootstyle
                command=lambda a=k:
                [self.openToolTypeNote(a),
                 self.toolTypeTitle(a)])  # 左键单击后2个事件，更新笔记和title,
            self.btnToolType.grid(
                row=r,
                column=0,
                columnspan=int(self.config_style["tool"]
                               ["toolColumn"]),  #mark.toolColumn,
                sticky=W)
            # 左键双击，打开cmd, 或者直接启动--类型按钮不需要这个功能
            # self.btnToolType.bind("<Double-Button-1>",lambda event,arg0=k:self.openToolCmd(arg0))  #核对下参数
            # 右键单击，打开目录
            self.btnToolType.bind("<Double-Button-1>",
                                  lambda event, arg0=k: self.openTypeDir(arg0))

            r += 1
            c = 0
            # 详细工具
            for i in self.toolsDic[k]:
                if c == int(self.config_style["tool"]
                            ["toolColumn"]):  #mark.toolColumn
                    r += 1
                    c = 0
                self.btnTools = ttk.Button(
                    self.toolFrame,
                    bootstyle=self.config_style["tool"]["toolBtnBootstyle"],
                    text=i,
                    # width=16,不设置btn的宽的话，下面设置sticky属性就会自己撑开，但是会左对齐，缺点，点击范围变小
                    command=lambda a=k, b=i: [
                        self.openToolNote(a, b),
                        self.toolTitle(a, b)
                    ])  # 左键单击后2个事件，更新笔记和title   ,width=16：删除就是另外一个布局
                #布局关键：不设置btn的宽的话，下面设置sticky属性就会自己撑开，但是会左对齐，缺点，点击范围变小
                #布局关键：设置btn的宽的话，下面设置sticky属性相当于是nswe且无法修改，但是会居中对齐，优点，点击范围变大
                self.btnTools.grid(row=r, column=c, sticky=N + S + W,
                                   pady=2)  #sticky=N + S + W+E
                # ToolTip(self.btnTools, text=str(k))   #增加提示---不能--1215
                # 右键单击，打开目录<ButtonPress-3>  #修改：1213-双击打开目录
                self.btnTools.bind(
                    "<Double-Button-1>",
                    lambda event, arg1=k, arg2=i: self.openToolDir(arg1, arg2))
                # 左键双击，打开cmd, 或者直接启动--类型按钮不需要这个功能，工具按钮需要-<Double-Button-1>  #修改：1213-滑动启动-按住鼠标左键移动--bug[改为右键单击启动]
                self.btnTools.bind("<ButtonPress-3>",
                                   lambda event, arg1=k, arg2=i: self.
                                   openToolCmd(arg1, arg2))  #核对下参数,,add= +

                c += 1
            r += 1

    # 笔记框架中的上面的框架信息显示--工具类型--框架重构和里面的控件绑定方法
    def toolTypeTitle(self, typedir):
        # 清除右边组件
        for widget in self.noteFrame_up.winfo_children():
            widget.destroy()

        # 创建布局，工具信息，笔记保存, 和 1209 优化：启动工具，打开目录按钮, 启动工具命令的快速添加
        # 20230109修改----删除
        # self.text1 = f'--{typedir}--'

        # self.noteFrameToolLabel = ttk.Label(
        #     self.noteFrame_up,
        #     text=self.text1,
        #     bootstyle=self.config_style["note"]["funBtnBootstyle"])
        # self.noteFrameToolLabel.pack(anchor=W,
        #                              side="left",
        #                              padx=10,
        #                              pady=10,
        #                              ipadx=10,
        #                              ipady=10)

        self.noteFrameTxtSaveBtn = ttk.Button(
            self.noteFrame_up,
            text=" 保存笔记 ",
            bootstyle=self.config_style["note"]["funBtnBootstyle"],
            command=lambda a=typedir: self.saveTypeNote(a))
        self.noteFrameTxtSaveBtn.pack(anchor=W,
                                      side="left",
                                      padx=2,
                                      pady=2,
                                      ipadx=10,
                                      ipady=10)  # pad同步上面的

        # 1209 优化：启动工具，打开目录按钮
        self.noteFrameStartBtn = ttk.Button(
            self.noteFrame_up,
            text=" 打开目录 ",
            bootstyle=self.config_style["note"]["funBtnBootstyle"])  #,width=10
        self.noteFrameStartBtn.pack(anchor=W,
                                    side="left",
                                    padx=2,
                                    pady=2,
                                    ipadx=10,
                                    ipady=10)
        self.noteFrameStartBtn[
            COMMAND] = lambda arg0=typedir: self.openTypeDir(arg0)

        # 1209 优化：启动工具，打开目录按钮, 启动工具命令的快速添加，，gui刷新按钮--暂时实现不了
        self.noteFrameRefreshBtn = ttk.Button(
            self.noteFrame_up,
            text=" 刷新GUI ",
            bootstyle=self.config_style["note"]["funBtnBootstyle"])  #,width=10
        self.noteFrameRefreshBtn.pack(anchor=W,
                                      side="left",
                                      padx=2,
                                      pady=2,
                                      ipadx=10,
                                      ipady=10)  #side=CENTER
        self.noteFrameRefreshBtn["command"] = self.refresh  #  手动刷新工具界面方法

        # 1209 优化：启动工具，打开目录按钮--工具类型按钮不需要该功能--这里不显示--改为显示
        self.noteFrameOpenDirBtn = ttk.Button(
            self.noteFrame_up,
            text=" 启动工具 ",
            bootstyle=self.config_style["note"]
            ["funBtnBootstyle"])  #,width=10  ,state=DISABLED
        self.noteFrameOpenDirBtn.pack(anchor=W,
                                      side="left",
                                      padx=2,
                                      pady=2,
                                      ipadx=10,
                                      ipady=10)

        # 1209 优化：启动工具，打开目录按钮, 启动工具命令的快速添加，--工具类型按钮不需要该功能--这里不显示--改为显示
        self.noteFrameCommandBtn = ttk.Button(
            self.noteFrame_up,
            text=" 编辑启动命令 ",
            bootstyle=self.config_style["note"]
            ["funBtnBootstyle"])  #,width=10   ,state=DISABLED
        self.noteFrameCommandBtn.pack(anchor=W,
                                      side="left",
                                      padx=2,
                                      pady=2,
                                      ipadx=10,
                                      ipady=10)  #side=CENTER
        self.noteFrameCommandBtn[COMMAND] = self.openStartCommandIniFile

        # 20230112优化，增加参数自定义，并提供工具内修改。
        self.noteFrameStyleBtn = ttk.Button(
        self.noteFrame_up,
        text=" 样式修改 ",
        bootstyle=self.config_style["note"]["funBtnBootstyle"])  #,width=10
        self.noteFrameStyleBtn.pack(anchor=W,
                                      side="right",
                                      padx=2,
                                      pady=2,
                                      ipadx=10,
                                      ipady=10)  #side=CENTER
        self.noteFrameStyleBtn[COMMAND] = self.openStyleIniFile  #绑定修改方法

    # 笔记框架中的上面的框架信息显示--具体工具--框架重构和里面的控件绑定方法
    def toolTitle(self, typedir, tool):
        # 清除右边组件
        for widget in self.noteFrame_up.winfo_children():
            widget.destroy()
        # 20230109修改，删除不显示
        # self.text1 = f'--{typedir}--{tool}--'

        # self.noteFrameToolLabel = ttk.Label(
        #     self.noteFrame_up,
        #     text=self.text1,
        #     bootstyle=self.config_style["note"]["funBtnBootstyle"])
        # self.noteFrameToolLabel.pack(anchor=W,
        #                              side="left",
        #                              padx=10,
        #                              pady=10,
        #                              ipadx=10,
        #                              ipady=10)

        self.noteFrameTxtSaveBtn = ttk.Button(
            self.noteFrame_up,
            text=" 保存笔记 ",
            bootstyle=self.config_style["note"]["funBtnBootstyle"],
            command=lambda a=typedir, b=tool: self.saveToolNote(
                a, b))  #,width = 20
        self.noteFrameTxtSaveBtn.pack(anchor=W,
                                      side="left",
                                      padx=2,
                                      pady=2,
                                      ipadx=10,
                                      ipady=10)

        # 1209 优化：启动工具，打开目录按钮
        self.noteFrameStartBtn = ttk.Button(
            self.noteFrame_up,
            text=" 打开目录 ",
            bootstyle=self.config_style["note"]["funBtnBootstyle"])  #,width=10
        self.noteFrameStartBtn.pack(anchor=W,
                                    side="left",
                                    padx=2,
                                    pady=2,
                                    ipadx=10,
                                    ipady=10)
        self.noteFrameStartBtn[
            COMMAND] = lambda arg1=typedir, arg2=tool: self.openToolDir(
                arg1, arg2)

        # # 1209 优化：启动工具，打开目录按钮, 启动工具命令的快速添加，gui刷新按钮--暂时实现不了
        self.noteFrameRefreshBtn = ttk.Button(
            self.noteFrame_up,
            text=" 刷新GUI ",
            bootstyle=self.config_style["note"]["funBtnBootstyle"])  #,width=10
        self.noteFrameRefreshBtn.pack(anchor=W,
                                      side="left",
                                      padx=2,
                                      pady=2,
                                      ipadx=10,
                                      ipady=10)  #side=CENTER
        self.noteFrameRefreshBtn["command"] = self.refresh  #  手动刷新工具界面方法--实现

        # 1209 优化：启动工具，打开目录按钮
        self.noteFrameOpenDirBtn = ttk.Button(
            self.noteFrame_up,
            text=" 启动工具 ",
            bootstyle=self.config_style["note"]["funBtnBootstyle"])  #,width=10
        self.noteFrameOpenDirBtn.pack(anchor=W,
                                      side="left",
                                      padx=2,
                                      pady=2,
                                      ipadx=10,
                                      ipady=10)
        self.noteFrameOpenDirBtn[
            COMMAND] = lambda arg1=typedir, arg2=tool: self.openToolCmd(
                arg1, arg2)

        # 1209 优化：启动工具，打开目录按钮, 启动工具命令的快速添加，
        self.noteFrameCommandBtn = ttk.Button(
            self.noteFrame_up,
            text=" 编辑启动命令 ",
            bootstyle=self.config_style["note"]["funBtnBootstyle"])  #,width=10
        self.noteFrameCommandBtn.pack(anchor=W,
                                      side="left",
                                      padx=2,
                                      pady=2,
                                      ipadx=10,
                                      ipady=10)  #side=CENTER
        self.noteFrameCommandBtn[COMMAND] = self.openStartCommandIniFile

        # 20230112优化，增加参数自定义，并提供工具内修改。
        self.noteFrameStyleBtn = ttk.Button(
        self.noteFrame_up,
        text=" 样式修改 ",
        bootstyle=self.config_style["note"]["funBtnBootstyle"])  #,width=10
        self.noteFrameStyleBtn.pack(anchor=W,
                                      side="right",
                                      padx=2,
                                      pady=2,
                                      ipadx=10,
                                      ipady=10)  #side=CENTER
        self.noteFrameStyleBtn[COMMAND] = self.openStyleIniFile  #绑定修改方法

    # 保存笔记-工具类型的笔记
    def saveTypeNote(self, typedir):
        notePath = f'{self.rootPath}\{typedir}\{self.config_style["app"]["txt_mark"]}'  #self.config_style["app"]["txt_mark"]
        # 重新读取控件中的内容
        content = self.txtCount.get(1.0, END)
        with open(notePath, "w", encoding='utf-8') as f:
            f.write(content)

    # 保存笔记-工具的笔记
    def saveToolNote(self, typedir, tool):
        notePath = f'{self.rootPath}\{typedir}\{tool}\{self.config_style["app"]["txt_mark"]}'
        # 重新读取控件中的内容,覆盖写入
        content = self.txtCount.get(1.0, END)
        with open(notePath, "w", encoding='utf-8') as f:
            f.write(content)

    # 打开笔记-工具的笔记
    def openToolNote(self, typedir, tool):
        notePath = f'{self.rootPath}\{typedir}\{tool}\{self.config_style["app"]["txt_mark"]}'
        # 修改笔记框架下面框架中的文本标题
        self.noteFrame_down["text"] = f"-- {self.rootPath}\{typedir}\{tool} --"
        # dirPath = f"{self.rootPath}\{typedir}\{tool}"
        #判断是不是目录
        # if os.path.isdir(dirPath):
        # 判断文件是不是存在
        if os.path.exists(notePath):
            with open(notePath, encoding='utf-8') as f:
                self.txtCount.delete('1.0', END)
                self.txtCount.insert(END, f.read())
        # 不存在，创建并写入提示信息
        else:
            Messagebox.ok(message="\n\t你还没有创建笔记，已自动创建初始化信息。\t\n",
                          title='OpenNote')  #,position=(mark.x,mark.y)
            infoMsg = f"-----你还没有创建笔记-----{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}-----"
            self.txtCount.delete('1.0', END)
            self.txtCount.insert(END, infoMsg)
            f = open(notePath, "w", encoding='utf-8')
            f.writelines(infoMsg)
            f.close()
        # # 不是目录，弹窗提示
        # Messagebox.ok(message="--你打开的不是目录--", title='OpenNote')

    # 打开笔记-工具类型的笔记
    def openToolTypeNote(self, typedir):
        notePath = f'{self.rootPath}\{typedir}\{self.config_style["app"]["txt_mark"]}'
        # 修改笔记框架下面框架中的文本标题
        self.noteFrame_down["text"] = f"-- {self.rootPath}\{typedir} --"
        # dirPath = f"{self.rootPath}\{typedir}"
        # #判断是不是目录
        # if os.path.isdir(dirPath):
        #判断文件是不是存在
        if os.path.exists(notePath):
            with open(notePath, encoding='utf-8') as f:
                self.txtCount.delete('1.0', END)
                self.txtCount.insert(END, f.read())
        # 不存在，创建并写入提示信息，初次会弹框提示
        else:
            Messagebox.ok(message="\n\t你还没有创建笔记，已自动创建初始化信息。\t\n",
                          title='OpenNote')  #,position=(mark.x,mark.y)
            infoMsg = f"-----你还没有创建笔记-----{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}-----"
            self.txtCount.delete('1.0', END)
            self.txtCount.insert(END, infoMsg)
            f = open(notePath, "w", encoding='utf-8')
            f.writelines(infoMsg)
            f.close()
        # # 不是目录，弹窗提示
        # Messagebox.ok(message="--你打开的不是目录--", title='OpenNote')

    # 打开目录--工具类型
    def openTypeDir(self, typedir):
        os.startfile(f'{self.rootPath}\{typedir}')

    # 打开目录--具体工具
    def openToolDir(self, typedir, tool):
        os.startfile(f'{self.rootPath}\{typedir}\{tool}')

    # 启动工具--后期待完善--可以在界面添加启动命令，双击直接启动，没有的话就进入cmd
    def openToolCmd(self, typedir, tool):
        os.chdir(f"{self.rootPath}\{typedir}\{tool}")
        # os.system(f"start cmd.exe cmd /k && title {tool} && cd {self.rootPath}\{typedir}\{tool}")
        iniPath = os.path.dirname(os.path.abspath(__file__))
        # print(path)
        iniPath = f"{iniPath}\config\startCommand.ini"  #f"{self.rootPath}\config\startCommand.json"
        conf = configparser.ConfigParser()
        conf.read(filenames=iniPath, encoding="utf-8")
        #cmd,powershell启动逻辑,[节点不在-直接cmd][节点在-启动方式-命令在]
        # if "start_type" in conf.options(tool): #tool in conf.sections() and
        #是否添加工具，没有就cmd和title
        if tool in conf.sections():
            #工具存在，是否指定启动类型，没有就普通执行
            if "type" in conf.options(tool):
                print(conf.get(tool, "type"))
                #工具存在，type存在，启动命令是否存在
                if "command" in conf.options(tool):
                    print(conf.get(tool, "command"))  #startCommand
                    startCommand = conf.get(tool, "command")
                    subprocess.Popen(
                        f'start powershell -NoExit "{startCommand}"',
                        shell=True
                    )  #"title {tool}"cd {self.rootPath}\{typedir}\{tool}  默认就是当前的工具路径
                else:
                    subprocess.Popen(f'start powershell -NoExit ', shell=True)
            else:
                startCommand = conf.get(tool, "command")
                subprocess.Popen(
                    f'{startCommand}',
                    shell=True)  #cd {self.rootPath}\{typedir}\{tool} &&
        else:
            # print(conf.options(tool))
            subprocess.Popen(
                f'start cmd /k  "title {tool}"',
                shell=True)  #  cd {self.rootPath}\{typedir}\{tool}
        os.chdir(self.rootPath)
        print(typedir, tool)

        # 参考
        # subprocess.Popen( ' start cmd /k "cd gui_shouji/Packer-Fuzzer-1.3" ' , shell=True)
        # subprocess.Popen(  'start D:\1_tools\8--集成工具\penKitGui\gui_scan'  , shell=True)
        # subprocess.Popen(  ' start powershell -NoExit cd D:\1_tools\8--集成工具\penKitGui\gui_scan\ '  , shell=True)
        # subprocess.Popen(  'start cmd /k " cd gui_scan/403bypasser " '  , shell=True)

    # 读取启动命令配置文件，写入到控件中，并动态生成save按钮，并绑定保存方法
    # 点击编辑启动命令后，修改属性遗忘并添加新按钮，同时保存笔记按钮置为不可点击
    def openStartCommandIniFile(self):  #openStartCommandIniFile
        path = os.path.dirname(os.path.abspath(__file__))
        # print(path)
        path = f"{path}\config\startCommand.ini"  #f"{self.rootPath}\config\startCommand.json"
        print(path)
        global afterTxt
        afterTxt = self.txtCount.get(1.0, END)  #self.txtCount.get(1.0,END)
        with open(path, encoding='utf-8') as f:
            self.txtCount.delete('1.0', END)
            self.txtCount.insert(END, f.read())
            print(f.read())
        self.noteFrameCommandBtn.pack_forget()  # 创建按钮前遗忘--编辑启动命令--
        self.noteFrameTxtSaveBtn['state'] = DISABLED  #点击修改启动按钮时，保存笔记按钮不可点击
        self.noteFrameStyleBtn['state'] = DISABLED  #修改启动命令按钮时样式按钮不可不可点击
        self.saveBtn = ttk.Button(
            self.noteFrame_up,
            text="保存启动命令",
            bootstyle=self.config_style["note"]["startComBtnBootstyle_save"])
        self.saveBtn.pack(anchor=W,
                          side="left",
                          padx=2,
                          pady=2,
                          ipadx=10,
                          ipady=10)
        self.saveBtn[
            COMMAND] = self.saveStartCommandIniFile  #saveStartCommandIniFile
        # return command_ini_data

    # save按钮--保存启动命令：点击保存启动命令按钮后，遗忘自己，并显示编辑启动命令，同时修改
    def saveStartCommandIniFile(self):
        path = os.path.dirname(os.path.abspath(__file__))
        # print(path)
        path = f"{path}\config\startCommand.ini"  #f"{self.rootPath}\config\startCommand.json"
        print(path)
        command_ini_data = self.txtCount.get(1.0, END)
        print(type(command_ini_data))
        self.saveBtn.pack_forget()  #遗忘自己
        self.noteFrameCommandBtn.pack(anchor=W,
                                      side="left",
                                      padx=2,
                                      pady=2,
                                      ipadx=10,
                                      ipady=10)  #编辑启动按钮又显示
        with open(path, "w", encoding='utf-8') as f:
            f.write(command_ini_data)
        # 在保存启动命令后，跳转到之前的工具笔记界面，同时保存笔记按钮恢复点击。
        self.txtCount.delete('1.0', END)
        self.txtCount.insert(END, afterTxt)
        self.noteFrameTxtSaveBtn['state'] = NORMAL  ##点击保存启动命令按钮时，保存笔记按钮不可点击
        self.noteFrameStyleBtn['state'] = NORMAL  #样式按钮还原状态
        # self.noteFrameTxtSaveBtn['state']  = DISABLED  ##点击保存启动命令按钮时，保存笔记按钮不可点击
        # with open(Path,"w",encoding='utf-8') as f:
        #     # 通过configparser库包中的ConfigParser()类，实例化一个对象config对象
        #     conf = configparser.ConfigParser()
        #     conf.write(command_ini_data)
        #     json.dump(command_json_data,f,ensure_ascii=False)
        # self.noteFrameTxtSaveBtn['state']  = NORMAL

    # 读取样式配置文件，写入到控件中，并动态生成save按钮，并绑定保存方法
    # 点击编辑启动命令后，修改属性遗忘并添加新按钮，同时保存笔记按钮置为不可点击
    def openStyleIniFile(self):  #打开样式配置文件
        path = os.path.dirname(os.path.abspath(__file__))
        # print(path)
        path = f"{path}\config\config.ini"  #f"{self.rootPath}\config\startCommand.json"
        # print(path)
        global afterTxt2
        afterTxt2 = self.txtCount.get(1.0, END)  #self.txtCount.get(1.0,END)
        with open(path, encoding='utf-8') as f:
            self.txtCount.delete('1.0', END)
            self.txtCount.insert(END, f.read())
            # print(f.read())
        self.noteFrameStyleBtn.pack_forget()  # 创建按钮前遗忘--样式修改--
        self.noteFrameTxtSaveBtn['state'] = DISABLED  #点击修改启动按钮时，保存笔记按钮不可点击
        self.noteFrameCommandBtn['state'] = DISABLED  #点击修改样式时，修改启动命令按钮不可点击

        self.saveBtn = ttk.Button(
            self.noteFrame_up,
            text="样式保存",
            bootstyle=self.config_style["note"]["styleBtnBootstyle_save"])
        self.saveBtn.pack(anchor=W,
                          side="right",
                          padx=2,
                          pady=2,
                          ipadx=10,
                          ipady=10)
        self.saveBtn[
            COMMAND] = self.saveStyleIniFile  #saveStartCommandIniFile
        # return command_ini_data

    # save按钮--保存启动命令：点击保存启动命令按钮后，遗忘自己，并显示编辑启动命令，同时修改
    def saveStyleIniFile(self):
        path = os.path.dirname(os.path.abspath(__file__))
        # print(path)
        path = f"{path}\config\config.ini"  #f"{self.rootPath}\config\startCommand.json"
        # print(path)
        command_ini_data = self.txtCount.get(1.0, END)
        # print(type(command_ini_data))
        self.saveBtn.pack_forget()  #遗忘自己
        self.noteFrameStyleBtn.pack(anchor=W,
                                      side="right",
                                      padx=2,
                                      pady=2,
                                      ipadx=10,
                                      ipady=10)  #编辑启动按钮又显示
        with open(path, "w", encoding='utf-8') as f:
            f.write(command_ini_data)
        # 在保存启动命令后，跳转到之前的工具笔记界面，同时保存笔记按钮恢复点击。
        self.txtCount.delete('1.0', END)
        self.txtCount.insert(END, afterTxt2)
        self.noteFrameTxtSaveBtn['state'] = NORMAL  ##点击保存启动命令按钮时，保存笔记按钮不可点击
        self.noteFrameCommandBtn['state'] = NORMAL  #恢复笔记按钮状态 

        # 刷新gui，先清除再生成。
    def refresh(self):
        self.toolsDic = tools_dict.toolsDir()
        # print(self.toolsDic)
        for widget in self.toolFrame.winfo_children():
            widget.destroy()
        self.toolFrameFun()

    # 工具框架中的上面的按钮，--功能拓展，传入的是具有特定意义的目录标识,相当于带参数的刷新按钮
    def toolFunBtn(self, typeMark):
        # self.Btnfr1['bootstyle'] = self.config_style["tool"]["funBtnBootstyle_click"]  
        self.toolsDic = tools_dict.toolsDir(typeMark)
        # print(self.toolsDic)
        for widget in self.toolFrame.winfo_children():
            widget.destroy()
        self.toolFrameFun()


# 读取style ini 配置，类外部引用conf_style，不是类内部self.config_style
styleIniPath = os.path.dirname(os.path.abspath(__file__))  #获取本py文件的所在目录（父目录）
styleIniPath = f"{styleIniPath}\config\config.ini"  # 拼接路径，获取style ini 文件路径
print("config.ini文件的路径是：", styleIniPath)
conf_style = configparser.ConfigParser()  #下面是读取文件
conf_style.read(filenames=styleIniPath,
                encoding="utf-8")  #注意编码，读取config ini 配置

# enable_high_dpi_awareness()  #启动高dpi
root = ttk.Window(title=conf_style["app"]["title"],
                  themename=str(conf_style["app"]["theme"]))  #darkly   morph

# 获取屏幕大小,方便调试
screenheight = root.winfo_screenheight()  #屏幕高
screenwidth = root.winfo_screenwidth()  #屏幕宽
print("  屏幕的-宽-高-是 (in pixels) =  ", (screenwidth, screenheight))
#screen Depth
screendepth = root.winfo_screendepth()
print("  屏幕的深度是 =", screendepth)

# 设置工具位置，大小，设置宽高，居中，注意ini中的数字是str
size_w = conf_style["app"]["size_w"]  #设置工具的宽，注意是str
size_h = conf_style["app"]["size_h"]  #设置工具的高,注意是str
# print(size_w, size_h,type(size_w),type(size_h))
center_w = int((screenwidth - int(size_w)) / 2)  #计算居中的左边距
center_h = int((screenheight - int(size_h)) / 2)  #计算居中的上边距
print("工具的位置参数信息：宽-高-左边距-上边距:", size_w, size_h, center_w, center_h)
root.geometry(f'{size_w}x{size_h}+{center_w}+{center_h}')  # 设置工具的位置，大小

root.iconbitmap('logo.ico')  #工具的logo引用
app = APP(master=root)  #创建实例

root.mainloop()  #循环