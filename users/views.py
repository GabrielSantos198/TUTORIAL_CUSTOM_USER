from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import User

# Create your views here.

class PageListView(ListView):
    model = User
    template_name = "index.html"


class DetailPageView(DetailView):
    model = User
    template_name = "detail.html"



