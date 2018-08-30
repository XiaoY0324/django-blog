from django.urls import re_path, path

from . import views

urlpatterns = [
		path('', views.home, name='home'),
    path('<int:id>/', views.detail, name='detail'),
    path('archives/', views.archives, name = 'archives'),
    path('about_me/', views.about_me, name = 'about_me'),
    re_path(r'^tag(?P<tag>\w+)/$', views.search_tag, name = 'search_tag'),
    path('search/', views.blog_search, name = 'search')
]