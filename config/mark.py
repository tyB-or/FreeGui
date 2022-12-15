'''
time: 20221127

这个文件保存的是工具的架构标识，可以自己喜好设置。
基础架构：
1--信息收集 					#工具类别
	urlfind					   #具体工具的名称
		00.txt				   #工具的笔记
		xxx.py				   #工具的源文件，启动文件，注意：请不要再新增一级目录

工具的启动类型：

python   xx.py
start  xx.exe

'''

# 工具类别目录标识
# 例如：1--信息收集,记号是mark
toolsTypeDirMark = '--'

# 具体工具
# 工具笔记文件名标识,txt是必要的
toolNoteMark = '00.txt'

# 工具的分类建议：
'''
vnlmap_0.9_py
名称-版本-类型
'''

# 初始窗口大小，root.geometry('2400x1600+300+200')
height = 1550   #高
width = 2550	#宽

# height = 1000   #高
# width = 1200	#宽


'''
如果显示异常，请对照gui.py修改:

# 工具框架-容器， #ScrolledFrame----init方法内
self.toolFra  = ttk.LabelFrame(
    self,text="工具导航-ToolsGui",bootstyle=PRIMARY,width=self.width/2,-----------------
    height=self.height,labelanchor=NW,padding=7,border=10)
self.toolFra.pack(side="left",fill=BOTH,ipadx=7,ipady=10,padx=10,pady=20,expand=True)
self.toolFrame = ScrolledFrame(self.toolFra,autohide=True,width=1100,height=2500,bootstyle="round") #bootstyle='danger-round
self.toolFrame.pack(fill=BOTH,anchor=NW)



# 笔记框架-容器
self.noteFrame = ttk.LabelFrame(
self,text="Note",bootstyle=PRIMARY,width=self.width/2,height=self.height,labelanchor=NW,padding=7,border=10)
self.noteFrame.pack(side="right",fill=BOTH,ipadx=7,ipady=10,padx=10,pady=20,expand=True)

# 笔记框架内部分配：下面添加一个滚动txt控件，显示笔记内容。
self.noteFrame_down = ttk.LabelFrame(self.noteFrame,text=" --Content--  ",style=SUCCESS,padding=5)
self.noteFrame_down.pack(fill=BOTH,padx=3,pady=3)

self.txtCount = ScrolledText(self.noteFrame_down,width=1200, height=1000,bootstyle='success-round',autohide=True)
self.txtCount.pack(fill=BOTH,side=BOTTOM,anchor=NW)


def toolFrameFun(self):----内部：

for i in range(5):
    self.Btnfr1 = ttk.Checkbutton(self.toolFrame,text="-",width=16,bootstyle="warning-toolbutton").grid(pady=5,row=0, column=i) #,state="disabled"
        

'''


# 上左边距，下面的两个参数，作用是保证弹框在中间（取消--1215）
scree = "300+200"



# position=(500,500)   左，上位置
# up = 1000
# left = 400

# x = 400
# y = 1000

# x = 620
# y = 800

