# example/urls.py
from django.urls import path

from example import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("info/", views.info_page, name="info"),
    path("about/", views.about_page, name="about"),
    path("framework/", views.framework_page, name="framework"),
    path("status/", views.status_view, name="status"),
    path("v1/", views.v1_index, name="v1_index"),
]
