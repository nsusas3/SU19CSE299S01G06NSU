from django.shortcuts import render
from django.views.generic import ListView
from .models import Newsfeed

# Create your views here.

class NewsFeedView(ListView):
    model = Newsfeed
    template_name = 'newsfeed_list.html'
