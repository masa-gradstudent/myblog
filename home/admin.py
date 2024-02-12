from django.contrib import admin
from .models import Article
# Register your models here.

# 管理画面の記事一覧を表示する列を指定
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'updated_at')

admin.site.register(Article, ArticleAdmin)

