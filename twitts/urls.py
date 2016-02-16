from django.conf.urls import include, url
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'myblog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^search/$', views.search, name='search'),
	url(r'^$', views.main, name='main'),

]
