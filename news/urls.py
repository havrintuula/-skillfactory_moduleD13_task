from django.urls import path
from django.views.decorators.cache import cache_page
# Импортируем созданное нами представление
from .views import NewsList, PostDetail, NewsCreate, ArticleCreate, NewsUpdate, \
   NewsDelete, ArticleUpdate, ArticleDelete, NewsSearchList, \
   CategoryListView, subscribe, unsubscribe
   # subscriptions


urlpatterns = [
   # path — означает путь.
   # В данном случае путь ко всем статьям у нас останется пустым,
   # чуть позже станет ясно почему.
   # Т.к. наше объявленное представление является классом,
   # а Django ожидает функцию, нам надо представить этот класс в виде view.
   # Для этого вызываем метод as_view.
   path('', cache_page(60)(NewsList.as_view()), name='news'),
   path('search', NewsSearchList.as_view(), name='search'),
   # pk — это первичный ключ товара, который будет выводиться у нас в шаблон
   # int — указывает на то, что принимаются только целочисленные значения
   path('<int:pk>', PostDetail.as_view(), name='post_detail'),
   path('news/create', NewsCreate.as_view(), name='news_create'),
   path('article/create', ArticleCreate.as_view(), name='article_create'),
   path('news/<int:pk>/edit/', NewsUpdate.as_view(), name='news_edit'),
   path('news/<int:pk>/delete', NewsDelete.as_view(), name='news_delete'),
   path('article/<int:pk>/edit', ArticleUpdate.as_view(), name='article_edit'),
   path('article/<int:pk>/delete', ArticleDelete.as_view(),name='article_delete'),
   # path('subscriptions/', subscriptions, name='subscriptions'),
   path('categories/<int:pk>/', CategoryListView.as_view(), name='category_list'),
   path('categories/<int:pk>/subscribe', subscribe, name='subscribe'),
   path('categories/<int:pk>/unsubscribe', unsubscribe, name='unsubscribe'),
]