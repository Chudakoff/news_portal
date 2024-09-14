from django.urls import path
from .views import NewsList, NewsDetail, NewsSearch, ArticleCreate, ArticleUpdate, PostDelete, NewsCreate #create_post,



urlpatterns = [
   path('', NewsList.as_view(), name='posts_list'),
   path('<int:pk>', NewsDetail.as_view(), name='post_detail'),
   # path('create/', create_post, name='post_create'),
   path('search/', NewsSearch.as_view()),
   path('articles/create/', ArticleCreate.as_view(), name='articles_create'),
   path('articles/<int:pk>/update/', ArticleUpdate.as_view(), name='articles_update'),
   path('articles/<int:pk>/delete/', PostDelete.as_view(), name='articles_delete'),
   path('news/create/', NewsCreate.as_view(), name='news_create'),
   path('news/<int:pk>/update/', ArticleUpdate.as_view(), name='news_update'),
   path('news/<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),
]