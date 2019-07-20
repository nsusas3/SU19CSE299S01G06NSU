from django.urls import path
from .views import ( 
    QArticleListView,
    QArticleUpdateView,
    QArticleDetailView,
    QArticleDeleteView, # new
    QArticleCreateView,
)
urlpatterns = [
    path('<int:pk>/edit/',
         QArticleUpdateView.as_view(), name='article_edit'), # new
    path('<int:pk>/',
         QArticleDetailView.as_view(), name='article_detail'), # new
    path('<int:pk>/delete/',
         QArticleDeleteView.as_view(), name='article_delete'), # new
    path('new/', QArticleCreateView.as_view(), name='article_new'), # new

    path('', QArticleListView.as_view(), name='article_list'),
]