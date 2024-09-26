from django.urls import path
from .views import NewsList, NewsDetail, NewsSearch, ArticleUpdate, PostDelete, NewsCreate, CategoryListView, subscribe

urlpatterns = [
   path('', NewsList.as_view(), name='posts_list'),
   path('<int:pk>', NewsDetail.as_view(), name='post_detail'),
   # path('create/', create_post, name='post_create'),
   path('search/', NewsSearch.as_view()),
   path('add/', NewsCreate.as_view(), name='news_create'),
   path('<int:pk>/edit', ArticleUpdate.as_view(), name='news_update'),
   path('<int:pk>/delete', PostDelete.as_view(), name='news_delete'),
   # path('<int:pk>/comments', CommentsList.as_view(), name='comments_list'),
   path('categories/<int:pk>/', CategoryListView.as_view(), name='category_list'),
   path('categories/<int:pk>/subscribe', subscribe, name='subscribe')
]