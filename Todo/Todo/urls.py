from django.conf.urls import patterns, include, url
from django.conf.urls.defaults import *
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Todo.views.home', name='home'),
    # url(r'^Todo/', include('Todo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^todo/$','Todo.todolist.views.index',name='index'),
     url(r'^todolist/(?P<poll_id>\d+)/$','Todo.todolist.views.detail',name='detail'),
     url(r'^todolist/(?P<poll_id>\d+)/results/$','Todo.todolist.views.results',name='results'),
     url(r'^todolist/(?P<poll_id>\d+)/vote/$','Todo.todolist.views.vote',name='vote'),
     url(r'^admin/', include(admin.site.urls)),
)
