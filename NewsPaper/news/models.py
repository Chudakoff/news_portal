from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Author(models.Model):
    author_user = models.OneToOneField(User, on_delete=models.CASCADE)
    author_rating = models.IntegerField(default=0)

    def update_rating(self):
        pass


class Category(models.Model):
    name = models.CharField(max_length=64, unique = True)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    ARTICLE = 'AR'
    NEWS = 'NW'
    CATEGORY_CHOICES = (
        (NEWS, 'Новость'),
        (ARTICLE, 'Статья'),
    )
    def preview(self):
        return None

    def like(self):
        pass

    def dislike(self):
        pass


class PostCategory(models.Model):
    pass


class Comment(models.Model):
    def like(self):
        pass
    def dislike(self):
        pass