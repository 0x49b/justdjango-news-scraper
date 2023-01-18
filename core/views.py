from django.shortcuts import render
from django.views import generic
from .models import NewsItem

# Create your views here.
class NewsItemListView(generic.ListView):
    model = NewsItem
    template_name = 'news_item_list.html'