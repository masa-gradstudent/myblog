from django.urls import path
from .views import home_view, ArticleListView, ArticleDetailView

urlpatterns = [
    # path('', home_view, name='home'),
    path('', ArticleListView.as_view(), name='article_list'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article_detail'),
]