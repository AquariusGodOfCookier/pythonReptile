import xlrd
import matplotlib.pyplot as plt
import numpy as np
import os
import matplotlib

matplotlib.rcParams['font.sans-serif'] = ['SimHei']
matplotlib.rcParams['axes.unicode_minus'] = False
# url = 'C:\\Users\\Dell\\Desktop\\学习文件\\Python\\实践\\pandas\\c#.xlsx'
def read_excel(name,type):
    workbook = xlrd.open_workbook(name)
    sheet = workbook.sheet_by_index(0)
    education_col = sheet.col_values(6)
    money_col = sheet.col_values(1)
    if type=='education':
        draw_get_education(education_col)
    elif type=='money':
        draw_get_money(money_col)
    else:
        return 'error'
def draw_get_education(col):
    educationy=0
    undergraduate = 0  #本科生数量
    master=0           #硕士数量
    specialty=0        #专科数量
    others=0           #其他数量
    for i in col:
        educationy+=1
        if i == '本科':
            undergraduate += 1
        elif i=='硕士' or i=='博士':
            master+=1
        elif i=='专科' or i=='大专':
            specialty+=1
        else:
            others+=1
    plt.ylim(0,250) #y轴取值范围
    val_y = [undergraduate,specialty,master,others]
    scale_ls = range(4)
    index_ls = ['本科','专科','硕博','学历不限']
    plt.xticks(scale_ls,index_ls,fontproperties='SimHei') ## 可以设置坐标字
    plt.title('公司学历要求',fontproperties='SimHei')
    plt.legend()#设置题注
    plt.xlabel('学历要求',fontproperties='SimHei')
    plt.ylabel('公司数量',fontproperties='SimHei')
    rects1=plt.bar(index_ls,val_y,align='center',color='b')
    for rect in rects1:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height+1, str(height), ha="center", va="bottom")
    plt.show()
def draw_get_money(col):
    LowLowMoney = 0 #0-10
    LowMoney=0 #10-15
    HighMoney=0#15-20
    HighHighMoney=0#20++
    allMoney = 0
    for i in col:
        if i == '薪资待遇':
            continue
        allMoney+=1
        low_money = i.split('-')[0]
        high_money = i.split('-')[1].split('K')[0].replace('/天','')
        average_money = int(low_money)+int(high_money)/2
        if average_money >0 and average_money<10:
            LowLowMoney +=1
        elif average_money>=10 and average_money<15:
            LowMoney +=1 
        elif average_money>=15 and average_money<20:
            HighMoney +=1
        else:
            HighHighMoney +=1
    #各个部分的百分比数字
    the_one_ratio = round(LowLowMoney/allMoney * 100) 
    the_two_ratio = round(LowMoney/allMoney * 100)
    the_three_ratio= round(HighMoney/allMoney*100)
    the_four_ratio = round(HighHighMoney/allMoney*100)      
   
    plt.title('公司薪水分布',fontproperties='SimHei')
    label_list=['月薪0k-10k','月薪10k-15k','月薪15k-20k','月薪20k以上'] #各部分标签
    size=[the_one_ratio,the_two_ratio,the_three_ratio,the_four_ratio]
    color=['red','green','blue','yellow'] #各部分颜色
    explode = [0.05,0,0,0]
    patches, l_text, p_text = plt.pie(size, explode=explode, colors=color, labels=label_list, labeldistance=1.1, autopct="%1.1f%%", shadow=False, startangle=90, pctdistance=0.6)
    plt.axis("equal")    # 设置横轴和纵轴大小相等，这样饼才是圆的
    plt.legend()
    plt.show()

