from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger  # 添加分页相关包

from .models import Article
from datetime import datetime

# Create your views here.
def home(request):
	post_list = Article.objects.all()
	paginator = Paginator(post_list, 2) # 每页显示两个
	page = request.GET.get('page') # 当前页码

	try :
		post_list = paginator.page(page)

	except PageNotAnInteger: # 无效页码
		post_list = paginator.page(1)
	except EmptyPage: # 有效页码 但是该页数据为空
		post_list = paginator.paginator(paginator.num_pages) # 取最后一页

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

	return render(request, 'archives.html', { 'post_list' : post_list, 'error': False })

# about me
def about_me(request):
	return render(request, 'aboutme.html')

# 标签分类页
def search_tag(request, tag):
	try:
		post_list = Article.objects.filter(category__iexact = tag) # iexact不区分大小写的精确匹配 区别于contains
	except Article.DoesNotExist:
		raise Http404

	return render(request, 'tag.html', { 'post_list' : post_list })

# 查询
def blog_search(request):
	if 's' in request.GET:
		s = request.GET['s']

		if not s:
			return render(request, 'home.html')
		else:
			post_list = Article.objects.filter(title__icontains = s) # icontains 忽略大小写的包含 
			if len(post_list) == 0:
				return render(request,'archives.html', { 'post_list' : post_list, 'error' : True })
			else:
				return render(request,'archives.html', { 'post_list' : post_list, 'error' : False })

	return redirect('/blog/')























