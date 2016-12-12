"""DrawingManagementSystem URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from drawingManageApp.views import loadDrawingsRequest, addDrawingRecord, updateDrawingRecord
from drawingSearchApp.search import *
from drawingSearchApp.views import *


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^drawingManagement/', TemplateView.as_view(template_name="drawingManagementPage.html")),

    url(r'^loadDrawings/', loadDrawingsRequest, name="loadDrawingsURL"),
    url(r'^addDrawing/', addDrawingRecord, name="addDrawingURL"),
    url(r'^updateDrawing/', updateDrawingRecord, name="updateDrawingURL"),
    url(r'^searchDrawing/', DrawingSearch, name="DrawingSearchURL"),    
    url(r'^search/', searchDrawing, name="searchDrawingURL"),    

]
