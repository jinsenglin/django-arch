from django.conf.urls import url

from app2_2 import views


urlpatterns = [
        url(r'^$', views.index, name='index'),
]
