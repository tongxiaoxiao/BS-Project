# -*-coding:utf-8 -*-

#!/usr/bin/env python

#from __future__ import unicode_literals
from django.shortcuts import render,render_to_response
from app1.models import Data
from django.http import HttpResponse
import MySQLdb
import MySQLdb as db
from io import BytesIO
import math
import pandas
import jupyter
import seaborn

import numpy as np
np.seterr(divide='ignore',invalid='ignore')
import scipy.stats  #from scipy import stats
import matplotlib.pyplot as plt

'''
con = db.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd='123456',
    db='DB',
)'''
con = db.connect('localhost', 'root', '123456', 'DB');
cur = con.cursor()
cur.execute("SET NAMES 'utf8'")
cur.execute("SET character_set_results='utf8'")
# Create your views here.
def Data_Result(request):
    con = db.connect('localhost', 'root', '123456', 'DB');
    cur = con.cursor()
    cur.execute("SET NAMES 'utf8'")
    cur.execute("SET character_set_results='utf8'")
    '''list=models.Data.objects.all().values(
                    'identification','symbolnumber','year','quarter','circulationstock',
                    'incometax','netprofit','accountsreceivable','advancepayment',
                    'stock','totalcurrentassets','fixedassets','intangibleassets',
                    'goodwill','totalcapital','payableaccount','payableinterest',
                    'othercurrentliability','totalcurrentliability','longtermloan',
                    'longtermpayable','totalnoncurrentliability','totalliability',
                    'assetvalue','cashpayment','cashforinterest','depreciation',
                    'amortization','longtermamortization','quickratio',
                    'totalcapitalratioofreturn','assetratioofreturn','volatility',
                    'netfixedassetsrate','companyname','identification')'''

    cur.execute("SELECT * FROM Data")
    data = cur.fetchall()
    basic = np.array(data)
    # default structure
    symbolnumber = np.array(basic[:, 0])
    year = np.array(basic[:, 2])
    quarter = np.array(basic[:, 3])
    P20 = np.array(basic[:, 4])
    P20 = P20.astype('float64')
    P22 = np.array(basic[:, 5])
    P22 = P22.astype('float64')
    B4 = np.array(basic[:, 6])
    B4 = B4.astype('float64')
    B5 = np.array(basic[:, 7])
    B5 = B5.astype('float64')
    B10 = np.array(basic[:, 8])
    B10 = B10.astype('float64')
    B14 = np.array(basic[:, 9])
    B14 = B14.astype('float64')
    B20 = np.array(basic[:, 10])
    B20 = B20.astype('float64')
    B26 = np.array(basic[:, 11])
    B26 = B26.astype('float64')
    B28 = np.array(basic[:, 12])
    B28 = B28.astype('float64')
    B33 = np.array(basic[:, 13])
    B33 = B33.astype('float64')
    B37 = np.array(basic[:, 14])
    B37 = B37.astype('float64')
    B41 = np.array(basic[:, 15])
    B41 = B41.astype('float64')
    B46 = np.array(basic[:, 16])
    B46 = B46.astype('float64')
    B47 = np.array(basic[:, 17])
    B47 = B47.astype('float64')
    B48 = np.array(basic[:, 18])
    B48 = B48.astype('float64')
    B50 = np.array(basic[:, 19])
    B50 = B50.astype('float64')
    B55 = np.array(basic[:, 20])
    B55 = B55.astype('float64')
    B56 = np.array(basic[:, 21])
    B56 = B56.astype('float64')
    B67 = np.array(basic[:, 22])
    B67 = B67.astype('float64')
    C17 = np.array(basic[:, 23])
    C17 = C17.astype('float64')
    C28 = np.array(basic[:, 24])
    C28 = C28.astype('float64')
    C36 = np.array(basic[:, 25])
    C36 = C36.astype('float64')
    C37 = np.array(basic[:, 26])
    C37 = C37.astype('float64')
    C38 = np.array(basic[:, 27])
    C38 = C38.astype('float64')
    F2 = np.array(basic[:, 28])
    F2 = F2.astype('float64')
    F20 = np.array(basic[:, 29])
    F20 = F20.astype('float64')
    F21 = np.array(basic[:, 30])
    F21 = F20.astype('float64')
    F33 = np.array(basic[:, 31])
    F33 = F33.astype('float64')
    F52 = np.array(basic[:, 32])
    F52 = F52.astype('float64')
    cnname = np.array(basic[:, 33])
    identification = np.array(basic[:,34])

    # SS
    # SS1
    capitalstructure = B56 / B33
    interestcover1 = P22 + P20 + C36 + C37 + C38 + C28
    interestcover = B41 / interestcover1
    ss1 = capitalstructure * interestcover
    ss2 = np.sqrt(ss1)
    SS1 = 5 * ss2
    # SS2
    profitability1 = P22 + C28
    profitability2 = B20 * F52
    profitability3 = P22 + C28 + C36 + C37 + C38 - C17 - B14 + B47
    profitability4 = B14 + profitability2 + B28 + B26 + B10 + B4 + B5 - profitability3 - B37 - B46 - B48
    profitability = profitability1 / profitability4
    SS2 = 4 * profitability
    # SS3
    SS3 = 1.5 * F2
    SS = SS1 - SS2 - SS3
    SS = np.fabs(SS)
    SS = np.ceil(SS)
    where_are_nan = np.isnan(SS)
    SS[where_are_nan] = 1

    # DD
    dd1 = np.log(B67)
    dd2 = F21
    dd3 = F33 * np.sqrt(252)
    dd4 = np.square(dd3)
    dd5 = dd4 / 2
    dd6 = np.log(B56)
    dd7 = F33 * np.sqrt(252)
    DD1 = dd1 + dd2 - F20 - dd5 - dd6

    if ((dd7 == 0).all()):
        DD = DD1
    else:
        DD = DD1 / dd7

    DD = np.fabs(DD)
    DD = np.ceil(DD)
    where_are_nan = np.isnan(DD)
    DD[where_are_nan] = 1
    where_are_inf = np.isinf(DD)
    DD[where_are_inf] = 1

    Score = 3.5 * SS + 3.5 * DD

    CR = np.chararray(33001)
    i = 0
    l = len(Score)
    while i < l:
        if Score[i] < 14:
            CR[i] = 'S'
            i = i + 1
        elif Score[i] >= 14 and Score[i] < 28:
            CR[i] = 'A'
            i = i + 1
        elif Score[i] >= 28 and Score[i] < 35:
            CR[i] = 'B'
            i = i + 1
        elif Score[i] >= 35 and Score[i] < 49:
            CR[i] = 'C'
            i = i + 1
        elif Score[i] >= 49 and Score[i] < 56:
            CR[i] = 'D'
            i = i + 1
        elif Score[i] >= 56 and Score[i] < 63:
            CR[i] = 'E'
            i = i + 1
        else:
            CR[i] = 'F'
            i = i + 1

    SS = np.transpose(SS)
    SS.shape = (33001, 1)
    DD = np.transpose(DD)
    DD.shape = (33001, 1)
    identification = np.transpose(identification)
    identification.shape = (33001, 1)
    symbolnumber = np.transpose(symbolnumber)
    symbolnumber.shape = (33001, 1)
    year = np.transpose(year)
    year.shape = (33001, 1)
    quarter = np.transpose(quarter)
    quarter.shape = (33001, 1)
    cnname = np.transpose(cnname)
    cnname.shape = (33001, 1)
    Score = np.transpose(Score)
    Score.shape = (33001,1)
    CR = np.transpose(CR)
    CR.shape = (33001, 1)
    result = np.hstack((identification, cnname, symbolnumber, year,
                        quarter, SS, DD, Score,CR))


    theads = ['关键词', '企业' ,'代码', '年份',
              '季度', '偿付能力得分(SolvencyScore)',
              '违约距离(DistancetoDefault)', '信用评级得分','级别','说明']

    records = [(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8]) for x in result]
    return render_to_response('Data_Result.html',
                              {'theads':theads,'trows':records})
