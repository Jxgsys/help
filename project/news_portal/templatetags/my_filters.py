from django import template

register = template.Library()


@register.filter(name='relax')
def relax(value):
    list_of = ['окончательно', 'корону', 'клавиш']
    for i in list_of:
        while True:
            if i in value:
                value = value.replace(i, '*' * len(i))
            else:
                break
    return value
