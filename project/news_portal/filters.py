from django_filters import FilterSet, CharFilter, DateFilter, ModelChoiceFilter,ModelMultipleChoiceFilter
from .models import Post, Author, Category

from .forms import DateInputWidget

class PostFilter(FilterSet):
    title_filter = CharFilter(field_name='title', lookup_expr='icontains', label='По названию')
    author_filter = ModelChoiceFilter(field_name='author', queryset=Author.objects.all(), label='Автор:')
    category_filter = ModelMultipleChoiceFilter(field_name='category', queryset=Category.objects.all(),
                                                label='Категория:')
    datetime_created__gte = DateFilter(field_name='time_in', lookup_expr='gte', label='Дата', widget=DateInputWidget)


    class Meta:
        model = Post
        fields = {
        }
