#coding=utf-8
from haystack import  indexes
from blogs.models import *

class PostIndex(indexes.SearchIndex,indexes.Indexable):
    text=indexes.CharField(document=True,use_template=True)


    #设置索引
    title=indexes.NgramField(model_attr='title')
    content=indexes.NgramField(model_attr='content')

    def get_model(self):
        return Post

    def index_queryset(self, using=None):
        return  self.get_model().objects.order_by('-creatime')
