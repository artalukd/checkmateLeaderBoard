from django.conf.urls import url, include
from . import views


urlpatterns = [
	url(r'^get$', views.getData, name = 'getData'),
    url(r'^refresh$', views.refresh, name = 'refresh'),
]
