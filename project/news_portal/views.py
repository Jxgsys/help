from django.shortcuts import render
from django.views.generic import ListView, DetailView, DeleteView  # импортируем уже знакомый generic
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.views.generic.edit import CreateView, UpdateView

from .models import Post, Category
from .filters import PostFilter
from .forms import PostForm


class Posts(ListView):
    model = Post
    template_name = 'news_portal/news.html'
    context_object_name = 'news'
    ordering = ['id']
    paginate_by = 1 # поставим постраничный вывод в один элемент
    form_class = PostForm

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)  # создаём новую форму, забиваем в неё данные из POST-запроса

        if form.is_valid():  # если пользователь ввёл всё правильно и нигде не ошибся, то сохраняем новый товар
            form.save()

        return super().get(request, *args, **kwargs)

class PostDetailView(DetailView):
    template_name = 'news_portal/post_detail.html'
    queryset = Post.objects.all()

class PostCreateView(PermissionRequiredMixin, CreateView):
    permission_required = ('news_portal.add_post',)
    template_name = 'news_portal/post_create.html'
    form_class = PostForm


class PostUpdateView(PermissionRequiredMixin, UpdateView):
    permission_required = ('news_portal.change_post',)
    template_name = 'news_portal/post_create.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

class PostDeleteView(DeleteView):
    template_name = 'news_portal/post_delete.html'
    queryset = Post.objects.all()
    success_url = '/news/'


class Search(ListView):
    model = Post
    template_name = 'news_portal/search.html'
    ordering = ['id']
    # paginate_by = 1

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = PostFilter(self.request.GET, queryset=self.get_queryset())
        # context['categories'] = Category.objects.all()
        return context
