from django.conf.urls import url
from django.contrib import admin

from kehadiran.api.views import(
    KehadiranListAPIView,
    KehadiranRetrieveAPIView
)

urlpatterns = [
    url(r'^$', KehadiranListAPIView.as_view(), name='list'),
    url(r'^(?P<id>\d+)/$', KehadiranRetrieveAPIView.as_view(), name='detail'),
]
