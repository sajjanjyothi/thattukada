from django.conf.urls import url 

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list$', views.list, name='list'),
    url(r'^newentry$', views.newentry, name='new'),
    url(r'^delete/(?P<pk>\d+)/', views.delete, name='delete'),
    url(r'^update/(?P<pk>\d+)/', views.update, name='update'),
    url(r'^search', views.search, name='search'),
]