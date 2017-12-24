from django.conf.urls import url
from itemdex import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
]
