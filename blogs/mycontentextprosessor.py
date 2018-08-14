#coding=utf-8

from  models import *
def getrightinfo(request):
    #分类信息
    from django.db.models import  Count
    cate_posts=Post.objects.values('category__cname','category')