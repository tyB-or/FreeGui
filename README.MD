# 工具介绍

freeGui：基于ttkbootstrap开发的一款用来管理自己的渗透测试工具的一个小工具，并提供一些实用小功能，例如打开目录，运行工具，工具备忘命令。

# 开发目的

总结：工具整理+效率提升

1.工具太多，杂乱，用这个可以帮忙分类工具

2.一些不常用的工具需要使用时可能需要重新查资料，这个可以记录一些备忘（txt笔记）方便快速查询

3.有的工具使用需要修改配置文件，使用这个可以一键直达工具目录

4.工具快捷启动，添加启动命令以后可以直接启动工具

5.自由删减工具，用过一些集成工具，虽然开箱即用，但是自由度不高。这个可以帮助自己构建属于自己的工具箱。

6.工具外观自由，工具内部提供高度自由化的配置，可以在工具内部按照自己的喜好修改样式。

# 工具使用：

注意：请使用python3.10及以上版本，低版本可能会出现异常。

## 1.安装模块：

```
pip  install  -r  requirements.txt
```

## 2.启动方式：

```
1.控制台模式：（查看调试信息）
python  gui.py  

2.bat启动
startGui.bat  （已经设置隐藏启动）

3.exe文件：
--（这里可以使用python打包成exe，但是我没有弄，你自己可以本地尝试下）
使用其他工具把bat转成exe(推荐)
Quick Batch File Compiler【可以设置图标】
```

## 3.功能介绍：

a.工具按钮：鼠标左键单击查看，右键单击运行，左键双击打开对应的目录，等同右边笔记上面的按钮。

b.配置文件可以控制软件大小，布局，按钮颜色等样式。请自行研究（样式修改按钮）

c.命令配置文件配置一键启动命令，没有就默认进入对应的cmd界面

d.工具框架中上面的是菜单切换，点击可以切换。

e.自由添加工具分类和工具：类别目录添加时需要带标识：--，类别目录下可自由添加工具，目录名字不宜太长。（请阅读配置文件修改）

