#coding=utf-8
from django.conf.urls import url, include
import views

urlpatterns = [
    url(r'^$',views.HomeView),
    url(r'^post/(\d+)$',views.post_view),
]
