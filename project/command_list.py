from news_portal.models import *

user_1 = User.objects.create_user('User_1')
user_2 = User.objects.create_user('User_2')

author_1 = Author.objects.create(user=user_1)
author_2 = Author.objects.create(user=user_2)

c_1 = Category.objects.create(name='Спорт')
c_2 = Category.objects.create(name='Музыка')
c_3 = Category.objects.create(name='Политика')
c_4 = Category.objects.create(name='Образование')


post_1 = Post.objects.create(text = 'Российский гроссмейстер Ян Непомнящий проиграл чемпиону мира норвежцу Магнусу Карлсену в девятой партии матча за мировую шахматную корону, проходящего в Дубае',
                                post_category = Post.news,
                                title = 'Приплыли',
                                author = Author.objects.get(pk=1))


post_2 = Post.objects.create(text = '''США окончательно объявили о дипломатическом бойкоте Олимпиады-2022. 
Этот символический шаг готовился более года, и вот наконец Белый дом констатировал, что официальная делегация не поедет в Пекин из-за «ситуации с правами человека в Китае».
Что же стало причиной бойкота? По официальным заявлениям – систематическое нарушение прав человека в Китае. 
Речь идёт о репрессиях в отношении китайских уйгуров и других национальных меньшинств на территории КНР, а также о жёстких подавлениях протестов в Гонконге.
США приписывает все эти осудительные действия Китаю, власти Поднебесной же называют такие обвинения ложью. Кто прав? Пусть заинтересованные стороны разбираются сами. и бла бла бла''',
                                post_category = Post.article,
                                title = 'Китай ответил, что их никто и не звал',
                                author = Author.objects.get(pk=1))

post_3 = Post.objects.create(text='''Мировой композитор Сергей Васильевич Рахманинов обладал уникальной особенностью – наибольшим охватом клавиш.
Так, он мог охватить сразу 12 белых клавиш, а левой рукой абсолютно свободно брал аккорд «до-ми/бемоль-соль-до-соль».
Его руки настолько были красивы, что папарацци в своей статье под фото Рахманинова сделали такую подпись: «Руки, которые стоят миллион!».''',
                                post_category = Post.article,
                                title = 'Факты из мира классической музыки',
                                author = Author.objects.get(pk=2))

PostCategory.objects.create(post=Post.objects.all()[0], category=Category.objects.get(pk=1))
PostCategory.objects.create(post=Post.objects.all()[1], category=Category.objects.get(pk=1))
PostCategory.objects.create(post=Post.objects.all()[1], category=Category.objects.get(pk=3))
PostCategory.objects.create(post=Post.objects.all()[2], category=Category.objects.get(pk=2))

com_1 = Comment.objects.create(text='комментарий_1', post=Post.objects.all().first(), user=User.objects.all().first())
com_2 =Comment.objects.create(text='комментарий_2', post=Post.objects.get(pk=2), user=User.objects.get(pk=1))
com_3 = Comment.objects.create(text='комментарий_3', post=Post.objects.get(pk=3), user=User.objects.get(pk=1))
com_4 = Comment.objects.create(text='комментарий_4', post=Post.objects.get(pk=3), user=User.objects.get(pk=2))
com_5 = Comment.objects.create(text='комментарий_5',post=Post.objects.get(pk=1), user=User.objects.get(pk=2))

Post.objects.all().first().like()
Post.objects.all().first().like()
Post.objects.all().first().like()
Post.objects.get(pk=2).dislike()
Post.objects.get(pk=2).dislike()
Post.objects.get(pk=3).like()

Comment.objects.get(pk=1).like()
Comment.objects.get(pk=2).dislike()
Comment.objects.get(pk=2).dislike()
Comment.objects.get(pk=2).dislike()
Comment.objects.get(pk=4).like()
Comment.objects.get(pk=4).like()
Comment.objects.get(pk=5).like()
Comment.objects.get(pk=5).like()
Comment.objects.get(pk=5).like()

rating_author_1 = (sum(i["_rating"] for i in Post.objects.filter(author_id=1).values('_rating')) * 3
                    + sum(i["_rating"] for i in Comment.objects.filter(user_id=1).values('_rating'))
                    + sum(i["_rating"] for i in Comment.objects.filter(post__author=Author.objects.get(pk=1)).values('_rating')))

author_1.update_rating(rating_author_1)


rating_author_2 = (sum(i["_rating"] for i in Post.objects.filter(author_id=2).values('_rating')) * 3
                    + sum(i["_rating"] for i in Comment.objects.filter(user_id=2).values('_rating'))
                    + sum(i["_rating"] for i in Comment.objects.filter(post__author=Author.objects.get(pk=2)).values('_rating')))

author_2.update_rating(rating_author_2)

best_user = Author.objects.all().order_by('-user_rating')[0]

print("Лучший автор:")
print("username:", best_user.user.username)
print("Рейтинг:", best_user.user_rating)

best_article = Post.objects.filter(post_category=Post.article).order_by('-_rating')[0]

print("Лучшая статья:")
print("Дата:", best_article.time_in)
print("Автор:", best_article.author.user.username)
print("Рейтинг:", best_article._rating)
print("Заголовок:", best_article.title)
print("Превью:", best_article.preview())

print("Комментарии к статье:")
for comment in Comment.objects.filter(post=best_article):
    print("Дата:", comment.time_in)
    print("Автор:", comment.user.username)
    print("Рейтинг:", comment._rating)
    print("Комментарий:", comment.text)




