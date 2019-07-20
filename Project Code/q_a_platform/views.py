from django.views.generic import ListView, DetailView # new
from django.views.generic.edit import UpdateView, DeleteView, CreateView # new from django.urls import reverse_lazy # new
from .models import QAarticle
from django.urls import reverse_lazy # new
class QArticleListView(ListView): 
    model = QAarticle
    template_name = 'article_list.html'

class QArticleDetailView(DetailView): # new 
    model = QAarticle
    template_name = 'article_detail.html'


class QArticleUpdateView(UpdateView): # new 
    model = QAarticle
    fields = ('title', 'body',)
    template_name = 'article_edit.html'


class QArticleDeleteView(DeleteView): # new
    model = QAarticle
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')