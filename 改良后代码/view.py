from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk
import os
import load
import db
import time
from AnalysisG import *
class technologyFrame(Frame): # 继承Frame类
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.root = master #定义内部变量root
		self.itemStart = StringVar()
		self.itemEnd = StringVar()
		self.number = StringVar()
		self.createPage()
 
	def createPage(self):
		Label(self).grid(row=0,stick=W,pady=10)
		Label(self, text = '请输入起始页数: ').grid(row=1, stick=W, pady=10)
		Entry(self, textvariable=self.itemStart).grid(row=1, column=1, stick=E)
		Label(self, text = '请输入结束页数: ').grid(row=2, stick=W, pady=10)
		Entry(self, textvariable=self.itemEnd).grid(row=2, column=1, stick=E)
		Label(self, text = '请选择要下载的职位: ').grid(row=3, stick=W, pady=10)
		numberchosen = ttk.Combobox(self,textvariable=self.number,state='readonly',width=17)
		numberchosen['values']=("java","php","web前端","html5","ios","javascript","python",'android')
		numberchosen.grid(row=3,column=1,stick=E,pady=10)
		numberchosen.current(0)
		Button(self, text='退出',width=20,command=self.back).grid(row=6, column=1, stick=E)
		Button(self, text='下载',width=20,command=self.technology).grid(row=6, column=1, stick=W)	
	
	def technology(self):
		theStartPage = self.itemStart.get()
		theEndPage = self.itemEnd.get()
		WhatPosition = self.number.get()
		try:
			showinfo(title='状态',message='点击开始下载')
			filename = os.path.abspath('')+'\\'+WhatPosition+'.xlsx'
			a = load.go(WhatPosition,theStartPage,theEndPage)
			if a =='ok':
				whentime =time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
				try:
					db.conn(WhatPosition,whentime)
				except:
					showinfo(title='错误',message='数据库错误')
				showinfo(title='状态',message='下载完成')
				self.root.destroy()
				root = Tk()
				root.title('小程序')
				AnalysisG(root,filename)
				root.mainloop()
			else:
				showinfo(title='错误',message='您使用次数过多，ip暂时被停封，不用担心，换个ip或者等待一段时间就可以')
		except:
			showinfo(title='错误',message='请正确输入起始页与终止页')
	def back(self):
		self.destroy()
class productFrame(Frame): # 继承Frame类
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.root = master #定义内部变量root
		self.itemStart = StringVar()
		self.itemEnd = StringVar()
		self.number = StringVar()
		self.createPage()
 
	def createPage(self):
		Label(self).grid(row=0,stick=W,pady=10)
		Label(self, text = '请输入起始页数: ').grid(row=1, stick=W, pady=10)
		Entry(self, textvariable=self.itemStart).grid(row=1, column=1, stick=E)
		Label(self, text = '请输入结束页数: ').grid(row=2, stick=W, pady=10)
		Entry(self, textvariable=self.itemEnd).grid(row=2, column=1, stick=E)
		Label(self, text = '请选择要下载的职位: ').grid(row=3, stick=W, pady=10)
		numberchosen = ttk.Combobox(self,textvariable=self.number,state='readonly',width=17)
		numberchosen['values']=("产品经理","产品总监","游戏策划","高端产品职位","游戏制作人","其他产品职位")
		numberchosen.grid(row=3,column=1,stick=E,pady=10)
		numberchosen.current(0)
		Button(self, text='退出',width=20,command=self.back).grid(row=6, column=1, stick=E)
		Button(self, text='下载',width=20,command=self.product).grid(row=6, column=1, stick=W)	
	
	def product(self):
		theStartPage = self.itemStart.get()
		theEndPage = self.itemEnd.get()
		WhatPosition = self.number.get()
		try:
			showinfo(title='状态',message='点击开始下载')
			a = load.go(WhatPosition,theStartPage,theEndPage)
			if a =='ok':
				whentime =time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
				try:
					db.conn(WhatPosition,whentime)
				except:
					showinfo(title='错误',message='数据库错误')
				showinfo(title='状态',message='下载完成')
				self.root.destroy()
				root = Tk()
				root.title('小程序')
				AnalysisG(root,'C:\\Users\\Dell\\Desktop\\爬虫代码\\php.xlsx')
				root.mainloop()
			else:
				showinfo(title='错误',message='您使用次数过多，ip暂时被停封，不用担心，换个ip或者等待一段时间就可以')
		except:
			showinfo(title='错误',message='请正确输入起始页与终止页')
	def back(self):
		self.destroy()
 
