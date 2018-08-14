# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from blogs.models import *
# Create your views here.

def HomeView(request):
    postList=Post.objects.all().order_by('-creatime')
    return render(request,'home.html',{'postlist':postList})

#显示全文
def post_view(request,postid):
    postid=int(postid)
    post= Post.objects.get(id=postid)
    return render(request,'detail.html',{'post':post})