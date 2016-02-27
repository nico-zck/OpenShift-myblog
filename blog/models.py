from datetime import datetime

from DjangoUeditor.models import UEditorField
from django.core.validators import RegexValidator
from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='分类名称')
    # smallinteger values from -32768 to 32767
    index = models.SmallIntegerField(default=99, verbose_name='分类的序号')

    class Meta:
        verbose_name = '文章类别'
        verbose_name_plural = verbose_name
        ordering = ['index', 'id']

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True, verbose_name='标签名称')

    class Meta:
        verbose_name = '标签'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class ArticleManager(models.Manager):
    def distinct_date(self):
        distinct_date_list = []
        date_list = self.values('publish_datetime')
        for date in date_list:
            date = date['publish_datetime'].strftime('%m/%Y  Articles')
            if date not in distinct_date_list:
                distinct_date_list.append(date)
        return distinct_date_list


class Article(models.Model):
    title = models.CharField(max_length=100, verbose_name='文章标题')
    publish_datetime = models.DateTimeField(default=datetime.now(), verbose_name='发布时间')
    update_datetime = models.DateTimeField(auto_now=True, verbose_name='修改时间')
    category = models.ForeignKey(Category, default=1, blank=True, verbose_name='分类')
    tag = models.ManyToManyField(Tag, blank=True, verbose_name='标签')
    is_allowed_comment = models.BooleanField(default=True, verbose_name='是否允许评论')
    views_count = models.PositiveIntegerField(default=0, verbose_name='浏览量')
    content = UEditorField(verbose_name='文章内容', width=800, height=350, toolbars='full',
                           imagePath='images/%(year)s/%(month)s/%(basename)s_%(datetime)s.%(extname)s', filePath="",
                           upload_settings={"imageMaxSize": 1204000},
                           settings={}, command=None, event_handler=None, blank=True)
    summary = models.TextField(max_length=100, verbose_name='总结摘要')

    objects = ArticleManager()

    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-publish_datetime', '-id']

    def __str__(self):
        return self.title


class Comment(models.Model):
    name = models.CharField(max_length=20, verbose_name='名字')
    email = models.EmailField(blank=True, max_length=50, verbose_name='邮箱地址')
    blog_url = models.URLField(blank=True, max_length=100, verbose_name='个人博客地址')
    comment_datetime = models.DateTimeField(auto_now_add=True, verbose_name='评论时间')
    comment = models.TextField(max_length=300, verbose_name='评论内容')
    article = models.ForeignKey(Article, on_delete=models.CASCADE)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s 说: %s' % (self.name, self.comment)


class Message(models.Model):
    name = models.CharField(max_length=20, verbose_name='名字')
    email = models.EmailField(max_length=50, verbose_name='邮箱地址')
    contact_datetime = models.DateTimeField(auto_now_add=True, verbose_name='留言时间')
    phone_number = models.CharField(blank=True, max_length=12, verbose_name='联系电话',
                                    validators=[RegexValidator(r'^((\d{3,4}-)?\d{7,8})$|(1[3-9][0-9]{9})$')])
    qq_number = models.CharField(blank=True, max_length=11, verbose_name='QQ号',
                                 validators=[RegexValidator(r'^([1-9][0-9]{4,10})$')])
    message = models.TextField(max_length=800, verbose_name='留言内容')

    class Meta:
        verbose_name = '留言'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '%s 说: %s' % (self.name, self.message)
