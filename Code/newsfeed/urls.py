from django.urls import path

from .views import NewsfeedListView


urlpatterns = [
    path('', NewsfeedListView.as_view(), name='newsfeed_list'),
]