from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView, DeleteView
from bookmark.models import Bookmark


# 모델+admin.py ---> view 와 template 코딩
# 함수형, 클래스형 뷰

class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 5

class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'
    # CreateView, UpdateView는 form이 접미사인데, bookmark_create 를 사용하기 위함.
    
class BookmarkDetailView(DetailView):
    model = Bookmark
    
class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    # success_url = reverse_lazy
    template_name_suffix = '_update'