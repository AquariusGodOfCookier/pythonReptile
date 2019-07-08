from tkinter import *
from tkinter.messagebox import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
import os
import Analysis
class AnalysisG(object):
    def __init__(self,master=None,id="A"):
        self.root = master
        self.root.geometry('%dx%d'%(600,400))
        self.id = id
        self.createPage()
    def createPage(self):
        self.page = Frame(self.root)
        self.page.pack()
        menubar = Menu(self.page)
        menubar.add_command(label='须知',command = self.file)
        menubar.add_command(label='统计学历',command = self.education)
        menubar.add_command(label='统计薪水',command = self.money)
        # menubar.add_command(label='返回上一级',command = self.back)
        self.root['menu'] = menubar


    def file(self):
        showinfo(title='须知',message='暂时只能统计学历与薪水')

    def education(self):
        Analysis.read_excel(self.id,'education')
    def money(self):
        Analysis.read_excel(self.id,'money')
    # def back(self):
    #     self.page.destroy()
    #     root = Tk()
    #     root.title('小程序')
    #     v = IntVar()
    #     MainPage(root)
    #     root.mainloop()

# root = Tk()
# root.title('小程序')
# v = IntVar()
# AnalysisG(root,'C:\\Users\\Dell\\Desktop\\爬虫代码\\php.xlsx')
# root.mainloop()