class designFrame(Frame): # 继承Frame类
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.root = master #定义内部变量root
		self.itemStart = StringVar()
		self.itemEnd = StringVar()
		self.number = StringVar()
		self.createPage()
 
	def createPage(self):
		Label(self).grid(row=0,stick=W,pady=10)
		Label(self, text = '请输入起始页数: ').grid(row=1, stick=W, pady=10)
		Entry(self, textvariable=self.itemStart).grid(row=1, column=1, stick=E)
		Label(self, text = '请输入结束页数: ').grid(row=2, stick=W, pady=10)
		Entry(self, textvariable=self.itemEnd).grid(row=2, column=1, stick=E)
		Label(self, text = '请选择要下载的职位: ').grid(row=3, stick=W, pady=10)
		numberchosen = ttk.Combobox(self,textvariable=self.number,state='readonly',width=17)
		numberchosen['values']=("ui设计师","平面设计师","网页设计师","交互设计师","插画师","数据分析师")
		numberchosen.grid(row=3,column=1,stick=E,pady=10)
		numberchosen.current(0)
		Button(self, text='退出',width=20,command=self.back).grid(row=6, column=1, stick=E)
		Button(self, text='下载',width=20,command=self.design).grid(row=6, column=1, stick=W)	
	
	def design(self):
		theStartPage = self.itemStart.get()
		theEndPage = self.itemEnd.get()
		WhatPosition = self.number.get()
		try:
			showinfo(title='状态',message='点击开始下载')
			a = load.go(WhatPosition,theStartPage,theEndPage)
			if a =='ok':
				whentime =time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
				try:
					db.conn(WhatPosition,whentime)
				except:
					showinfo(title='错误',message='数据库错误')
				showinfo(title='状态',message='下载完成')
				self.root.destroy()
				root = Tk()
				root.title('小程序')
				AnalysisG(root,'C:\\Users\\Dell\\Desktop\\爬虫代码\\php.xlsx')
				root.mainloop()
			else:
				showinfo(title='错误',message='您使用次数过多，ip暂时被停封，不用担心，换个ip或者等待一段时间就可以')
		except:
			showinfo(title='错误',message='请正确输入起始页与终止页')
	def back(self):
		self.destroy()
 
class operateFrame(Frame): # 继承Frame类
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.root = master #定义内部变量root
		self.itemStart = StringVar()
		self.itemEnd = StringVar()
		self.number = StringVar()
		self.createPage()
 
	def createPage(self):
		Label(self).grid(row=0,stick=W,pady=10)
		Label(self, text = '请输入起始页数: ').grid(row=1, stick=W, pady=10)
		Entry(self, textvariable=self.itemStart).grid(row=1, column=1, stick=E)
		Label(self, text = '请输入结束页数: ').grid(row=2, stick=W, pady=10)
		Entry(self, textvariable=self.itemEnd).grid(row=2, column=1, stick=E)
		Label(self, text = '请选择要下载的职位: ').grid(row=3, stick=W, pady=10)
		numberchosen = ttk.Combobox(self,textvariable=self.number,state='readonly',width=17)
		numberchosen['values']=("产品运营","新媒体运营","游戏运营","数据运营","编辑","客服")
		numberchosen.grid(row=3,column=1,stick=E,pady=10)
		numberchosen.current(0)
		Button(self, text='退出',width=20,command=self.back).grid(row=6, column=1, stick=E)
		Button(self, text='下载',width=20,command=self.operate).grid(row=6, column=1, stick=W)	
	
	def operate(self):
		theStartPage = self.itemStart.get()
		theEndPage = self.itemEnd.get()
		WhatPosition = self.number.get()
		try:
			showinfo(title='状态',message='点击开始下载')
			a = load.go(WhatPosition,theStartPage,theEndPage)
			if a =='ok':
				whentime =time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
				try:
					db.conn(WhatPosition,whentime)
				except:
					showinfo(title='错误',message='数据库错误')
				showinfo(title='状态',message='下载完成')
				self.root.destroy()
				root = Tk()
				root.title('小程序')
				AnalysisG(root,'C:\\Users\\Dell\\Desktop\\爬虫代码\\php.xlsx')
				root.mainloop()
			else:
				showinfo(title='错误',message='您使用次数过多，ip暂时被停封，不用担心，换个ip或者等待一段时间就可以')
		except:
			showinfo(title='错误',message='请正确输入起始页与终止页')
	def back(self):
		self.destroy()

