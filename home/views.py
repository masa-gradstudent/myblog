from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Article
from .forms import CommentForm


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #投稿されたコメントの全権を取得
        comments = self.object.comments.all()
        #コメントフォームを設置
        form = CommentForm()
        context.update({
            'comments': comments, 
            'form': form,
        })
        return context
    
    #POSTで呼び出された場合はコメントを登録
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = CommentForm(data=self.request.POST or None)
        #フォームの入力値に問題がなければ、投稿に紐づけてから登録する
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = self.object
            comment.save()
 
        return redirect('post_detail', pk=self.object.pk)
