## 前言

freeGui：基于ttkbootstrap开发的一款windows渗透测试工具管理框架。你可以用来动态管理自己的工具，框架内部提供了笔记备忘，一键启动，直达目录等实用功能。

后期会往里面增加工具和笔记

（python可以打包成exe,不想打包的话就用专门的工具把bat等转成exe,就可以拖到外面了。）

## 工具基础使用：

1.下载解压后，你得到的是演示demo，删除其余文件，仅保留FreeGui_v2.1_win即可。

2.安装模块：

```
pip   install  -r  requirements.txt
```

3.在FreeGui_v2.1_win的同级目录下创建自己想要的工具分类目录（带有“--”标识），例如：01--信息收集

4.在创建好的目录（01--信息收集）中放入想要添加的工具，例如：appinfoscan

5.启动工具：

```python
# 启动方式：
python  gui.py  
# 或者双击
startGui.bat 、  startGui.vbs  都行
```

6.重复循环3-4，时间久了，就会形成自己的工具箱。

参考demo:

![image-20221212202346022](https://github.com/tyB-or/FreeGui/blob/main/image/image-20221212202346022.png)



## 工具界面介绍：

1：

![image-20221212204834349](https://github.com/tyB-or/FreeGui/blob/main/image/image-20221212204834349.png)

2：

![image-20221212205434389](https://github.com/tyB-or/FreeGui/blob/main/image/image-20221212205434389.png)

3：

![image-20221212205843428](https://github.com/tyB-or/FreeGui/blob/main/image/image-20221212205843428.png)

![image-20221212205942883](https://github.com/tyB-or/FreeGui/blob/main/image/image-20221212205942883.png)

4：启动命令说明：

点击前：

![image-20221212210234445](https://github.com/tyB-or/FreeGui/blob/main/image/image-20221212210234445.png)

点击后：

![image-20221212210645137](https://github.com/tyB-or/FreeGui/blob/main/image/image-20221212210645137.png)

5：启动工具按钮说明：

我在这里把工具分为2类，图形化工具和命令行工具，在使用命令行工具时，点击按钮会自动进入该工具的cmd界面，并设置title

![image-20221212211634138](https://github.com/tyB-or/FreeGui/blob/main/image/image-20221212211634138.png)

图形化工具：如果不想使用命令行的方式启动，那就先配置好启动命令，保存后双击就是直接启动工具：

（常见的启动方式：java  -jar  xx.jar        start  xx.exe   ）

![image-20221212211856154](https://github.com/tyB-or/FreeGui/blob/main/image/image-20221212211856154.png)

## 后续：

布局优化、添加工具和笔记。

不足之处：有的地方异常处理缺少交互。但是不影响使用。

针对不同尺寸的电脑屏幕显示会有异常（如果你的电脑显示有异常，欢迎提交issues，我会尽力解决）

对应代码片段：

![image-20221212214944724](https://github.com/tyB-or/FreeGui/blob/main/image/image-20221212214933439.png)
![image-20221212212716778](https://github.com/tyB-or/FreeGui/blob/main/image/image-20221212214944724.png)

mac版本的适配也在进行中，感谢@asaotomo

## DIY功能：

**--修改标识，位置：**

配置文件：FreeGui_v2.1_win\config\mark.py


![image-20221212214933439](https://github.com/tyB-or/FreeGui/blob/main/image/image-20221212212716778.png)



**--修改内部布局，样式：**

主程序文件：FreeGui_v2.1_win\gui.py

样式修改参考：https://ttkbootstrap.readthedocs.io/en/latest/zh/



**--自由、快速、便捷的添加和更新工具**

启动命令保存即生效。

工具更新，点击刷新GUI按钮即可生效。

## 更新记录：

**20221213更新**：v2.2

优化布局：采用等宽靠左布局。同时工具界面预留5个位置，方便后续功能拓展。

优化保存启动命令的点击逻辑：点击后笔记框恢复原来的工具命令笔记，并恢复保存笔记按钮的功能。

补充mac版本。

解决bug：点击刷新gui时，原先控件影像残留问题


**屏幕大小显示异常问题请按需修改源码：**

gui.py【下面是针对macbookpro-2021-13.3英寸进行适配修改的，初始设置均为一半】

工具界面-宽：width=self.width / 3【第50行】

笔记界面-宽：width=(self.width / 3) * 2【第59行】

同时，在代码的【156行】调整参数：width=16

初始大小和位置请修改config.mark文件，里面有详细说明。

**20221217更新**：添加工具（样式可以自己修改，白的太亮了，笔记不是很清楚，自己换成黑暗样式）
![image](https://user-images.githubusercontent.com/38561404/208229483-661b9f20-e0df-4085-aecd-33c033d0f65e.png)

工具链接：
链接：https://pan.baidu.com/s/1fLm5QCbK8JvJLV0MetkPCg?pwd=t1ui 
提取码：t1ui 

使用说明：
在工具的同级目录下导入这些类别的工具，部分工具需要解压后使用（放的是压缩包），且工具名不要太长，否则上面的灰条会有分割提示你。
因为工具在使用的过程中会包含一些项目敏感信息，也不想再去找原版工具了，所以后续应该是不会在更新了。
工具本意是构造自己熟悉的工具箱，记录工作中的想法，记性不好经常反复查资料，有的东西用的次数不多，容易忘，这个工具刚好记录，有个印象直接在工具里找，比较快。
工具不仅仅可以放工具，放一些笔记，文档资料也行，方便自己速查。

**20230110：提升自由度**
更新：（耗费时间：20230109--20230110），正好一起解决了，顺路补充下集成工具箱：开箱即用。

1.配置参数化：修改mark.py参数
调整工具大小，位置，内部工具，笔记占比，这里设置3:2，可修改。
可自由设置工具框架中每列工具宽度（自适应受到分辨率影响，所以需要手工设置），一行显示几个工具。摆脱工具名称过长的影响。
修改工具的样式-总样式
修改内部按钮的样式：类别按钮，工具按钮，笔记功能按钮，滚动条样式。
文本自定义：自由设定修改文字信息，软件标题，工具标题，笔记标题，功能预留标志符

2.修改启动命令配置文件：
增加powershell启动，增加参数可打开powershell，方便启动需要powershell权限的工具

3.外观修改：
笔记框架中功能按钮按左布局，避免挤占
删除笔记框架中信息显示文本框，改为动态显示：点击左边按钮，显示对应的路径信息。

存在问题：设置3:2，全屏后变为1:1，这个问题暂时没找到原因，不搞了。
工具箱地址：
链接：https://pan.baidu.com/s/19qQHDk49NTUKfq3jXAnB2A?pwd=wby8 
提取码：wby8 
--来自百度网盘超级会员V6的分享

![image](https://user-images.githubusercontent.com/38561404/211466071-2c0dd322-2958-405e-ad9b-033c55d938cf.png)




## 常见问题：
1.因为当前gui框架自身原因，请尽量设置短工具名，同时，因为屏幕大小和分辨率问题，查看了官方文档并没有很好的办法解决，请参考config\mark.py文件中的说明进行调整，这个需要你有一定的代码基础。


## 免责声明

```
本工具仅面向合法授权的企业安全建设行为，在使用本工具进行检测时，您应确保该行为符合当地的法律法规，并且已经取得了足够的授权。  

如您在使用本工具的过程中存在任何非法行为，您需自行承担相应后果，我们将不承担任何法律及连带责任。 

在使用本工具前，请您务必审慎阅读、充分理解各条款内容，限制、免责条款或者其他涉及您重大权益的条款可能会以加粗、加下划线等形式提示您重点注意。 除非您已充分阅读、完全理解并接受本协议所有条款，否则，请您不要使用本工具。

您的使用行为或者您以其他任何明示或者默示方式表示接受本协议的，即视为您已阅读并同意本协议的约束。 
```

