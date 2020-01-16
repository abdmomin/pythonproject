from django.conf.urls import url
from . import views
from .views import DestListView


urlpatterns = [
    url(r'^$', DestListView.as_view(), name='index'),
    url(r'details/(?P<pk>\d+)/$', views.details, name='details'),
]
