from tkinter import *
import tkinter.messagebox
from tkinter.filedialog import askopenfilename
import os
from bs4 import BeautifulSoup
import requests
from xlwt import *
import xlsxwriter
import xlrd
import time
import json
from pathlib import Path
Infor = []
       
listss = {
    #技术
    'php':'c101010100-p100103',
    'java':'c101010100-p100101',
    'web前端':'c101010100-p100901',
    'html5':'c101010100-p100201',
    'ios':'c101010100-p100203',
    'android':'c101010100-p100202',
    'javascript':'c101010100-p100208',
    'python':'c101010100-p100109',
    #产品
    '产品经理':'c101010100-p110101',
    '产品总监':'c101010100-p110302',
    '游戏策划':'c101010100-p110107',
    '高端产品职位':'c101010100-p110399',
    '游戏制作人':'c101010100-p110303',
    '其他产品职位':'c101010100-p110401',
    #设计
    'ui设计师':'c101010100-p120105',
    '平面设计师':'c101010100-p120106',
    '网页设计师':'c101010100-p120102',
    '交互设计师':'c101010100-p120201',
    '插画师':'c101010100-p120121',
    '数据分析师':'c101010100-p120301',
    #运营
    '产品运营':'c101010100-p130102',
    '新媒体运营':'c101010100-p130111',
    '游戏运营':'c101010100-p130108',
    '数据运营':'c101010100-p130103',
    '编辑':'c101010100-p130299',
    '客服':'c101010100-p130303',
    #市场
    '市场营销':'c101010100-p140101',
    '市场推广':'c101010100-p140104',
    '市场策划':'c101010100-p140102',
    '市场顾问':'c101010100-p140103',
    '公关媒介':'c101010100-p140299',
    '广告':'c101010100-p140699',
    #人事
    'hr':'c101010100-p150104',
    '行政':'c101010100-p150204',
    '财务':'c101010100-p150303',
    '人力资源经理':'c101010100-p150403',
    '行政经理':'c101010100-p150401',
    '出纳':'c101010100-p150302',
    #高级管理
    'CEO':'c101010100-p150407',
    '副总裁':'c101010100-p150408',
    '总经理':'c101010100-p150411',
    '董事长秘书':'c101010100-p150414',
    #销售
    '销售专员':'c101010100-p140301',
    '销售经理':'c101010100-p140302',
    '客户代表':'c101010100-p140303',
    '销售管理':'c101010100-p160199',
    '商务总监':'c101010100-p140403',
    '团队经理':'c101010100-p160104',
}



def getJobList(url):
    headrs = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.81 Safari/537.36",
        "accept-encoding": "gzip, deflate, br",
        "accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "cookie":"lastCity=101010100; sid=sem_pz_bdpc_dasou_title; __c=1557886691; __g=sem_pz_bdpc_dasou_title; __l=l=%2Fwww.zhipin.com%2F%3Fsid%3Dsem_pz_bdpc_dasou_title&r=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fDIFkY0IWPB0KZEgsZmIVVT00000Kd7ZNC000002hH8y_.THdBULP1doZA8QMu1x60UWdBmy-bIfK15yczmvwhn101nj0snjKBPWm0IHY1PbRsPH-Df1nYfHnzPHujP164fY77nHf3wDmknHI7r0K95gTqFhdWpyfqn1czPjmsPjnYrausThqbpyfqnHm0uHdCIZwsT1CEQLILIz4lpA-spy38mvqVQ1q1pyfqTvNVgLKlgvFbTAPxuA71ULNxIA-YUAR0mLFW5HDYrH6L%26tpl%3Dtpl_11534_19713_15764%26l%3D1511867677%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253DBoss%2525E7%25259B%2525B4%2525E8%252581%252598%2525E2%252580%252594%2525E2%252580%252594%2525E6%252589%2525BE%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E6%252588%252591%2525E8%2525A6%252581%2525E8%2525B7%25259F%2525E8%252580%252581%2525E6%25259D%2525BF%2525E8%2525B0%252588%2525EF%2525BC%252581%2526xp%253Did(%252522m3224604348_canvas%252522)%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D8%26ie%3Dutf-8%26f%3D3%26tn%3Dbaidu%26wd%3Dboss%25E7%259B%25B4%25E8%2581%2598%25E5%25AE%2598%25E7%25BD%2591%26oq%3Dpython%252520%2525E7%252588%2525AC%2525E5%25258F%252596boss%26rqlang%3Dcn%26inputT%3D2943%26prefixsug%3Dboss%26rsp%3D1&g=%2Fwww.zhipin.com%2F%3Fsid%3Dsem_pz_bdpc_dasou_title; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1557886691; _uab_collina=155788669108862409788549; JSESSIONID=497B7226F56E5830A65A918DF5A4CB4A; __a=43943888.1557886691..1557886691.22.1.22.22; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1557887551",
        "referer":"https://www.zhipin.com/?sid=sem_pz_bdpc_dasou_title"
        }
    res = requests.get(url,headers = headrs)
    soup = BeautifulSoup(res.text,'html.parser')
    return soup.find_all(name='div',attrs={'class':'job-list'})

