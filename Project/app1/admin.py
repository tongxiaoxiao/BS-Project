# -*-coding:utf-8 -*-
from __future__ import unicode_literals
from django.contrib import admin
from django.shortcuts import render
from views import Data_Result
from app1 import models
from django.utils.safestring import mark_safe
'''import sys
reload(sys)
sys.setdefaultencoding('utf-8')'''


admin.site.site_header= '上市公司信用评级'
admin.site.site_title = '上市公司信用评级'
class ShowData(admin.ModelAdmin):
    list_display = ['identification','symbolnumber','year','quarter','circulationstock',
                    'incometax','netprofit','accountsreceivable','advancepayment',
                    'stock','totalcurrentassets','fixedassets','intangibleassets',
                    'goodwill','totalcapital','payableaccount','payableinterest',
                    'othercurrentliability','totalcurrentliability','longtermloan',
                    'longtermpayable','totalnoncurrentliability','totalliability',
                    'assetvalue','cashpayment','cashforinterest','depreciation',
                    'amortization','longtermamortization','quickratio',
                    'totalcapitalratioofreturn','assetratioofreturn','volatility',
                    'netfixedassetsrate']
    list_per_page = 50
    ordering = ('identification',)
    search_fields = ('identification', )
    #list_filter = ('symbolnumber','year','quarter')


class ShowData_Result(admin.ModelAdmin):
    def changelist_view(self, request, extra_context=None):
        #self.queryset = self.queryset.filter(editors=request.symbolnumber)
        return Data_Result(request)
    #search_fields = ('identification',)
    #def more(self, obj):
        #return mark_safe("<a href='http://www.baidu.com'>点击</a>")

admin.site.register(models.Data, ShowData)
admin.site.register(models.Data_Result,ShowData_Result)