def CreditRating(request):
    return render_to_response("CreditRating.html",{})


def index(request):
    return render(request, 'CreditQuery.html')
def CreditQuery(request):
    p20 = request.GET['p20']
    p20 = float(p20)
    ansp20 = p20
    p22 = request.GET['p22']
    p22 = float(p22)
    ansp22 = p22
    b4 = request.GET['b4']
    b4 = float(b4)
    ansb4 = b4
    b5 = request.GET['b5']
    b5 = float(b5)
    ansb5 = b5
    b10 = request.GET['b10']
    b10 = float(b10)
    ansb10 = b10
    b14 = request.GET['b14']
    b14 = float(b14)
    ansb14 = b14
    b20 = request.GET['b20']
    b20 = float(b20)
    ansb20 = b20
    b26 = request.GET['b26']
    b26 = float(b26)
    ansb26 = b26
    b28 = request.GET['b28']
    b28 = float(b28)
    ansb28 = b28
    b33 = request.GET['b33']
    b33 = float(b33)
    ansb33 = b33
    b37 = request.GET['b37']
    b37 = float(b37)
    ansb37 = b37
    b41 = request.GET['b41']
    b41 = float(b41)
    ansb41 = b41
    b46 = request.GET['b46']
    b46 = float(b46)
    ansb46 = b46
    b47 = request.GET['b47']
    b47 = float(b47)
    ansb47 = b47
    b48 = request.GET['b48']
    b48 = float(b48)
    ansb48 = b48
    b50 = request.GET['b50']
    b50 = float(b50)
    ansb50 = b50
    b55 = request.GET['b55']
    b55 = float(b55)
    ansb55 = b55
    b56 = request.GET['b56']
    b56 = float(b56)
    ansb56 = b56
    b67 = request.GET['b67']
    b67 = float(b67)
    ansb67 = b67
    c17 = request.GET['c17']
    c17 = float(c17)
    ansc17 = c17
    c28 = request.GET['c28']
    c28 = float(c28)
    ansc28 = c28
    c36 = request.GET['c36']
    c36 = float(c36)
    ansc36 = c36
    c37 = request.GET['c37']
    c37 = float(c37)
    ansc37 = c37
    c38 = request.GET['c38']
    c38 = float(c38)
    ansc38 = c38
    f2 = request.GET['f2']
    f2 = float(f2)
    ansf2 = f2
    f20 = request.GET['f20']
    f20 = float(f20)
    ansf20 = f20
    f21 = request.GET['f21']
    f21 = float(f21)
    ansf21 = f21
    f33 = request.GET['f33']
    f33 = float(f33)
    ansf33 = f33
    f52 = request.GET['f52']
    f52 = float(f52)
    ansf52 = f52

    ss1 = b56 / b33
    ss2 = p22 + p20 + c36 + c37 + c38 + c28
    ss3 = b41 / ss2
    ss4 = ss1 * ss3
    ss5 = math.sqrt(ss4)
    SS1 = 5 * ss5

    ss7 = p22 + c28 + c36 + c37 + c38 - c17 - b14 + b37
    ss8 = b20 * f52
    ss9 = b14 + ss8 + b28 + b26 + b10 + b4 + b5 - ss7 - b37 - b46 - b48
    ss10 = p22 + c28
    ss11 = ss10 / ss9
    SS2 = 4 * ss11

    SS3 = 1.5 * f2

    SS = SS1 - SS2 - SS3
    SS = math.fabs(SS)
    SS = math.ceil(SS)
    ansSS = SS

    dd1 = math.log(b67)
    dd2 = f21
    dd3 = f33 * math.sqrt(252)
    dd4 = math.pow(dd3,2)
    dd5 = dd4 / 2
    dd6 = math.log(b56)
    dd7 = f33 * math.sqrt(252)
    DD1 = dd1 + dd2 - f20 - dd5 - dd6

    if (dd7 == 0):
        DD = DD1
    else:
        DD = DD1 / dd7
    DD = math.fabs(DD)
    DD = math.ceil(DD)
    ansDD = DD

    CR = SS * 3.5 + DD * 3.5
    ansCR = CR

    if CR < 14:
        R = 'S'
    elif CR >= 14 and CR < 28:
        R = 'A'
    elif CR >= 28 and CR < 35:
        R = 'B'
    elif CR >= 35 and CR < 49:
        R = 'C'
    elif CR >= 49 and CR < 56:
        R = 'D'
    elif CR >= 56 and CR < 63:
        R = 'E'
    else:
        R = 'F'

    if R == 'S':
        RR = '极低的违约风险。被评为S级的企业通常运营范围广泛，业务不确定性低，并且可以轻松支付所有未结的到期日和目前现金以及一年的自由现金流量。'
    elif R == 'A':
        RR = '非常低的违约风险。被评为A的企业倾向于宽幅或窄幅的经济保护性，业务不确定性中低度，现金流比率具有较高的安全性，防止不利发展。'
    elif R == 'B':
        RR = '低违约风险。被评为B的企业包括宽幅或窄幅的经济保护性，业务不确定性中至高，现金流比率具有较高的安全性，可防止不利发展。'
    elif R == 'C':
        RR = '中等违约风险。发行人评为C的企业通常包括窄幅或无经济保护性，业务不确定性中至高，现金流比率提供适度的安全边际以防止恶化的商业环境。'
    elif R == 'D':
        RR = '高于平均违约风险。评级为D的企业通常不包括经济保护性，业务不确定性高至非常高，现金流比率提供较小安全边际以防止恶化的商业条件。'
    elif R == 'E':
        RR = '违约风险高。评级为E的企业通常不包括经济保护性，业务不确定性很高，现金流比率无法提供保护作用，说明企业对有利的商业条件有很大依赖性。'
    else:
        RR = '目前违约风险很高。评级为F的企业通常不包括经济保护性，业务不确定性极高，现金流比率无法提供保护作用，企业极度依赖有利的商业条件以避免违约或重大资本重组。'
    ansR = R
    ansRR = RR
    return render_to_response('CreditQuery.html',locals())
