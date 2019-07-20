from django.views.generic import ListView, DetailView # new
from django.views.generic.edit import UpdateView, DeleteView, CreateView # new from django.urls import reverse_lazy # new
from .models import QAarticle
from django.urls import reverse_lazy # new
class QArticleListView(ListView): 
    model = QAarticle
    template_name = 'article_list.html'