#!/usr/bin/python3
# coding=utf-8

import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledText, ScrolledFrame
from ttkbootstrap.dialogs.dialogs import Messagebox
import subprocess
import configparser  # 导入内置的模块

import os
import datetime

import tools_dict
from config import mark


class APP(ttk.Frame):

    # 界面的主要构建代码，框架，组件等
    def __init__(self, master=None):
        self.rootPath = tools_dict.tools_root_path()
        self.toolsDic = tools_dict.toolsDir()
        # self.startCommandDict = self.openStartCommandIniFile()  #name:command

        super().__init__(master)
        self.master = master
        self.pack()

        # 工具框架-容器，
        self.toolFra = ttk.LabelFrame(self,
                                    text=mark.toolFrameText,
                                    bootstyle=mark.toolFrameBootstyle,
                                    width=mark.toolFrameWidth,
                                    height=mark.toolFrameHeight,
                                    labelanchor=NW,
                                    padding=7,
                                    border=10)
        self.toolFra.pack(side="left",
                        fill=BOTH
                        ipadx=7,
                        ipady=10,
                        padx=10,
                        pady=20)  #expand=True
        self.toolFrame = ScrolledFrame(
            self.toolFra,
            autohide=True,
            width=mark.toolFrameWidth,
            height=mark.toolFrameHeight + 500,
            bootstyle=mark.toolFrameBootstyle_Scrolled
        )  #bootstyle='danger-round
        self.toolFrame.pack(fill=BOTH, anchor=NW)

        # 笔记框架-容器
        self.noteFrame = ttk.LabelFrame(self,
                                        text="Note",
                                        bootstyle=mark.noteFrameBootstyle,
                                        width=mark.noteFrameWidth,
                                        height=mark.noteFrameHeight,
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

        # 笔记框架内部分配：上面添加一个功能框架
        self.noteFrame_up = ttk.Frame(
            self.noteFrame, bootstyle=mark.noteFrameUpFraBootstyle)  #可以调颜色
        self.noteFrame_up.pack(side="top", fill="x", ipadx=7, ipady=10)

        # 20230109删除
        # self.noteFrameToolLabel = ttk.Label(
        #     self.noteFrame_up,
        #     text="  查看笔记：--toolInfo--  ",
        #     bootstyle=mark.noteFrameFunBtnBootstyle)
        # self.noteFrameToolLabel.pack(anchor=W,
        #                              side="left",
        #                              padx=5,
        #                              pady=5,
        #                              ipadx=10,
        #                              ipady=10)

        self.noteFrameTxtSaveBtn = ttk.Button(
            self.noteFrame_up,
            text=" 保存笔记 ",
            bootstyle=mark.noteFrameFunBtnBootstyle)  # ,width=10
        self.noteFrameTxtSaveBtn.pack(anchor=W,
                                    padx=5,
                                    pady=5,
                                    ipadx=10,
                                    side="left",
                                    ipady=10)
        self.noteFrameStartBtn = ttk.Button(
            self.noteFrame_up,
            text=" 打开目录 ",
            bootstyle=mark.noteFrameFunBtnBootstyle)  #,width=10
        self.noteFrameStartBtn.pack(anchor=W,
                                    side="left",
                                    padx=5,
                                    pady=5,
                                    ipadx=10,
                                    ipady=10)

        self.noteFrameRefreshBtn = ttk.Button(
            self.noteFrame_up,
            text=" 刷新GUI ",
            bootstyle=mark.noteFrameFunBtnBootstyle
        )  #,width=10  ,command=self.refreshWin
        self.noteFrameRefreshBtn.pack(anchor=W,
                                    side="left",
                                    padx=5,
                                    pady=5,
                                    ipadx=10,
                                    ipady=10)  #side=CENTER
        self.noteFrameRefreshBtn["command"] = self.refresh  #  手动刷新工具界面方法

        self.noteFrameOpenDirBtn = ttk.Button(
            self.noteFrame_up,
            text=" 启动工具 ",
            bootstyle=mark.noteFrameFunBtnBootstyle)  #,width=10
        self.noteFrameOpenDirBtn.pack(anchor=W,
                                    side="left",
                                    padx=5,
                                    pady=5,
                                    ipadx=10,
                                    ipady=10)

        self.noteFrameCommandBtn = ttk.Button(
            self.noteFrame_up,
            text=" 编辑启动命令 ",
            bootstyle=mark.noteFrameFunBtnBootstyle2)  #,width=10
        self.noteFrameCommandBtn.pack(anchor=W,
                                    side="left",
                                    padx=5,
                                    pady=5,
                                    ipadx=10,
                                    ipady=10)  #side=CENTER
        self.noteFrameCommandBtn[COMMAND] = self.openStartCommandIniFile

        # 笔记框架内部分配：-嵌套
        self.noteFrame_down = ttk.LabelFrame(self.noteFrame,
                                            text=mark.noteFrameDownTxt,
                                            style=mark.noteFrameDownStyle,
                                            padding=5)
        self.noteFrame_down.pack(fill=BOTH, padx=3, pady=3)

        self.txtCount = ScrolledText(self.noteFrame_down,
                                    width=mark.noteFrameWidth,
                                    height=mark.noteFrameHeight,
                                    bootstyle=mark.noteFrameDownScrolled,
                                    autohide=True)
        self.txtCount.pack(fill=BOTH, side=BOTTOM, anchor=NW)

        # 框架生成方法，界面构建，即是左边的工具布局，同时也包含了右边的一些事件，代码等
        self.toolFrameFun()

    # 左边工具布局
    def toolFrameFun(self):
        # 调试信息，结合mark.py修改配置，涉及分辨率问题需要参考这里
        print("总宽-工具宽-笔记宽-工具列宽:  ", mark.appWidth, mark.toolFrameWidth,
            mark.noteFrameWidth, mark.toolFrameToolColumnWidth)
        print("总高-工具高-笔记高:  ", mark.appHeight, mark.toolFrameHeight,
            mark.noteFrameHeight)
        for i in range(mark.toolColumn):
            self.Btnfr1 = ttk.Button(
                self.toolFrame,
                text=mark.after,
                width=mark.toolFrameToolColumnWidth,
                bootstyle=mark.noteFrameFunBtnBootstyle).grid(
                    pady=5, row=0, column=i)  #,state="disabled"
        r = 1
        # 工具类别
        for k in self.toolsDic.keys():
            self.btnToolType = ttk.Button(
                self.toolFrame,
                text=k,
                bootstyle=mark.toolTypeBootstyle,
                command=lambda a=k:
                [self.openToolTypeNote(a),
                self.toolTypeTitle(a)])
            self.btnToolType.grid(row=r,
                                column=0,
                                columnspan=mark.toolColumn,
                                sticky=W)
            self.btnToolType.bind("<Double-Button-1>",
                                  lambda event, arg0=k: self.openTypeDir(arg0))

            r += 1
            c = 0
            # 详细工具
            for i in self.toolsDic[k]:
                if c == mark.toolColumn:
                    r += 1
                    c = 0
                self.btnTools = ttk.Button(
                    self.toolFrame,
                    bootstyle=mark.toolBtnBootstyle,
                    text=i,
                    command=lambda a=k, b=i:
                    [self.openToolNote(a, b),
                    self.toolTitle(a, b)])
                self.btnTools.grid(row=r, column=c, sticky=N + S + W, pady=2)
                self.btnTools.bind(
                    "<Double-Button-1>",
                    lambda event, arg1=k, arg2=i: self.openToolDir(arg1, arg2))
                self.btnTools.bind(
                    "<ButtonPress-3>",
                    lambda event, arg1=k, arg2=i: self.openToolCmd(arg1, arg2))

                c += 1
            r += 1

    # 笔记框架中的上面的框架信息显示--工具类型--框架重构和里面的控件绑定方法
    def toolTypeTitle(self, typedir):
        for widget in self.noteFrame_up.winfo_children():
            widget.destroy()

        # 创建布局，工具信息，笔记保存, 和 1209 优化：启动工具，打开目录按钮, 启动工具命令的快速添加
        # 20230109修改----删除
        # self.text1 = f'--{typedir}--'

        # self.noteFrameToolLabel = ttk.Label(
        #     self.noteFrame_up,
        #     text=self.text1,
        #     bootstyle=mark.noteFrameFunBtnBootstyle)
        # self.noteFrameToolLabel.pack(anchor=W,
        #                              side="left",
        #                              padx=10,
        #                              pady=10,
        #                              ipadx=10,
        #                              ipady=10)

        self.noteFrameTxtSaveBtn = ttk.Button(
            self.noteFrame_up,
            text=" 保存笔记 ",
            bootstyle=mark.noteFrameFunBtnBootstyle,
            command=lambda a=typedir: self.saveTypeNote(a))
        self.noteFrameTxtSaveBtn.pack(anchor=W,
                                    side="left",
                                    padx=5,
                                    pady=5,
                                    ipadx=10,
                                    ipady=10)

        self.noteFrameStartBtn = ttk.Button(
            self.noteFrame_up,
            text=" 打开目录 ",
            bootstyle=mark.noteFrameFunBtnBootstyle)  #,width=10
        self.noteFrameStartBtn.pack(anchor=W,
                                    side="left",
                                    padx=5,
                                    pady=5,
                                    ipadx=10,
                                    ipady=10)
        self.noteFrameStartBtn[
            COMMAND] = lambda arg0=typedir: self.openTypeDir(arg0)

        self.noteFrameRefreshBtn = ttk.Button(
            self.noteFrame_up,
            text=" 刷新GUI ",
            bootstyle=mark.noteFrameFunBtnBootstyle)  #,width=10
        self.noteFrameRefreshBtn.pack(anchor=W,
                                      side="left",
                                      padx=5,
                                      pady=5,
                                      ipadx=10,
                                      ipady=10)  #side=CENTER
        self.noteFrameRefreshBtn["command"] = self.refresh

        self.noteFrameOpenDirBtn = ttk.Button(
            self.noteFrame_up,
            text=" 启动工具 ",
            bootstyle=mark.noteFrameFunBtnBootstyle
        )  #,width=10  ,state=DISABLED
        self.noteFrameOpenDirBtn.pack(anchor=W,
                                      side="left",
                                      padx=5,
                                      pady=5,
                                      ipadx=10,
                                      ipady=10)

        self.noteFrameCommandBtn = ttk.Button(
            self.noteFrame_up,
            text=" 编辑启动命令 ",
            bootstyle=mark.noteFrameFunBtnBootstyle2
        )  #,width=10   ,state=DISABLED
        self.noteFrameCommandBtn.pack(anchor=W,
                                      side="left",
                                      padx=5,
                                      pady=5,
                                      ipadx=10,
                                      ipady=10)  #side=CENTER
        self.noteFrameCommandBtn[COMMAND] = self.openStartCommandIniFile

    # 笔记框架中的上面的框架信息显示--具体工具--框架重构和里面的控件绑定方法
    def toolTitle(self, typedir, tool):
        for widget in self.noteFrame_up.winfo_children():
            widget.destroy()
        # 20230109修改，删除不显示
        # self.text1 = f'--{typedir}--{tool}--'

        # self.noteFrameToolLabel = ttk.Label(
        #     self.noteFrame_up,
        #     text=self.text1,
        #     bootstyle=mark.noteFrameFunBtnBootstyle)
        # self.noteFrameToolLabel.pack(anchor=W,
        #                              side="left",
        #                              padx=10,
        #                              pady=10,
        #                              ipadx=10,
        #                              ipady=10)

        self.noteFrameTxtSaveBtn = ttk.Button(
            self.noteFrame_up,
            text=" 保存笔记 ",
            bootstyle=mark.noteFrameFunBtnBootstyle,
            command=lambda a=typedir, b=tool: self.saveToolNote(
                a, b))  #,width = 20
        self.noteFrameTxtSaveBtn.pack(anchor=W,
                                      side="left",
                                      padx=5,
                                      pady=5,
                                      ipadx=10,
                                      ipady=10)

        self.noteFrameStartBtn = ttk.Button(
            self.noteFrame_up,
            text=" 打开目录 ",
            bootstyle=mark.noteFrameFunBtnBootstyle)  #,width=10
        self.noteFrameStartBtn.pack(anchor=W,
                                    side="left",
                                    padx=5,
                                    pady=5,
                                    ipadx=10,
                                    ipady=10)
        self.noteFrameStartBtn[
            COMMAND] = lambda arg1=typedir, arg2=tool: self.openToolDir(
                arg1, arg2)

        self.noteFrameRefreshBtn = ttk.Button(
            self.noteFrame_up,
            text=" 刷新GUI ",
            bootstyle=mark.noteFrameFunBtnBootstyle)  #,width=10
        self.noteFrameRefreshBtn.pack(anchor=W,
                                      side="left",
                                      padx=5,
                                      pady=5,
                                      ipadx=10,
                                      ipady=10)  #side=CENTER
        self.noteFrameRefreshBtn["command"] = self.refresh

        self.noteFrameOpenDirBtn = ttk.Button(
            self.noteFrame_up,
            text=" 启动工具 ",
            bootstyle=mark.noteFrameFunBtnBootstyle)  #,width=10
        self.noteFrameOpenDirBtn.pack(anchor=W,
                                      side="left",
                                      padx=5,
                                      pady=5,
                                      ipadx=10,
                                      ipady=10)
        self.noteFrameOpenDirBtn[
            COMMAND] = lambda arg1=typedir, arg2=tool: self.openToolCmd(
                arg1, arg2)

        self.noteFrameCommandBtn = ttk.Button(
            self.noteFrame_up,
            text=" 编辑启动命令 ",
            bootstyle=mark.noteFrameFunBtnBootstyle2)  #,width=10
        self.noteFrameCommandBtn.pack(anchor=W,
                                      side="left",
                                      padx=5,
                                      pady=5,
                                      ipadx=10,
                                      ipady=10)  #side=CENTER
        self.noteFrameCommandBtn[COMMAND] = self.openStartCommandIniFile

    # 保存笔记-工具类型的笔记
    def saveTypeNote(self, typedir):
        notePath = f"{self.rootPath}\{typedir}\{mark.toolNoteMark}"
        content = self.txtCount.get(1.0, END)
        with open(notePath, "w", encoding='utf-8') as f:
            f.write(content)

    # 保存笔记-工具的笔记
    def saveToolNote(self, typedir, tool):
        notePath = f"{self.rootPath}\{typedir}\{tool}\{mark.toolNoteMark}"
        content = self.txtCount.get(1.0, END)
        with open(notePath, "w", encoding='utf-8') as f:
            f.write(content)

    # 打开笔记-工具的笔记
    def openToolNote(self, typedir, tool):
        notePath = f"{self.rootPath}\{typedir}\{tool}\{mark.toolNoteMark}"

        self.noteFrame_down["text"] = f"-- {self.rootPath}\{typedir}\{tool} --"
        if os.path.exists(notePath):
            with open(notePath, encoding='utf-8') as f:
                self.txtCount.delete('1.0', END)
                self.txtCount.insert(END, f.read())
        else:
            Messagebox.ok(message="\n\t你还没有创建笔记，已自动创建初始化信息。\t\n",
                          title='OpenNote')  #,position=(mark.x,mark.y)
            infoMsg = f"-----你还没有创建笔记-----{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}-----"
            self.txtCount.delete('1.0', END)
            self.txtCount.insert(END, infoMsg)
            f = open(notePath, "w", encoding='utf-8')
            f.writelines(infoMsg)
            f.close()

    # 打开笔记-工具类型的笔记
    def openToolTypeNote(self, typedir):
        notePath = f"{self.rootPath}\{typedir}\{mark.toolNoteMark}"

        self.noteFrame_down["text"] = f"-- {self.rootPath}\{typedir} --"

        if os.path.exists(notePath):
            with open(notePath, encoding='utf-8') as f:
                self.txtCount.delete('1.0', END)
                self.txtCount.insert(END, f.read())

        else:
            Messagebox.ok(message="\n\t你还没有创建笔记，已自动创建初始化信息。\t\n",
                          title='OpenNote')  #,position=(mark.x,mark.y)
            infoMsg = f"-----你还没有创建笔记-----{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}-----"
            self.txtCount.delete('1.0', END)
            self.txtCount.insert(END, infoMsg)
            f = open(notePath, "w", encoding='utf-8')
            f.writelines(infoMsg)
            f.close()

    # 打开目录--工具类型
    def openTypeDir(self, typedir):
        os.startfile(f'{self.rootPath}\{typedir}')

    # 打开目录--具体工具
    def openToolDir(self, typedir, tool):
        os.startfile(f'{self.rootPath}\{typedir}\{tool}')

    # 启动逻辑实现
    def openToolCmd(self, typedir, tool):
        os.chdir(f"{self.rootPath}\{typedir}\{tool}")

        iniPath = os.path.dirname(os.path.abspath(__file__))

        iniPath = f"{iniPath}\config\startCommand.ini"
        conf = configparser.ConfigParser()
        conf.read(filenames=iniPath, encoding="utf-8")

        if tool in conf.sections():

            if "type" in conf.options(tool):
                print(conf.get(tool, "type"))

                if "command" in conf.options(tool):
                    print(conf.get(tool, "command"))  #startCommand
                    startCommand = conf.get(tool, "command")
                    subprocess.Popen(
                        f'start powershell -NoExit "{startCommand}"',
                        shell=True)
                else:
                    subprocess.Popen(f'start powershell -NoExit ', shell=True)
            else:
                startCommand = conf.get(tool, "command")
                subprocess.Popen(f'{startCommand}', shell=True)

        else:
            # print(conf.options(tool))
            subprocess.Popen(
                f'start cmd /k  "title {tool}"',
                shell=True)  #  cd {self.rootPath}\{typedir}\{tool}
        os.chdir(self.rootPath)
        print(typedir, tool)

    # 读取启动命令配置文件，并动态生成save按钮，并绑定保存方法
    # 点击编辑启动命令后，修改属性，并添加新按钮，同时设置笔记按钮置为不可点击
    def openStartCommandIniFile(self):
        path = os.path.dirname(os.path.abspath(__file__))
        # print(path)
        path = f"{path}\config\startCommand.ini"
        print(path)
        global afterTxt
        afterTxt = self.txtCount.get(1.0, END)
        with open(path, encoding='utf-8') as f:
            self.txtCount.delete('1.0', END)
            self.txtCount.insert(END, f.read())
            print(f.read())
        self.noteFrameCommandBtn.pack_forget()
        self.noteFrameTxtSaveBtn['state'] = DISABLED
        self.saveBtn = ttk.Button(self.noteFrame_up,
                                  text="保存启动命令",
                                  bootstyle=mark.noteFrameFunBtnBootstyle3)
        self.saveBtn.pack(anchor=W,
                          side=RIGHT,
                          padx=5,
                          pady=5,
                          ipadx=10,
                          ipady=10)
        self.saveBtn[
            COMMAND] = self.saveStartCommandIniFile  #saveStartCommandIniFile

    # save按钮--保存启动命令：点击保存启动命令按钮后，修改属性，并显示编辑启动命令
    def saveStartCommandIniFile(self):
        path = os.path.dirname(os.path.abspath(__file__))
        # print(path)
        path = f"{path}\config\startCommand.ini"
        print(path)
        command_ini_data = self.txtCount.get(1.0, END)
        print(type(command_ini_data))
        self.saveBtn.pack_forget()
        self.noteFrameCommandBtn.pack(anchor=W,
                                      side="left",
                                      padx=5,
                                      pady=5,
                                      ipadx=10,
                                      ipady=10)
        with open(path, "w", encoding='utf-8') as f:
            f.write(command_ini_data)

        self.txtCount.delete('1.0', END)
        self.txtCount.insert(END, afterTxt)
        self.noteFrameTxtSaveBtn['state'] = NORMAL

    def refresh(self):
        self.toolsDic = tools_dict.toolsDir()
        # print(self.toolsDic)
        for widget in self.toolFrame.winfo_children():
            widget.destroy()
        self.toolFrameFun()


# enable_high_dpi_awareness()  #启动高dpi
root = ttk.Window(title=mark.appTitle,
                  themename=mark.appThemename)  #darkly   morph
root.geometry(f'{mark.appWidth}x{mark.appHeight}+{mark.appScree}')
root.iconbitmap('logo.ico')
app = APP(master=root)

root.mainloop()