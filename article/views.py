from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from .models import Article
from datetime import datetime

# Create your views here.
def home(request):
	post_list = Article.objects.all()

	return render(request, 'home.html', { 'post_list': post_list })

def detail(request, id):
	print('---------')
	post = get_object_or_404(Article, id = str(id))

	# str = ('title = %s, category = %s, date_time = %s, content= %s' % (post.title, post.category, post.date_time, post.content ))

	# return HttpResponse(post)
	return render(request, 'post.html', { 'post' : post })

# 归档页
def archives(request):
	try:
		post_list = Article.objects.all()
	except Article.DoesNotExist:
		raise Http404

	print(post_list)
	return render(request, 'archives.html', { 'post_list' : post_list, 'error' : False })

# about me
def about_me(request):
	return render(request, 'aboutme.html')