class marketFrame(Frame): # 继承Frame类
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.root = master #定义内部变量root
		self.itemStart = StringVar()
		self.itemEnd = StringVar()
		self.number = StringVar()
		self.createPage()
 
	def createPage(self):
		Label(self).grid(row=0,stick=W,pady=10)
		Label(self, text = '请输入起始页数: ').grid(row=1, stick=W, pady=10)
		Entry(self, textvariable=self.itemStart).grid(row=1, column=1, stick=E)
		Label(self, text = '请输入结束页数: ').grid(row=2, stick=W, pady=10)
		Entry(self, textvariable=self.itemEnd).grid(row=2, column=1, stick=E)
		Label(self, text = '请选择要下载的职位: ').grid(row=3, stick=W, pady=10)
		numberchosen = ttk.Combobox(self,textvariable=self.number,state='readonly',width=17)
		numberchosen['values']=("市场营销","市场推广","市场策划","市场顾问","公关媒介","广告")
		numberchosen.grid(row=3,column=1,stick=E,pady=10)
		numberchosen.current(0)
		Button(self, text='退出',width=20,command=self.back).grid(row=6, column=1, stick=E)
		Button(self, text='下载',width=20,command=self.market).grid(row=6, column=1, stick=W)	
	
	def market(self):
		theStartPage = self.itemStart.get()
		theEndPage = self.itemEnd.get()
		WhatPosition = self.number.get()
		try:
			showinfo(title='状态',message='点击开始下载')
			a = load.go(WhatPosition,theStartPage,theEndPage)
			if a =='ok':
				whentime =time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
				try:
					db.conn(WhatPosition,whentime)
				except:
					showinfo(title='错误',message='数据库错误')
				showinfo(title='状态',message='下载完成')
				self.root.destroy()
				root = Tk()
				root.title('小程序')
				AnalysisG(root,'C:\\Users\\Dell\\Desktop\\爬虫代码\\php.xlsx')
				root.mainloop()
			else:
				showinfo(title='错误',message='您使用次数过多，ip暂时被停封，不用担心，换个ip或者等待一段时间就可以')
		except:
			showinfo(title='错误',message='请正确输入起始页与终止页')
	def back(self):
		self.destroy()

class personnelFrame(Frame): # 继承Frame类
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.root = master #定义内部变量root
		self.itemStart = StringVar()
		self.itemEnd = StringVar()
		self.number = StringVar()
		self.createPage()
 
	def createPage(self):
		Label(self).grid(row=0,stick=W,pady=10)
		Label(self, text = '请输入起始页数: ').grid(row=1, stick=W, pady=10)
		Entry(self, textvariable=self.itemStart).grid(row=1, column=1, stick=E)
		Label(self, text = '请输入结束页数: ').grid(row=2, stick=W, pady=10)
		Entry(self, textvariable=self.itemEnd).grid(row=2, column=1, stick=E)
		Label(self, text = '请选择要下载的职位: ').grid(row=3, stick=W, pady=10)
		numberchosen = ttk.Combobox(self,textvariable=self.number,state='readonly',width=17)
		numberchosen['values']=("hr","行政","财务","人力资源经理","行政经理","出纳")
		numberchosen.grid(row=3,column=1,stick=E,pady=10)
		numberchosen.current(0)
		Button(self, text='退出',width=20,command=self.back).grid(row=6, column=1, stick=E)
		Button(self, text='下载',width=20,command=self.personnel).grid(row=6, column=1, stick=W)	
	
	def personnel(self):
		theStartPage = self.itemStart.get()
		theEndPage = self.itemEnd.get()
		WhatPosition = self.number.get()
		try:
			showinfo(title='状态',message='点击开始下载')
			a = load.go(WhatPosition,theStartPage,theEndPage)
			if a =='ok':
				whentime =time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
				try:
					db.conn(WhatPosition,whentime)
				except:
					showinfo(title='错误',message='数据库错误')
				showinfo(title='状态',message='下载完成')
				self.root.destroy()
				root = Tk()
				root.title('小程序')
				AnalysisG(root,'C:\\Users\\Dell\\Desktop\\爬虫代码\\php.xlsx')
				root.mainloop()
			else:
				showinfo(title='错误',message='您使用次数过多，ip暂时被停封，不用担心，换个ip或者等待一段时间就可以')
		except:
			showinfo(title='错误',message='请正确输入起始页与终止页')
	def back(self):
		self.destroy()