（工具汇总：链接：https://pan.baidu.com/s/19qQHDk49NTUKfq3jXAnB2A?pwd=wby8 提取码：wby8 ）
工具展示图：
![image](https://user-images.githubusercontent.com/38561404/212345858-ca79d9d3-6581-4979-83a9-9af9dc3ba219.png)
目录结构图：
请仔细阅读配置文件，在设置类别目录时请带标识。
![image](https://user-images.githubusercontent.com/38561404/212346586-bdad75e9-9626-464c-9376-a343a2f02e05.png)


# 配置文件说明：

样式配置文件：app样式，工具框样式，笔记框样式

\config\\config.ini

```
#20230111
#bytyb-or
#python3.10#3.7有问题，建议使用3.10版本
#样式参考：https://ttkbootstrap.readthedocs.io/en/latest/zh/

#"""
#修改外观，样式
#配置文件分为app(全局)app-左（工具）app-右（笔记）3大区域
#"""

#===================================工具相关参数=====================================

[app]
title=渗透测试工具箱
#工具的标题
theme=darkly
#工具主题样式，参考：litera，darkly，lumen，sandstone，yeti，united，morph，journal，superhero，solar，simplex，cerculean

size_w=2550
#工具大小--宽
size_h=1550
#工具大小--高

average = 5
#工具等分为多少份
tool_aver = 3
#工具框架占比3份，说明，工具框架的宽度占比总宽的3/5
note_aver = 2
#工具框架占比3份，占比总宽的2/5


txt_mark=00.txt
#笔记标识，每个工具的txt备忘。不建议修改。00可以保证排序比较前。

#============================tool框架相关参数-左边====================================

[tool]
title=工具导航-ToolsGui
#工具框架的标题
theme=primary
#Labelframe控件bootstyle，影响边框颜色参考：default,primary,success,info,warning,danger
scrolled=round
#滚动条样式：圆【加-round】和方形，方形参考：default,primary,secondary,success,info,warning,danger,light,dark，圆角举例：danger-round，默认圆角就是round

toolColumn=6
#多少列，工具框架中多少列，可修改
columnWidth=20
#列宽--自己设置，分辨率会影响，所以需要自己调试

#注意：这里的后面的标识也是目录识别的特征，可以自己设置，根据不同的标识区分不同类别，实现功能菜单的切换
#同步toolColumn参数，如果设置7列，列表中必须7个元素，如果分类不多，就用["预留X","自己设定标志识别符"]占位。
funList=[["测试工具","--"],["红蓝对抗","~~"],["学习笔记","__"],["预留1","自己设定标志识别符"],["预留2","自己设定标志识别符"],["预留3","自己设定标志识别符"]]

funBtnBootstyle=success
#工具框架中的菜单切换按钮的样式，Bootstyle：default,primary,secondary,success,info,warning,danger,light,dark
typeBtnBootstyle=info
#工具类别按钮的样式,Bootstyle：Bootstyle：default,primary,secondary,success,info,warning,danger,light,dark
toolBtnBootstyle=info-link
#工具按钮的样式，Bootstyle：success-linkdanger-link（参考上面的加-link）


#==================================note框架相关参数-右边===============================

[note]
title=Note
#笔记框架的标题
theme=PRIMARY
#笔记框架样式，Labelframe控件bootstyle，影响边框颜色参考：default,primary,success,info,warning,danger
theme_up = default
#笔记框架功能框架样式，Labelframe控件bootstyle，影响边框颜色参考：default,primary,success,info,warning,danger

funBtnBootstyle=warning
#笔记框架中上面的按钮的样式，Bootstyle：Bootstyle：default,primary,secondary,success,info,warning,danger,light,dark

startComBtnBootstyle_open=info
#启动命令修改按钮样式的单独设置，参考Bootstyle
startComBtnBootstyle_save=danger
#启动命令按钮样式的单独设置，参考Bootstyle

styleBtnBootstyle_open=info
#样式修改按钮样式的单独设置，参考Bootstyle
styleBtnBootstyle_save=danger
#样式保存按钮样式的单独设置，参考Bootstyle

txt_title=--Content--
#txt笔记的文本提示信息，LabelFrame，后续会随点击的工具不同，变成对应的路径信息

noteFrameDownStyle=success
#笔记框架文本框架样式，Style  笔记框架中分上下，上-功能，下-txt笔记，
scrolledTextBootstyle=success-round
#txt笔记的滚动条样式，#滚动条样式：圆【加-round】和方形，方形参考：Bootstyle：default,primary,secondary,success,info,warning,danger,light,dark，圆角举例：danger-round，默认圆角就是round


```

启动命令配置文件：

\config\\startCommand.ini

```
#添加参考：
#[webfinder-3.2]      这个是工具的目录
#command = java -jar webfinder-3.2.jar   这个是在工具当前目录下的启动工具的命令，不需要加引号。
#type = powershell    【可选】，若添加此参数，会调用powershell
#
#常见问题：
#1.工具的名称填写不规范，会默认进入工具的cmd界面
#2.双击启动没有反应，启动命令填写错误，可以用python  gui.py，在控制台查看报错信息
#
#启动命令参考：start xx.exe    java -jar  xx.jar


# =========================英文路径工具=========================
[0-GUI_Tools]
command = start  start.vbs
```



# 免责声明

```
本工具仅面向合法授权的企业安全建设行为，在使用本工具进行检测时，您应确保该行为符合当地的法律法规，并且已经取得了足够的授权。  

如您在使用本工具的过程中存在任何非法行为，您需自行承担相应后果，我们将不承担任何法律及连带责任。 

在使用本工具前，请您务必审慎阅读、充分理解各条款内容，限制、免责条款或者其他涉及您重大权益的条款可能会以加粗、加下划线等形式提示您重点注意。 除非您已充分阅读、完全理解并接受本协议所有条款，否则，请您不要使用本工具。

您的使用行为或者您以其他任何明示或者默示方式表示接受本协议的，即视为您已阅读并同意本协议的约束。 
```

