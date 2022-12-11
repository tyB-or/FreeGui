import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledText, ScrolledFrame
from ttkbootstrap.dialogs.dialogs import Messagebox
import subprocess
import json

import configparser

import os
import datetime

import tools_dict
from config import mark


class APP(ttk.Frame):

    def __init__(self, master=None):
        self.rootPath = tools_dict.tools_root_path()
        self.toolsDic = tools_dict.toolsDir()

        super().__init__(master)
        self.master = master
        self.pack()

        self.height = mark.height
        self.width = mark.width

        self.toolFra = ttk.LabelFrame(self,
                                      text="工具导航-ToolsGui",
                                      bootstyle=PRIMARY,
                                      width=self.width / 2,
                                      height=self.height,
                                      labelanchor=NW,
                                      padding=7,
                                      border=10)
        self.toolFra.pack(side="left",
                          fill=BOTH,
                          ipadx=7,
                          ipady=10,
                          padx=10,
                          pady=20,
                          expand=True)
        self.toolFrame = ScrolledFrame(self.toolFra,
                                       autohide=True,
                                       width=1100,
                                       height=2500,
                                       bootstyle="round")
        self.toolFrame.pack(fill=BOTH, anchor=NW)

        self.noteFrame = ttk.LabelFrame(self,
                                        text="Note",
                                        bootstyle=PRIMARY,
                                        width=self.width / 2,
                                        height=self.height,
                                        labelanchor=NW,
                                        padding=7,
                                        border=10)
        self.noteFrame.pack(side="right",
                            fill=BOTH,
                            ipadx=7,
                            ipady=10,
                            padx=10,
                            pady=20,
                            expand=True)

        self.noteFrame_up = ttk.Frame(self.noteFrame, bootstyle=PRIMARY)
        self.noteFrame_up.pack(side="top", fill="x", ipadx=7, ipady=10)

        self.nootFrameToolLabel = ttk.Label(self.noteFrame_up,
                                            text="  查看笔记：--toolInfo--  ",
                                            bootstyle="success")
        self.nootFrameToolLabel.pack(anchor=W,
                                     side="left",
                                     padx=5,
                                     pady=5,
                                     ipadx=10,
                                     ipady=10)

        self.nootFrameTxtSaveBtn = ttk.Button(self.noteFrame_up,
                                              text=" 保存笔记 ",
                                              bootstyle="success")
        self.nootFrameTxtSaveBtn.pack(anchor=W,
                                      side=RIGHT,
                                      padx=5,
                                      pady=5,
                                      ipadx=10,
                                      ipady=10)

        self.nootFrameStartBtn = ttk.Button(self.noteFrame_up,
                                            text=" 打开目录 ",
                                            bootstyle="success")
        self.nootFrameStartBtn.pack(anchor=W,
                                    side=RIGHT,
                                    padx=5,
                                    pady=5,
                                    ipadx=10,
                                    ipady=10)

        self.nootFrameOpenDirBtn = ttk.Button(self.noteFrame_up,
                                              text=" 启动工具 ",
                                              bootstyle="success")
        self.nootFrameOpenDirBtn.pack(anchor=W,
                                      side=RIGHT,
                                      padx=5,
                                      pady=5,
                                      ipadx=10,
                                      ipady=10)

        self.nootFrameCommandBtn = ttk.Button(self.noteFrame_up,
                                              text=" 编辑启动命令 ",
                                              bootstyle="info")
        self.nootFrameCommandBtn.pack(anchor=W,
                                      side=RIGHT,
                                      padx=5,
                                      pady=5,
                                      ipadx=10,
                                      ipady=10)
        self.nootFrameCommandBtn[COMMAND] = self.openStartCommandIniFile

        self.noteFrame_down = ttk.LabelFrame(self.noteFrame,
                                             text=" --Content--  ",
                                             style=SUCCESS,
                                             padding=5)
        self.noteFrame_down.pack(fill=BOTH, padx=3, pady=3)

        self.txtCount = ScrolledText(self.noteFrame_down,
                                     width=1200,
                                     height=1000,
                                     bootstyle='success-round',
                                     autohide=True)
        self.txtCount.pack(fill=BOTH, side=BOTTOM, anchor=NW)

        self.toolFrameFun()

    def toolFrameFun(self):
        r = 0

        for k in self.toolsDic.keys():
            self.btnToolType = ttk.Button(
                self.toolFrame,
                text=k,
                width=20,
                bootstyle="danger-outline",
                command=lambda a=k:
                [self.openToolTypeNote(a),
                 self.toolTypeTitle(a)])
            self.btnToolType.grid(row=r, column=0, columnspan=5, sticky=W)

            self.btnToolType.bind("<ButtonPress-3>",
                                  lambda event, arg0=k: self.openTypeDir(arg0))
            r += 1
            c = 0

            for i in self.toolsDic[k]:
                if c == 5:
                    r += 1
                    c = 0
                self.btnTools = ttk.Button(
                    self.toolFrame,
                    bootstyle="dark-link",
                    text=i,
                    width=16,
                    command=lambda a=k, b=i:
                    [self.openToolNote(a, b),
                     self.toolTitle(a, b)])

                self.btnTools.grid(row=r, column=c, sticky=N + S + W, pady=2)

                self.btnTools.bind(
                    "<ButtonPress-3>",
                    lambda event, arg1=k, arg2=i: self.openToolDir(arg1, arg2))

                self.btnTools.bind(
                    "<Double-Button-1>",
                    lambda event, arg1=k, arg2=i: self.openToolCmd(arg1, arg2))
                c += 1
            r += 1

    def toolTypeTitle(self, typedir):

        for widget in self.noteFrame_up.winfo_children():
            widget.destroy()

        self.text1 = f'--{typedir}--'

        self.nootFrameToolLabel = ttk.Label(self.noteFrame_up,
                                            text=self.text1,
                                            bootstyle="success")
        self.nootFrameToolLabel.pack(anchor=W,
                                     side="left",
                                     padx=10,
                                     pady=10,
                                     ipadx=10,
                                     ipady=10)

        self.nootFrameTxtSaveBtn = ttk.Button(
            self.noteFrame_up,
            text=" 保存笔记 ",
            bootstyle="success",
            command=lambda a=typedir: self.saveTypeNote(a))
        self.nootFrameTxtSaveBtn.pack(anchor=W,
                                      side=RIGHT,
                                      padx=5,
                                      pady=5,
                                      ipadx=10,
                                      ipady=10)

        self.nootFrameStartBtn = ttk.Button(self.noteFrame_up,
                                            text=" 打开目录 ",
                                            bootstyle="success")
        self.nootFrameStartBtn.pack(anchor=W,
                                    side=RIGHT,
                                    padx=5,
                                    pady=5,
                                    ipadx=10,
                                    ipady=10)
        self.nootFrameStartBtn[
            COMMAND] = lambda arg0=typedir: self.openTypeDir(arg0)

        self.nootFrameOpenDirBtn = ttk.Button(self.noteFrame_up,
                                              text=" 启动工具 ",
                                              bootstyle="success",
                                              state=DISABLED)
        self.nootFrameOpenDirBtn.pack(anchor=W,
                                      side=RIGHT,
                                      padx=5,
                                      pady=5,
                                      ipadx=10,
                                      ipady=10)

        self.nootFrameCommandBtn = ttk.Button(self.noteFrame_up,
                                              text=" 编辑启动命令 ",
                                              bootstyle="success",
                                              state=DISABLED)
        self.nootFrameCommandBtn.pack(anchor=W,
                                      side=RIGHT,
                                      padx=5,
                                      pady=5,
                                      ipadx=10,
                                      ipady=10)

    def toolTitle(self, typedir, tool):

        for widget in self.noteFrame_up.winfo_children():
            widget.destroy()

        self.text1 = f'--{typedir}--{tool}--'

        self.nootFrameToolLabel = ttk.Label(self.noteFrame_up,
                                            text=self.text1,
                                            bootstyle="success")
        self.nootFrameToolLabel.pack(anchor=W,
                                     side="left",
                                     padx=10,
                                     pady=10,
                                     ipadx=10,
                                     ipady=10)

        self.nootFrameTxtSaveBtn = ttk.Button(
            self.noteFrame_up,
            text=" 保存笔记 ",
            bootstyle="success",
            command=lambda a=typedir, b=tool: self.saveToolNote(a, b))
        self.nootFrameTxtSaveBtn.pack(anchor=W,
                                      side=RIGHT,
                                      padx=5,
                                      pady=5,
                                      ipadx=10,
                                      ipady=10)

        self.nootFrameStartBtn = ttk.Button(self.noteFrame_up,
                                            text=" 打开目录 ",
                                            bootstyle="success")
        self.nootFrameStartBtn.pack(anchor=W,
                                    side=RIGHT,
                                    padx=5,
                                    pady=5,
                                    ipadx=10,
                                    ipady=10)
        self.nootFrameStartBtn[
            COMMAND] = lambda arg1=typedir, arg2=tool: self.openToolDir(
                arg1, arg2)

        self.nootFrameOpenDirBtn = ttk.Button(self.noteFrame_up,
                                              text=" 启动工具 ",
                                              bootstyle="success")
        self.nootFrameOpenDirBtn.pack(anchor=W,
                                      side=RIGHT,
                                      padx=5,
                                      pady=5,
                                      ipadx=10,
                                      ipady=10)
        self.nootFrameOpenDirBtn[
            COMMAND] = lambda arg1=typedir, arg2=tool: self.openToolCmd(
                arg1, arg2)

        self.nootFrameCommandBtn = ttk.Button(self.noteFrame_up,
                                              text=" 编辑启动命令 ",
                                              bootstyle="info")
        self.nootFrameCommandBtn.pack(anchor=W,
                                      side=RIGHT,
                                      padx=5,
                                      pady=5,
                                      ipadx=10,
                                      ipady=10)
        self.nootFrameCommandBtn[COMMAND] = self.openStartCommandIniFile

    def saveTypeNote(self, typedir):
        notePath = f"{self.rootPath}\{typedir}\{mark.toolNoteMark}"

        content = self.txtCount.get(1.0, END)
        with open(notePath, "w", encoding='utf-8') as f:
            f.write(content)

    def saveToolNote(self, typedir, tool):
        notePath = f"{self.rootPath}\{typedir}\{tool}\{mark.toolNoteMark}"

        content = self.txtCount.get(1.0, END)
        with open(notePath, "w", encoding='utf-8') as f:
            f.write(content)

    def openToolNote(self, typedir, tool):
        notePath = f"{self.rootPath}\{typedir}\{tool}\{mark.toolNoteMark}"

        if os.path.exists(notePath):
            with open(notePath, encoding='utf-8') as f:
                self.txtCount.delete('1.0', END)
                self.txtCount.insert(END, f.read())

        else:
            Messagebox.ok(message="\n\t你还没有创建笔记，已自动创建初始化信息。\t\n",
                          title='OpenNote',
                          position=(mark.x, mark.y))
            infoMsg = f"-----你还没有创建笔记-----{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}-----"
            self.txtCount.delete('1.0', END)
            self.txtCount.insert(END, infoMsg)
            f = open(notePath, "w", encoding='utf-8')
            f.writelines(infoMsg)
            f.close()

    def openToolTypeNote(self, typedir):
        notePath = f"{self.rootPath}\{typedir}\{mark.toolNoteMark}"

        if os.path.exists(notePath):
            with open(notePath, encoding='utf-8') as f:
                self.txtCount.delete('1.0', END)
                self.txtCount.insert(END, f.read())

        else:
            Messagebox.ok(message="\n\t你还没有创建笔记，已自动创建初始化信息。\t\n",
                          title='OpenNote',
                          position=(mark.x, mark.y))
            infoMsg = f"-----你还没有创建笔记-----{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}-----"
            self.txtCount.delete('1.0', END)
            self.txtCount.insert(END, infoMsg)
            f = open(notePath, "w", encoding='utf-8')
            f.writelines(infoMsg)
            f.close()

    def openTypeDir(self, typedir):
        os.startfile(f'{self.rootPath}\{typedir}')

    def openToolDir(self, typedir, tool):
        os.startfile(f'{self.rootPath}\{typedir}\{tool}')

    def openToolCmd(self, typedir, tool):
        os.chdir(f"{self.rootPath}\{typedir}\{tool}")

        iniPath = os.path.dirname(os.path.abspath(__file__))

        iniPath = f"{iniPath}\config\startCommand.ini"
        conf = configparser.ConfigParser()
        conf.read(filenames=iniPath, encoding="utf-8")
        if tool in conf.sections():
            startCommand = conf.get(tool, "startCommand")
            subprocess.Popen(
                f'cd {self.rootPath}\{typedir}\{tool} && {startCommand}',
                shell=True)

        else:
            subprocess.Popen(f'start cmd /k  "title {tool}"', shell=True)
        os.chdir(self.rootPath)

        print(typedir, tool)

    def openStartCommandIniFile(self):
        path = os.path.dirname(os.path.abspath(__file__))

        path = f"{path}\config\startCommand.ini"
        print(path)
        with open(path, encoding='utf-8') as f:
            self.txtCount.delete('1.0', END)
            self.txtCount.insert(END, f.read())
            print(f.read())

        self.nootFrameCommandBtn.pack_forget()
        self.nootFrameTxtSaveBtn['state'] = DISABLED
        self.saveBtn = ttk.Button(self.noteFrame_up,
                                  text="保存启动命令",
                                  bootstyle="info")
        self.saveBtn.pack(anchor=W,
                          side=RIGHT,
                          padx=5,
                          pady=5,
                          ipadx=10,
                          ipady=10)
        self.saveBtn[COMMAND] = self.saveStartCommandIniFile

    def saveStartCommandIniFile(self):
        path = os.path.dirname(os.path.abspath(__file__))

        path = f"{path}\config\startCommand.ini"
        print(path)
        command_ini_data = self.txtCount.get(1.0, END)
        print(type(command_ini_data))
        self.saveBtn.pack_forget()

        self.nootFrameCommandBtn.pack(anchor=W,
                                      side=RIGHT,
                                      padx=5,
                                      pady=5,
                                      ipadx=10,
                                      ipady=10)
        with open(path, "w", encoding='utf-8') as f:
            f.write(command_ini_data)


root = ttk.Window(title="TOOLS_GUI    一款可以自己更新的工具箱__v1.0    by：tyb",
                  themename="morph")
root.geometry(f'{mark.width}x{mark.height}+{mark.scree}')
root.iconbitmap('logo.ico')
app = APP(master=root)

root.mainloop()