class EMBAFrame(Frame): # 继承Frame类
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.root = master #定义内部变量root
		self.itemStart = StringVar()
		self.itemEnd = StringVar()
		self.number = StringVar()
		self.createPage()
 
	def createPage(self):
		Label(self).grid(row=0,stick=W,pady=10)
		Label(self, text = '请输入起始页数: ').grid(row=1, stick=W, pady=10)
		Entry(self, textvariable=self.itemStart).grid(row=1, column=1, stick=E)
		Label(self, text = '请输入结束页数: ').grid(row=2, stick=W, pady=10)
		Entry(self, textvariable=self.itemEnd).grid(row=2, column=1, stick=E)
		Label(self, text = '请选择要下载的职位: ').grid(row=3, stick=W, pady=10)
		numberchosen = ttk.Combobox(self,textvariable=self.number,state='readonly',width=17)
		numberchosen['values']=("CEO","副总裁","总经理","董事长秘书")
		numberchosen.grid(row=3,column=1,stick=E,pady=10)
		numberchosen.current(0)
		Button(self, text='退出',width=20,command=self.back).grid(row=6, column=1, stick=E)
		Button(self, text='下载',width=20,command=self.EMBA).grid(row=6, column=1, stick=W)	
	
	def EMBA(self):
		theStartPage = self.itemStart.get()
		theEndPage = self.itemEnd.get()
		WhatPosition = self.number.get()
		try:
			showinfo(title='状态',message='点击开始下载')
			a = load.go(WhatPosition,theStartPage,theEndPage)
			if a =='ok':
				whentime =time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
				try:
					db.conn(WhatPosition,whentime)
				except:
					showinfo(title='错误',message='数据库错误')
				showinfo(title='状态',message='下载完成')
				self.root.destroy()
				root = Tk()
				root.title('小程序')
				AnalysisG(root,'C:\\Users\\Dell\\Desktop\\爬虫代码\\php.xlsx')
				root.mainloop()
			else:
				showinfo(title='错误',message='您使用次数过多，ip暂时被停封，不用担心，换个ip或者等待一段时间就可以')
		except:
			showinfo(title='错误',message='请正确输入起始页与终止页')
	def back(self):
		self.destroy()


class saleFrame(Frame): # 继承Frame类
	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.root = master #定义内部变量root
		self.itemStart = StringVar()
		self.itemEnd = StringVar()
		self.number = StringVar()
		self.createPage()
 
	def createPage(self):
		Label(self).grid(row=0,stick=W,pady=10)
		Label(self, text = '请输入起始页数: ').grid(row=1, stick=W, pady=10)
		Entry(self, textvariable=self.itemStart).grid(row=1, column=1, stick=E)
		Label(self, text = '请输入结束页数: ').grid(row=2, stick=W, pady=10)
		Entry(self, textvariable=self.itemEnd).grid(row=2, column=1, stick=E)
		Label(self, text = '请选择要下载的职位: ').grid(row=3, stick=W, pady=10)
		numberchosen = ttk.Combobox(self,textvariable=self.number,state='readonly',width=17)
		numberchosen['values']=("销售专员","销售经理","客户代表","销售管理","商务总监","团队经理")
		numberchosen.grid(row=3,column=1,stick=E,pady=10)
		numberchosen.current(0)
		Button(self, text='退出',width=20,command=self.back).grid(row=6, column=1, stick=E)
		Button(self, text='下载',width=20,command=self.sale).grid(row=6, column=1, stick=W)	
	
	def sale(self):
		theStartPage = self.itemStart.get()
		theEndPage = self.itemEnd.get()
		WhatPosition = self.number.get()
		try:
			showinfo(title='状态',message='点击开始下载')
			a = load.go(WhatPosition,theStartPage,theEndPage)
			if a =='ok':
				whentime =time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
				try:
					db.conn(WhatPosition,whentime)
				except:
					showinfo(title='错误',message='数据库错误')
				showinfo(title='状态',message='下载完成')
				self.root.destroy()
				root = Tk()
				root.title('小程序')
				# AnalysisG(root,'C:\\Users\\Dell\\Desktop\\爬虫代码\\php.xlsx')
				root.mainloop()
			else:
				showinfo(title='错误',message='您使用次数过多，ip暂时被停封，不用担心，换个ip或者等待一段时间就可以')
		except:
			showinfo(title='错误',message='请正确输入起始页与终止页')
	def back(self):
		self.destroy()

