from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
class NewsList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'newslist.html'
    context_object_name = 'post'

class NewsDetail(DetailView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'post'
