


import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from ttkbootstrap.scrolled import ScrolledText, ScrolledFrame
from ttkbootstrap.dialogs.dialogs import Messagebox
import subprocess
import configparser
import json

import os
import datetime

import tools_dict


class APP(ttk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        self.rootPath = tools_dict.tools_root_path()
        print(f"调试信息: 1.工具的类别目录是：\n{self.rootPath}\n")
        self.toolsDic = tools_dict.toolsDir()

        self.config_ini_path1 = os.path.dirname(os.path.abspath(__file__))
        self.config_ini_path = f"{self.config_ini_path1}\config\config.ini"
        print(f"调试信息: 2.config.ini文件路径是: \n{self.config_ini_path}\n")

        self.config_style = configparser.ConfigParser()
        self.config_style.read(filenames=self.config_ini_path,
                               encoding="utf-8")

        self.app_size_w = int(self.config_style["app"]["size_w"])
        self.app_size_h = int(self.config_style["app"]["size_h"])
        self.average = int(self.config_style["app"]["average"])
        self.tool_aver = int(self.config_style["app"]["tool_aver"])
        self.note_aver = int(self.config_style["app"]["note_aver"])

        print(
            f"调试信息: 3.工具框架的宽是:\n{int(self.app_size_w/self.average*self.tool_aver)}\n"
        )
        print(
            f"调试信息: 4.笔记框架的宽是:\n{int(self.app_size_w/self.average*self.note_aver)}\n"
        )

        self.toolFra = ttk.LabelFrame(
            self,
            text=self.config_style["tool"]["title"],
            bootstyle=self.config_style["tool"]["theme"],
            width=int(self.app_size_w / self.average * self.tool_aver),
            height=self.app_size_h,
            labelanchor=NW,
            padding=7,
            border=10)
        self.toolFra.pack(side="left",
                          fill=BOTH,
                          ipadx=7,
                          ipady=10,
                          padx=10,
                          pady=20)
        self.toolFrame = ScrolledFrame(
            self.toolFra,
            autohide=True,
            width=int(self.app_size_w / self.average * self.tool_aver),
            height=self.app_size_h + 500,
            bootstyle=self.config_style["tool"]["scrolled"])
        self.toolFrame.pack(fill=BOTH, anchor=NW)

        self.noteFrame = ttk.LabelFrame(
            self,
            text=self.config_style["note"]["title"],
            bootstyle=self.config_style["note"]["theme"],
            width=int(self.app_size_w / self.average * self.note_aver),
            height=self.app_size_h,
            labelanchor=NW,
            padding=7,
            border=10)
        self.noteFrame.pack(side="left", ipadx=7, ipady=10, padx=10, pady=20)

        self.noteFrame_up = ttk.Frame(
            self.noteFrame, bootstyle=self.config_style["note"]["theme_up"])
        self.noteFrame_up.pack(side="top", fill="x", ipadx=7, ipady=10)

        self.noteFrameTxtSaveBtn = ttk.Button(
            self.noteFrame_up,
            text=" 保存笔记 ",
            bootstyle=self.config_style["note"]["funBtnBootstyle"])
        self.noteFrameTxtSaveBtn.pack(anchor=W,
                                      padx=2,
                                      pady=2,
                                      ipadx=10,
                                      side="left",
                                      ipady=10)

        self.noteFrameStartBtn = ttk.Button(
            self.noteFrame_up,
            text=" 打开目录 ",
            bootstyle=self.config_style["note"]["funBtnBootstyle"])
        self.noteFrameStartBtn.pack(anchor=W,
                                    side="left",
                                    padx=2,
                                    pady=2,
                                    ipadx=10,
                                    ipady=10)

        self.noteFrameRefreshBtn = ttk.Button(
            self.noteFrame_up,
            text=" 刷新GUI ",
            bootstyle=self.config_style["note"]["funBtnBootstyle"])
        self.noteFrameRefreshBtn.pack(anchor=W,
                                      side="left",
                                      padx=2,
                                      pady=2,
                                      ipadx=10,
                                      ipady=10)
        self.noteFrameRefreshBtn["command"] = self.refresh

        self.noteFrameOpenDirBtn = ttk.Button(
            self.noteFrame_up,
            text=" 启动工具 ",
            bootstyle=self.config_style["note"]["funBtnBootstyle"])
        self.noteFrameOpenDirBtn.pack(anchor=W,
                                      side="left",
                                      padx=2,
                                      pady=2,
                                      ipadx=10,
                                      ipady=10)

        self.noteFrameCommandBtn = ttk.Button(
            self.noteFrame_up,
            text=" 编辑启动命令 ",
            bootstyle=self.config_style["note"]["funBtnBootstyle"])
        self.noteFrameCommandBtn.pack(anchor=W,
                                      side="left",
                                      padx=2,
                                      pady=2,
                                      ipadx=10,
                                      ipady=10)
        self.noteFrameCommandBtn[COMMAND] = self.openStartCommandIniFile

        self.noteFrameStyleBtn = ttk.Button(
            self.noteFrame_up,
            text=" 样式修改 ",
            bootstyle=self.config_style["note"]["funBtnBootstyle"])
        self.noteFrameStyleBtn.pack(anchor=W,
                                    side="right",
                                    padx=2,
                                    pady=2,
                                    ipadx=10,
                                    ipady=10)
        self.noteFrameStyleBtn[COMMAND] = self.openStyleIniFile

        self.noteFrame_down = ttk.LabelFrame(
            self.noteFrame,
            text=self.config_style["note"]["txt_title"],
            style=self.config_style["note"]["noteFrameDownStyle"],
            padding=5)
        self.noteFrame_down.pack(fill=BOTH, padx=3, pady=3)

        self.txtCount = ScrolledText(
            self.noteFrame_down,
            width=int(self.app_size_w / self.average * self.note_aver),
            height=self.app_size_h,
            bootstyle=self.config_style["note"]["scrolledTextBootstyle"],
            autohide=True)
        self.txtCount.pack(fill=BOTH, side=BOTTOM, anchor=NW)

        self.toolFrameFun()

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

        toolFunlist = self.config_style.get("tool", "funList")
        toolFunlist = json.loads(toolFunlist)

        for i in range(int(self.config_style["tool"]["toolColumn"])):
            self.Btnfr1 = ttk.Button(
                self.toolFrame,
                text=toolFunlist[i][0],
                width=self.config_style["tool"]["columnWidth"],
                bootstyle=self.config_style["tool"]["funBtnBootstyle"],
                command=lambda arg=toolFunlist[i][1]: self.toolFunBtn(
                    arg)).grid(pady=2, row=0, column=i)
        r = 1

        for k in self.toolsDic.keys():
            self.btnToolType = ttk.Button(
                self.toolFrame,
                text=k,
                bootstyle=self.config_style["tool"]["typeBtnBootstyle"],
                command=lambda a=k:
                [self.openToolTypeNote(a),
                 self.toolTypeTitle(a)])
            self.btnToolType.grid(row=r,
                                  column=0,
                                  columnspan=int(
                                      self.config_style["tool"]["toolColumn"]),
                                  sticky=W)

            self.btnToolType.bind("<Double-Button-1>",
                                  lambda event, arg0=k: self.openTypeDir(arg0))

            r += 1
            c = 0

            for i in self.toolsDic[k]:
                if c == int(self.config_style["tool"]["toolColumn"]):
                    r += 1
                    c = 0
                self.btnTools = ttk.Button(
                    self.toolFrame,
                    bootstyle=self.config_style["tool"]["toolBtnBootstyle"],
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

    def toolTypeTitle(self, typedir):

        for widget in self.noteFrame_up.winfo_children():
            widget.destroy()

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
                                      ipady=10)

        self.noteFrameStartBtn = ttk.Button(
            self.noteFrame_up,
            text=" 打开目录 ",
            bootstyle=self.config_style["note"]["funBtnBootstyle"])
        self.noteFrameStartBtn.pack(anchor=W,
                                    side="left",
                                    padx=2,
                                    pady=2,
                                    ipadx=10,
                                    ipady=10)
        self.noteFrameStartBtn[
            COMMAND] = lambda arg0=typedir: self.openTypeDir(arg0)

        self.noteFrameRefreshBtn = ttk.Button(
            self.noteFrame_up,
            text=" 刷新GUI ",
            bootstyle=self.config_style["note"]["funBtnBootstyle"])
        self.noteFrameRefreshBtn.pack(anchor=W,
                                      side="left",
                                      padx=2,
                                      pady=2,
                                      ipadx=10,
                                      ipady=10)
        self.noteFrameRefreshBtn["command"] = self.refresh

        self.noteFrameOpenDirBtn = ttk.Button(
            self.noteFrame_up,
            text=" 启动工具 ",
            bootstyle=self.config_style["note"]["funBtnBootstyle"])
        self.noteFrameOpenDirBtn.pack(anchor=W,
                                      side="left",
                                      padx=2,
                                      pady=2,
                                      ipadx=10,
                                      ipady=10)

        self.noteFrameCommandBtn = ttk.Button(
            self.noteFrame_up,
            text=" 编辑启动命令 ",
            bootstyle=self.config_style["note"]["funBtnBootstyle"])
        self.noteFrameCommandBtn.pack(anchor=W,
                                      side="left",
                                      padx=2,
                                      pady=2,
                                      ipadx=10,
                                      ipady=10)
        self.noteFrameCommandBtn[COMMAND] = self.openStartCommandIniFile

        self.noteFrameStyleBtn = ttk.Button(
            self.noteFrame_up,
            text=" 样式修改 ",
            bootstyle=self.config_style["note"]["funBtnBootstyle"])
        self.noteFrameStyleBtn.pack(anchor=W,
                                    side="right",
                                    padx=2,
                                    pady=2,
                                    ipadx=10,
                                    ipady=10)
        self.noteFrameStyleBtn[COMMAND] = self.openStyleIniFile

    def toolTitle(self, typedir, tool):

        for widget in self.noteFrame_up.winfo_children():
            widget.destroy()

        self.noteFrameTxtSaveBtn = ttk.Button(
            self.noteFrame_up,
            text=" 保存笔记 ",
            bootstyle=self.config_style["note"]["funBtnBootstyle"],
            command=lambda a=typedir, b=tool: self.saveToolNote(a, b))
        self.noteFrameTxtSaveBtn.pack(anchor=W,
                                      side="left",
                                      padx=2,
                                      pady=2,
                                      ipadx=10,
                                      ipady=10)

        self.noteFrameStartBtn = ttk.Button(
            self.noteFrame_up,
            text=" 打开目录 ",
            bootstyle=self.config_style["note"]["funBtnBootstyle"])
        self.noteFrameStartBtn.pack(anchor=W,
                                    side="left",
                                    padx=2,
                                    pady=2,
                                    ipadx=10,
                                    ipady=10)
        self.noteFrameStartBtn[
            COMMAND] = lambda arg1=typedir, arg2=tool: self.openToolDir(
                arg1, arg2)

        self.noteFrameRefreshBtn = ttk.Button(
            self.noteFrame_up,
            text=" 刷新GUI ",
            bootstyle=self.config_style["note"]["funBtnBootstyle"])
        self.noteFrameRefreshBtn.pack(anchor=W,
                                      side="left",
                                      padx=2,
                                      pady=2,
                                      ipadx=10,
                                      ipady=10)
        self.noteFrameRefreshBtn["command"] = self.refresh

        self.noteFrameOpenDirBtn = ttk.Button(
            self.noteFrame_up,
            text=" 启动工具 ",
            bootstyle=self.config_style["note"]["funBtnBootstyle"])
        self.noteFrameOpenDirBtn.pack(anchor=W,
                                      side="left",
                                      padx=2,
                                      pady=2,
                                      ipadx=10,
                                      ipady=10)
        self.noteFrameOpenDirBtn[
            COMMAND] = lambda arg1=typedir, arg2=tool: self.openToolCmd(
                arg1, arg2)

        self.noteFrameCommandBtn = ttk.Button(
            self.noteFrame_up,
            text=" 编辑启动命令 ",
            bootstyle=self.config_style["note"]["funBtnBootstyle"])
        self.noteFrameCommandBtn.pack(anchor=W,
                                      side="left",
                                      padx=2,
                                      pady=2,
                                      ipadx=10,
                                      ipady=10)
        self.noteFrameCommandBtn[COMMAND] = self.openStartCommandIniFile

        self.noteFrameStyleBtn = ttk.Button(
            self.noteFrame_up,
            text=" 样式修改 ",
            bootstyle=self.config_style["note"]["funBtnBootstyle"])
        self.noteFrameStyleBtn.pack(anchor=W,
                                    side="right",
                                    padx=2,
                                    pady=2,
                                    ipadx=10,
                                    ipady=10)
        self.noteFrameStyleBtn[COMMAND] = self.openStyleIniFile

    def saveTypeNote(self, typedir):
        notePath = f'{self.rootPath}\{typedir}\{self.config_style["app"]["txt_mark"]}'

        content = self.txtCount.get(1.0, END)
        with open(notePath, "w", encoding='utf-8') as f:
            f.write(content)

    def saveToolNote(self, typedir, tool):
        notePath = f'{self.rootPath}\{typedir}\{tool}\{self.config_style["app"]["txt_mark"]}'

        content = self.txtCount.get(1.0, END)
        with open(notePath, "w", encoding='utf-8') as f:
            f.write(content)

    def openToolNote(self, typedir, tool):
        notePath = f'{self.rootPath}\{typedir}\{tool}\{self.config_style["app"]["txt_mark"]}'

        self.noteFrame_down["text"] = f"-- {self.rootPath}\{typedir}\{tool} --"

        if os.path.exists(notePath):
            with open(notePath, encoding='utf-8') as f:
                self.txtCount.delete('1.0', END)
                self.txtCount.insert(END, f.read())

        else:
            Messagebox.ok(message="\n\t你还没有创建笔记，已自动创建初始化信息。\t\n",
                          title='OpenNote')
            infoMsg = f"-----你还没有创建笔记-----{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}-----"
            self.txtCount.delete('1.0', END)
            self.txtCount.insert(END, infoMsg)
            f = open(notePath, "w", encoding='utf-8')
            f.writelines(infoMsg)
            f.close()

    def openToolTypeNote(self, typedir):
        notePath = f'{self.rootPath}\{typedir}\{self.config_style["app"]["txt_mark"]}'

        self.noteFrame_down["text"] = f"-- {self.rootPath}\{typedir} --"

        if os.path.exists(notePath):
            with open(notePath, encoding='utf-8') as f:
                self.txtCount.delete('1.0', END)
                self.txtCount.insert(END, f.read())

        else:
            Messagebox.ok(message="\n\t你还没有创建笔记，已自动创建初始化信息。\t\n",
                          title='OpenNote')
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

            if "type" in conf.options(tool):
                print(conf.get(tool, "type"))

                if "command" in conf.options(tool):
                    print(conf.get(tool, "command"))
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

            subprocess.Popen(f'start cmd /k  "title {tool}"', shell=True)
        os.chdir(self.rootPath)
        print(typedir, tool)

    def openStartCommandIniFile(self):
        path = os.path.dirname(os.path.abspath(__file__))

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
        self.noteFrameStyleBtn['state'] = DISABLED
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
        self.saveBtn[COMMAND] = self.saveStartCommandIniFile

    def saveStartCommandIniFile(self):
        path = os.path.dirname(os.path.abspath(__file__))

        path = f"{path}\config\startCommand.ini"
        print(path)
        command_ini_data = self.txtCount.get(1.0, END)
        print(type(command_ini_data))
        self.saveBtn.pack_forget()
        self.noteFrameCommandBtn.pack(anchor=W,
                                      side="left",
                                      padx=2,
                                      pady=2,
                                      ipadx=10,
                                      ipady=10)
        with open(path, "w", encoding='utf-8') as f:
            f.write(command_ini_data)

        self.txtCount.delete('1.0', END)
        self.txtCount.insert(END, afterTxt)
        self.noteFrameTxtSaveBtn['state'] = NORMAL
        self.noteFrameStyleBtn['state'] = NORMAL

    def openStyleIniFile(self):
        path = os.path.dirname(os.path.abspath(__file__))

        path = f"{path}\config\config.ini"

        global afterTxt2
        afterTxt2 = self.txtCount.get(1.0, END)
        with open(path, encoding='utf-8') as f:
            self.txtCount.delete('1.0', END)
            self.txtCount.insert(END, f.read())

        self.noteFrameStyleBtn.pack_forget()
        self.noteFrameTxtSaveBtn['state'] = DISABLED
        self.noteFrameCommandBtn['state'] = DISABLED

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
        self.saveBtn[COMMAND] = self.saveStyleIniFile

    def saveStyleIniFile(self):
        path = os.path.dirname(os.path.abspath(__file__))

        path = f"{path}\config\config.ini"

        command_ini_data = self.txtCount.get(1.0, END)

        self.saveBtn.pack_forget()
        self.noteFrameStyleBtn.pack(anchor=W,
                                    side="right",
                                    padx=2,
                                    pady=2,
                                    ipadx=10,
                                    ipady=10)
        with open(path, "w", encoding='utf-8') as f:
            f.write(command_ini_data)

        self.txtCount.delete('1.0', END)
        self.txtCount.insert(END, afterTxt2)
        self.noteFrameTxtSaveBtn['state'] = NORMAL
        self.noteFrameCommandBtn['state'] = NORMAL

    def refresh(self):
        self.toolsDic = tools_dict.toolsDir()

        for widget in self.toolFrame.winfo_children():
            widget.destroy()
        self.toolFrameFun()

    def toolFunBtn(self, typeMark):
        self.toolsDic = tools_dict.toolsDir(typeMark)

        for widget in self.toolFrame.winfo_children():
            widget.destroy()
        self.toolFrameFun()


styleIniPath = os.path.dirname(os.path.abspath(__file__))
styleIniPath = f"{styleIniPath}\config\config.ini"

conf_style = configparser.ConfigParser()
conf_style.read(filenames=styleIniPath, encoding="utf-8")

root = ttk.Window(title=conf_style["app"]["title"],
                  themename=str(conf_style["app"]["theme"]))

screenheight = root.winfo_screenheight()
screenwidth = root.winfo_screenwidth()
print("  调试信息: 屏幕的-宽-高-是 (in pixels) =  \n", (screenwidth, screenheight))
print()



size_w = conf_style["app"]["size_w"]
size_h = conf_style["app"]["size_h"]

center_w = int((screenwidth - int(size_w)) / 2)
center_h = int((screenheight - int(size_h)) / 2)
print("调试信息: 工具的位置参数信息：宽-高-左边距-上边距:\n", size_w, size_h, center_w, center_h)
print()
root.geometry(f'{size_w}x{size_h}+{center_w}+{center_h}')

root.iconbitmap('logo.ico')
app = APP(master=root)

root.mainloop()
