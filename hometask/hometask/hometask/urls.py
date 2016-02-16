from django.conf.urls import include, url
from django.contrib import admin
admin.autodiscover()
urlpatterns = [

	url(r'^twitts/', include('twitts.urls')),
	]

