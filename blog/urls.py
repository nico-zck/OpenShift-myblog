from django.conf.urls import url

from blog import views

urlpatterns = [
    url(r'^$|index/$', views.index, name='index'),
    url(r'^article/(?P<aid>\d{0,6})/$', views.article, name='article'),
    url(r'^about/', views.about, name='about'),
    url(r'^contact/', views.contact, name='contact'),
    url(r'^archive/(?P<year>\d{4})/(?P<month>\d{2})/$', views.archive, name='archive'),
    url(r'^category/(?P<cid>\d{1,6})/$', views.category, name='category')
]
