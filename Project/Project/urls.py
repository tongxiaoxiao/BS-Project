"""Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin

from django.conf.urls import include, url
from django.contrib import admin

from app1 import views as app1_views
'''import sys
reload(sys)
sys.setdefaultencoding('utf-8')'''

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/Data_Result/', app1_views.Data_Result),
    url(r'^admin/CreditRating/', app1_views.CreditRating, name='CreditRating'),

    url(r'^index/', app1_views.index,name='index'),
    url(r'^CreditQuery/', app1_views.CreditQuery),
]
