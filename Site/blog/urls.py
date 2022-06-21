from django.urls import path
from blog.views import ArticlesListView, ArticlesDetailView, ArticlesCreateView, ArticlesUpdateView, ArticlesDeleteView

app_name='blog'
urlpatterns = [
    path('', ArticlesListView.as_view() , name='article_list'),
    path('<int:pk>/detail/', ArticlesDetailView.as_view(), name='article_detail'),
    path('create/', ArticlesCreateView.as_view(), name='article_create'),
    path('<int:pk>/update/', ArticlesUpdateView.as_view(), name='article_update'),
    path('<int:pk>/delete/', ArticlesDeleteView.as_view(), name='article_delete'),
]
