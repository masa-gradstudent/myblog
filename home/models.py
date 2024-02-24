from django.db import models

# 投稿記事（Article）
class Article(models.Model):
    title = models.CharField(max_length = 255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    thumbnail = models.ImageField(upload_to='thumbnails', blank=True, null=True)

    def __str__(self):
        return self.title # 記事タイトルを返す

class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length = 50, blank = True, default = '匿名')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)
    approved_comment = models.BooleanField(default = False)
    def __str__(self):
        return self.text 
