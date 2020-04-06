"""DJ_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from blog.views import *


urlpatterns = [

    path(r'admin/', admin.site.urls),
    path(r'', login),
    path(r'login/', login),
    path(r'index/', index),
    path(r'delete_user/', delete_user),
    path(r'adduser/', adduser),
    path(r'blog/', blog),
    path(r'comment/', comment),
    path(r'modifyuser/', modifyuser),
    path(r'delete_comment/', delete_comment),
    path(r'addcomment/', addcomment),
    path(r'modifycomment/', modifycomment),
    path(r'addblog/', addblog),
    path(r'search/', search),
    path(r'modifyblog/', modifyblog),

]
