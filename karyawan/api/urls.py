from django.conf.urls import url
from django.contrib import admin
from . import views

from karyawan.api.views import(
    KaryawanListAPIView,
    KaryawanDetailAPIView
)

urlpatterns = [
    url(r'^$', KaryawanListAPIView.as_view(), name='list'),
    url(r'^(?P<id>[0-9])/$', views.KaryawanDetailAPIView),
]
