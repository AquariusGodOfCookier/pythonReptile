from tkinter import *
from view import *  #菜单栏对应的各个子页面
 
class MainPage(object):
	def __init__(self, master=None):
		self.root = master #定义内部变量root
		self.root.geometry('%dx%d' % (600, 400)) #设置窗口大小
		self.createPage()
 
	def createPage(self):
		self.technologypage = technologyFrame(self.root) # 创建不同Frame
		self.productPage = productFrame(self.root)
		self.designPage = designFrame(self.root)
		self.operatePage = operateFrame(self.root)
		self.marketPage = marketFrame(self.root)
		self.personnelPage = personnelFrame(self.root)
		self.EMBAPage = EMBAFrame(self.root)
		self.salePage = saleFrame(self.root)
		self.technologypage.pack() #默认显示数据录入界面
		menubar = Menu(self.root)
		menubar.add_command(label='技术', command = self.technology)
		menubar.add_command(label='产品', command = self.product)
		menubar.add_command(label='设计', command = self.design)
		menubar.add_command(label='运营', command = self.operate)
		menubar.add_command(label='市场', command = self.market)
		menubar.add_command(label='人事', command = self.personnel)
		menubar.add_command(label='高级管理', command = self.EMBA)
		menubar.add_command(label='销售', command = self.sale)
		self.root['menu'] = menubar  # 设置菜单栏
 
	def technology(self):
		self.technologypage.pack()
		self.productPage.pack_forget()
		self.designPage.pack_forget()
		self.operatePage.pack_forget()
		self.marketPage.pack_forget()
		self.personnelPage.pack_forget()
		self.EMBAPage.pack_forget()
		self.salePage.pack_forget()
 
	def product(self):
		self.technologypage.pack_forget()
		self.productPage.pack()
		self.designPage.pack_forget()
		self.operatePage.pack_forget()
		self.marketPage.pack_forget()
		self.personnelPage.pack_forget()
		self.EMBAPage.pack_forget()
		self.salePage.pack_forget()
 
	def design(self):
		self.technologypage.pack_forget()
		self.productPage.pack_forget()
		self.designPage.pack()
		self.operatePage.pack_forget()
		self.marketPage.pack_forget()
		self.personnelPage.pack_forget()
		self.EMBAPage.pack_forget()
		self.salePage.pack_forget()
 
	def operate(self):
		self.technologypage.pack_forget()
		self.productPage.pack_forget()
		self.designPage.pack_forget()
		self.operatePage.pack()
		self.marketPage.pack_forget()
		self.personnelPage.pack_forget()
		self.EMBAPage.pack_forget()
		self.salePage.pack_forget()
 
	def market(self):
		self.technologypage.pack_forget()
		self.productPage.pack_forget()
		self.designPage.pack_forget()
		self.operatePage.pack_forget()
		self.marketPage.pack()
		self.personnelPage.pack_forget()
		self.EMBAPage.pack_forget()
		self.salePage.pack_forget()

	def personnel(self):
		self.technologypage.pack_forget()
		self.productPage.pack_forget()
		self.designPage.pack_forget()
		self.operatePage.pack_forget()
		self.marketPage.pack_forget()
		self.personnelPage.pack()
		self.EMBAPage.pack_forget()
		self.salePage.pack_forget()

	def EMBA(self):
		self.technologypage.pack_forget()
		self.productPage.pack_forget()
		self.designPage.pack_forget()
		self.operatePage.pack_forget()
		self.marketPage.pack_forget()
		self.personnelPage.pack_forget()
		self.EMBAPage.pack()
		self.salePage.pack_forget()

	def sale(self):
		self.technologypage.pack_forget()
		self.productPage.pack_forget()
		self.designPage.pack_forget()
		self.operatePage.pack_forget()
		self.marketPage.pack_forget()
		self.personnelPage.pack_forget()
		self.EMBAPage.pack_forget()
		self.salePage.pack()

# root = Tk()
# root.title('小程序')
# v = IntVar()
# MainPage(root)
# root.mainloop()
