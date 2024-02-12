from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Article
# Create your views here.

def home_view(request):
    return render(request, "home/home.html")

class ArticleListView(ListView):
    model = Article
    template_name = 'home/article_list.html'
    #コンテキスト名を設定
    context_object_name = 'articles'
    

class ArticleDetailView(DetailView):
    model = Article

    template_name = 'home/article_detail.html'   
    #コンテキスト名を設定
    context_object_name = 'article'