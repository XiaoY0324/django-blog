from django.urls import re_path, path

from . import views

urlpatterns = [
		path('', views.home, name='home'),
    re_path(r'^detail/(?P<my_args>\d+)/$', views.detail, name='detail'),
]