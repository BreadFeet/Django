"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from css import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('html5', views.html5, name='html5'),
    path('css', views.css, name='css'),
    path('js', views.js, name='js'),
    path('jq', views.jq, name='jq'),
    path('ajax', views.ajax, name='ajax'),

    path('login', views.login, name='login'),
    path('loginimpl', views.loginimpl, name='loginimpl'),
    path('register', views.reg, name='register'),
    path('regimpl', views.regimpl, name='registerimpl'),

    path('logout', views.logout, name='logout'),

    path('userli', views.userli, name="userlist"),
    path('userdtl', views.userdtl, name='userdetail'),
    path('itemli', views.itemli, name="itemlist"),
    path('itemdtl', views.itemdtl, name='itemdetail'),
    path('additem', views.additem, name="additem"),
    path('additemimpl', views.addimpl, name="addimpl"),

]
