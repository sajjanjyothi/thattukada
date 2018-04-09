from django.conf.urls import url 
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    url(r'^list$', views.list, name='list'),
    url(r'^newentry$', views.newentry, name='new'),
    url(r'^delete/(?P<pk>\d+)/', views.delete, name='delete'),
    url(r'^update/(?P<pk>\d+)/', views.update, name='update'),
    url(r'^search', views.search, name='search'),
    url(r'^export', views.export, name='export'),
    url(r'^sales', views.sales, name='sales'),
]