def getInformation(InUrl):
    ul = getJobList(InUrl)[0].find_all(name='li')
    for i in ul:
        Recruitment = i.find(name='div',attrs={'class':'job-title'}).contents[0]
        salary = i.find(name='span',attrs={'class':'red'}).contents[0]
        urls = i.find(name='h3',attrs={'class':'name'}).a['href']
        AbsoluteUrl = 'https://www.zhipin.com'+urls
        CorporateName = i.find(name='div',attrs={'class':'info-company'}).find(name='h3',attrs={'class':'name'}).a.contents[0]
        address = i.find(name='div',attrs={'class':'info-primary'}).p.contents[0]
        WorkTime = i.find(name='div',attrs={'class':'info-primary'}).p.contents[2]
        Eduction = i.find(name='div',attrs={'class':'info-primary'}).p.contents[4]
        dict = {
            '招聘方向':Recruitment,
            '薪资待遇':salary,
            'boss地址':AbsoluteUrl,
            '公司名称':CorporateName,
            '工作地点':address,
            '工作经验时长':WorkTime,
            '学历要求':Eduction
        }
        Infor.append(dict)
        
def EstablishXsl(name):
    names = name+'.xlsx'
    workbook = xlsxwriter.Workbook(names)
    worksheet = workbook.add_worksheet('demo')
    bold_format = workbook.add_format({'align':'center','valign':'vcenter','bold':True})
    align_format = workbook.add_format({'align':'center','valign':'vcenter'})
    worksheet.write('A1','招聘方向',bold_format)
    worksheet.write('B1','薪资待遇',bold_format)
    worksheet.write('C1','boss地址',bold_format)
    worksheet.write('D1','公司名称',bold_format)
    worksheet.write('E1','工作地点',bold_format)
    worksheet.write('F1','工作经验时长',bold_format)
    worksheet.write('G1','学历要求',bold_format)
    worksheet.set_column("A:A",20)
    worksheet.set_column("B:B",20)
    worksheet.set_column("C:C",70)
    worksheet.set_column("D:D",20)
    worksheet.set_column("E:E",20)
    worksheet.set_column("F:F",30)
    worksheet.set_column("G:G",20)
    row = 1
    col = 0
    for i in Infor:
        worksheet.write_string(row,col,i['招聘方向'],align_format)
        worksheet.write_string(row,col+1,i['薪资待遇'],align_format)
        worksheet.write_string(row,col+2,i['boss地址'],align_format)
        worksheet.write_string(row,col+3,i['公司名称'],align_format)
        worksheet.write_string(row,col+4,i['工作地点'],align_format)
        worksheet.write_string(row,col+5,i['工作经验时长'],align_format)
        worksheet.write_string(row,col+6,i['学历要求'],align_format)
        row += 1
    workbook.close()


def loding(i):
   #print('第'+i+'页正在下载，请稍后,loading',end='')
    for i in range(10):
       # print('.',end='',flush=True)
        time.sleep(0.3)

def go(name,start,end):
    urls = listss[name]
    start = int(start)
    end = int(end)
    for i in range(start,end):
        time.sleep(5) #防止ip地址被封
        i = str(i)
        url = ''.join(['https://www.zhipin.com/',urls,'/?page=',i,"&ka=page-",i])
        loding(i)
        getInformation(url)
       # print('第'+i+'页下载完成')
        EstablishXsl(name)
    return 'ok'

# def ggo(name,start,end):
#     return 'ok'

# go('python',1,5)