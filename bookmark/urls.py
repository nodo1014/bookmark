# from os import path
from django.urls import path
# from bookmark.views import BookmarkCreateView, BookmarkDetailView, BookmarkListView
from .views import *
# url 네임스페이스
# <a href="{% url 'detail' pk=bookmark.id %}">{{bookmark.site_name}}</a>

urlpatterns = [
    path('', BookmarkListView.as_view(), name='list'),
    path('add/', BookmarkCreateView.as_view(), name='add'),
    path('detail/<int:pk>', BookmarkDetailView.as_view(), name='detail'),
    path('update/<int:pk>', BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', BookmarkDeleteView.as_view(), name='delete'),
]