from django.forms import ModelForm, BooleanField, DateInput
from .models import Post


# Создаём модельную форму

class DateInputWidget(DateInput):
    input_type = 'date'


class PostForm(ModelForm):
    check_box = BooleanField(label='( ╯°□°)╯')  # добавляем галочку, или же true-false поле

    class Meta:
        model = Post
        fields = ['category', 'post_category', 'author', 'title', 'text']
