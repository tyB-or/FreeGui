
#=======================================工具类别和笔记-标识=========================================

# 工具类别目录标识
# 例如：1--信息收集,记号是mark
toolsTypeDirMark = '--'

# 具体工具笔记
# 工具笔记文件名标识,txt是必要的
toolNoteMark = '00.txt'



# 工具的分类建议：
'''
vnlmap_0.9_py
名称-版本-类型
'''
#=======================================界面大小和屏幕位置和app样式=========================================

# 初始窗口大小，root.geometry('2400x1600+300+200')
appHeight = 1550   #高
appWidth = 2550	 #宽
# 屏幕上左边距
appScree = "300+200"

#ttk框架的样式-str
appThemename = "darkly"
#app的title
#title="FREE_GUI    一款可以自己更新的工具箱__v2.2    by：tyb-or"
appTitle="我的小工具"




#===================工具框架-大小、布局、样式设置=========================================

# 工具框架的标题
toolFrameText = "工具导航-ToolsGui"
# 工具框架的主题
toolFrameBootstyle = "PRIMARY"
# 工具框架的宽  总宽的 3/5
toolFrameWidth = int(appWidth/5*3) #下取整
# 工具框架的高
toolFrameHeight = appHeight
# 工具框架的滚动条样式
toolFrameBootstyle_Scrolled = "round"

# 工具多少列
toolColumn = 4
# 每列列宽，见控制台调试信息：总宽-工具宽-笔记宽-工具列宽
# 这里好像会受到显示器分辨率的问题显示异常，我的数据是2550 1530 1020 255，255修改成20才显示完全
# toolFrameToolColumnWidth = int(toolFrameWidth/toolColumn)
toolFrameToolColumnWidth = 30

# 工具类别按钮的样式
toolTypeBootstyle = "info"
toolBtnBootstyle = "info-link"  # 工具按钮的样式

# 留空位标志符号：
after = "-"


#====================笔记框架-样式修改=========================================
# 笔记框架的标题
noteFrameText = "Note"
# 笔记框架的主题
noteFrameBootstyle = "PRIMARY"
# 笔记框架的宽，总宽的2/5
noteFrameWidth = int(appWidth/5*2) #下取整
# 笔记框架的高
noteFrameHeight = appHeight

#笔记框架功能框架样式
noteFrameUpFraBootstyle = "PRIMARY"
#笔记框架上面框架中的按钮的样式--同步修改工具框架中留空位置的颜色
noteFrameFunBtnBootstyle = "success"
noteFrameFunBtnBootstyle2 = "info"   #启动命令修改按钮样式的单独设置
noteFrameFunBtnBootstyle3 = "danger"  #启动命令按钮样式的单独设置
#笔记框架文本框架标题
noteFrameDownTxt = " --Content--  "
#笔记框架文本框架样式
noteFrameDownStyle = "success"
#笔记框架文本框架滚动样式
noteFrameDownScrolled = 'success-round'