from django.urls import path
from .views import ArticleCreateView, ArticleDetailView, ArticleDeleteView, ArticleListView, CommentCreateView, ArticleUpdateView
from django.contrib.auth import views

urlpatterns = [
    path('article/add/', ArticleCreateView.as_view(), name='article-create'),
    path('article/<int:pk>/', ArticleDetailView.as_view(), name='article-detail'),
    path('article/<int:pk>/delete/', ArticleDeleteView.as_view(), name='article-delete'),
    path('article/<int:pk>/update/', ArticleUpdateView.as_view(), name='article-update'),
    path('article/comment/<int:pk>/', CommentCreateView.as_view(), name='article-comment'),
    path('', ArticleListView.as_view(), name="article-list"),
]
