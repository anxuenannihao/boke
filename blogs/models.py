# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
#创建分类
from ckeditor_uploader.fields import RichTextUploadingField
class  Category(models.Model):
    cname=models.CharField(max_length=30,unique=True,verbose_name=u'类别名称')
    class Meta:
        db_table='t_category'
        verbose_name_plural=u'类别'
    def __unicode__(self):
        return u'Category:%s'%self.cname
#标签
class Tag(models.Model):
    tname=models.CharField(max_length=30,unique=True,verbose_name=u'标签名')
    class Meta:
        db_table = 't_tag'
        verbose_name_plural = u'标签'
    def __unicode__(self):
        return u'Category:%s' % self.tname

#内容交互
class Post(models.Model):
    #标题
      title=models.CharField(max_length=30 ,verbose_name=u'标题')
    #描述
      desc=models.TextField(verbose_name=u'描述')
    #内容
      content=RichTextUploadingField(null=True,blank=True)
    #分类
      category=models.ForeignKey(Category,verbose_name=u'所属类别')
    #标签
      tags=models.ManyToManyField(Tag,verbose_name=u'标签')
    #创建时间
      creatime=models.DateField(auto_now_add=True,verbose_name='创建时间')

      class Meta:
         db_table='t_post'
         verbose_name_plural=u'内容'


      def __unicode__(self):
           return 'Post:%s' % self.title

