from tkinter import *
from tkinter.messagebox import *
from MainPage import *

class LoginPage(object):
    def __init__(self,master=None):
        self.root = master
        self.root.geometry('%dx%d'%(600,400))
        self.v = IntVar()
        self.createPage()
        
    def createPage(self):
        self.page=Frame(self.root)
        self.page.pack()
        Label(self.page,text="声明").grid(row=0)
        Label(self.page,text="本软件仅供python大作业学习使用，不具有其他用途，不负任何责任").grid(row=1)
        checkButton = Checkbutton(self.page,text="我同意",variable=self.v).grid(row=5,columnspan=5,sticky=W)
        Button(self.page,text='下一步',command=self.next).grid(row=10, columnspan=2, stick=W)
        Button(self.page,text='退出',command=self.page.quit).grid(row=10, columnspan=2, stick=E)

    def next(self):
        IsAgree = self.v.get()
        if IsAgree == 1:
            self.page.destroy()
            MainPage(self.root)
        else:
            showinfo(title='错误',message='请选择是否同意')


