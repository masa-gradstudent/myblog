from django.contrib import admin
from .models import Article, Comment
from django.urls import reverse
from django.db import models
from django.utils.html import format_html
# Register your models here.

# 管理画面の記事一覧を表示する列を指定
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')

#投稿詳細管理画面にコメントも追加
class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0
    fields = ('author', 'text', 'approved_comment')
 
class ArticleAdmin(admin.ModelAdmin):
     list_display = ('title', 'created_at', 'updated_at', 'get_comment_count')
     inlines = (CommentInline,)
    
     #コメント数を測定して、記事一覧画面に反映
     def get_comment_count(self, obj):
          return obj.comments.count()
 
     get_comment_count.short_description = 'Comment Count'

class CommentAdmin(admin.ModelAdmin):
    list_display = ('text', 'get_post_link', 'author', 'created_at', 'approved_comment')
    #フィルターフィールドを追加
    list_filter = ('approved_comment', 'created_at',)
    #検索フィールドを追加
    search_fields = ('text', 'article__title', 'author')
    #編集不可フィールドを追加
    readonly_fields = ('created_at',)
 
    #コメントに紐づく投稿名と編集画面へのリンク追加
    def get_post_link(self, obj):
        url = reverse('admin:home_article_change', args=[obj.article.id])
        return format_html("<a href='{}'>{}</a>", url, obj.article.title)
 
    get_post_link.short_description = 'Article'

admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
