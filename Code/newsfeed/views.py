from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from .models import Newsfeed

class NewsfeedListView(ListView):
    model = Newsfeed
    template_name= 'newsfeed_list.html'
