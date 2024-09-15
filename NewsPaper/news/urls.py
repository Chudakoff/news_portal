from django.urls import path
from .views import NewsList, NewsDetail, NewsSearch, ArticleUpdate, PostDelete, NewsCreate #create_post,



urlpatterns = [
   path('', NewsList.as_view(), name='posts_list'),
   path('<int:pk>', NewsDetail.as_view(), name='post_detail'),
   # path('create/', create_post, name='post_create'),
   path('search/', NewsSearch.as_view()),
   path('create/', NewsCreate.as_view(), name='news_create'),
   path('<int:pk>/update/', ArticleUpdate.as_view(), name='news_update'),
   path('<int:pk>/delete/', PostDelete.as_view(), name='news_delete'),
]