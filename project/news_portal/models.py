from django.db import models
from django.contrib.auth.models import User


class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_rating = models.IntegerField(default=0)

    def update_rating(self, new):
        self.user_rating = new
        self.save()

    def __str__(self):
        return f'{self.user}'


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)
    # subscribers = models.ForeignKey(Author, on_delete=models.CASCADE)



    def __str__(self):
        return f'{self.name}'

class Post(models.Model):
    article = 'a'
    news = 'n'

    CATEGORY = [
        (article, "статья"),
        (news, "новость")

    ]

    post_category = models.CharField(max_length=1, choices=CATEGORY, default=article)
    time_in = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=255)
    text = models.TextField()
    _rating = models.IntegerField(default=0, db_column='rating')
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    category = models.ManyToManyField(Category, through='PostCategory')


    def __str__(self):
        return f'{self.post_category.title()}: {self.title}'

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'/news/{self.id}'

    def like(self):
        self._rating += 1
        self.save()

    def dislike(self):
        self._rating -= 1
        self.save()

    def preview(self):
        a = self.text[:128] + '...'
        return a


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.category.name}'


class Comment(models.Model):
    text = models.TextField()
    time_in = models.DateTimeField(auto_now_add=True)
    _rating = models.IntegerField(default=0, db_column='rating')
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def like(self):
        self._rating += 1
        self.save()

    def dislike(self):
        self._rating -= 1
        self.save()

# Create your models here.
