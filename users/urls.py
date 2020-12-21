from django.urls import path
from . import views

urlpatterns = [
    path("", views.PageListView.as_view(), name="home"),
    path("detail/<slug:slug>", views.DetailPageView.as_view(), name="detail"),
]
