from django.shortcuts import get_object_or_404 ,render, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.contrib.auth.decorators import login_required

from django.db.models.query import QuerySet
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Comment, Category
from .filters import PostsFilter
from .forms import PostForm

# Create your views here.
class NewsList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'newslist.html'
    context_object_name = 'posts_list'
    paginate_by = 6

class NewsSearch(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'search.html'
    context_object_name = 'posts_search'
    # paginate_by = 5

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = PostsFilter(self.request.GET, queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context

class NewsDetail(DetailView):
    model = Post
    template_name = 'news.html'
    context_object_name = 'post'


class ArticleCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'article_edit.html'

class ArticleUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = ('news.change_post',)
    form_class = PostForm
    model = Post
    template_name = 'article_edit.html'

class PostDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('news.delete_post',)
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts_list')

class NewsCreate(PermissionRequiredMixin, CreateView):
    permission_required = ('news.add_post',)
    form_class = PostForm
    model = Post
    template_name = 'article_edit.html'

    def form_valid(self, form):
        post = form.save(commit=False)
        post.categoryType = 'NW'
        return super().form_valid(form)

class CommentsList(ListView):
    model = Comment
    ordering = '-dateCreation'
    template_name = 'commentslist.html'
    context_object_name = 'comments_list'
    paginate_by = 10


class CategoryListView(ListView):
    model = Post
    template_name = 'news/category_list.html'
    context_object_name = 'category_news_list'

    def get_queryset(self):
        self.postCategory = get_object_or_404(Category, id=self.kwargs['pk'])
        queryset = Post.objects.filter(postCategory=self.postCategory).order_by('-dateCreation')

        return queryset

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['is_not_subscriber'] = self.request.user not in self.postCategory.subscribers.all()
        context['postCategory'] = self.postCategory

        return context

@login_required
def subscribe(request, pk):
    user = request.user
    category = Category.objects.get(id=pk)
    category.subscribers.add(user)
    message = 'Вы успешно подписались на рассылку новосте по категории'

    return render(request, 'news/subscribe.html', {'category': category, 'message': message})