# -*- coding: utf-8 -*-
from django.shortcuts import render,redirect
from django.shortcuts import render
from hashlib import sha1
from df_goods.models import *
from . import user_decorator
from df_goods.models import *
from df_order.models import *
from django.http import JsonResponse,HttpResponseRedirect
from django.core.paginator import Paginator,Page


def add_goods(request):
    context={'title':'用户注册'}
    return render(request,'df_operation/add_goods.html',context)

def addgoods_handle(request):
    #接收用户输入
    post=request.POST
    bname=post.get('book_name')
    aname=post.get('author')
    book_link=request.FILES.get('book_link')
    book_img=request.FILES.get('book_img')
    content=post.get('content')
    gtype=post.get('gtype')
    #创建对象
    good=GoodsInfo()
    good.gtitle=bname
    good.gjianjie=aname
    good.gfile=book_link
    good.gpic=book_img
    good.gcontent=content
    good.gclick=50
    good.gkucun=1000
    good.gprice=2
    good.gunit=1
    good.gtype_id=gtype
    #注册成功，转到登录页面
    good.save()
    return redirect('/operation/add_goods/')