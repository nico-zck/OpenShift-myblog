from django.conf import settings
from django.core.paginator import Paginator, EmptyPage, InvalidPage, PageNotAnInteger
from django.shortcuts import render

from blog.forms import *
from blog.models import *


# Create your views here.

# Get your site settings from settings.py
def global_settings(request):
    SITE_NAME = settings.SITE_NAME
    SITE_OWNER = settings.SITE_OWNER
    SITE_DESCRIPTION = settings.SITE_DESCRIPTION
    archive_list = Article.objects.distinct_date()[:6]
    categories_list = Category.objects.all()
    return locals()


def make_pages(request, articles_list):
    paginator = Paginator(articles_list, 6)
    try:
        page = int(request.GET.get('page', 1))
        articles_list = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        articles_list = paginator.page(1)
    return articles_list


def index(request):
    articles_list = Article.objects.all()
    articles_list = make_pages(request, articles_list)
    return render(request, 'index.html', locals())


def archive(request, year, month):
    try:
        articles_list = Article.objects.filter(publish_datetime__icontains=year + '-' + month)
    except Exception:
        return
    articles_list = make_pages(request, articles_list)
    return render(request, 'index.html', locals())


def category(request, cid):
    try:
        article_list = Article.objects.filter(category_id__exact=cid)
    except Exception:
        return
    articles_list = make_pages(request, article_list)
    return render(request, 'index.html', locals())


def article(request, aid):
    art = Article.objects.get(pk=aid)
    Article.objects.filter(pk=aid).update(views_count=(art.views_count + 1))
    # 获取评论表单对象
    # comment_form = CommentForm(initial={'article': aid})
    # 自定义评论Form处理
    # if request.method == 'POST':
    #     comment_form = CommentForm(request.POST)
    #     if comment_form.is_valid():
    #         comment = comment_form.save()
    #         comment.save()
    return render(request, 'single.html', locals())


def about(request):
    return render(request, 'about.html')


def contact(request):
    contact_form = MessageForm()
    # 自定义留言Form处理
    if request.method == 'POST':
        contact_form = MessageForm(request.POST)
        if contact_form.is_valid():
            message = contact_form.save()
            message.save()
    return render(request, 'contact.html', locals())
