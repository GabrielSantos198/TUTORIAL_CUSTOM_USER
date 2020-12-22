from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView
from .models import User

# Create your views here.

class PageListView(ListView):
    model = User
    template_name = "index.html"


class DetailPageView(DetailView):
    model = User
    template_name = "detail.html"
    context_object_name = "post"


class EditView(UpdateView):
    model = User
    template_name = "edit.html"
    fields = ("username","summary","image")
    success_url = "/"


