from django.contrib import admin
from .models import Post, PostCategory, Comment, Author, Category, CategoryPost


# создаём новый класс для представления товаров в админке
class PostAdmin(admin.ModelAdmin):
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с новостями
    list_display = ('title','author', 'categoryType', 'dateCreation')
    list_filter = ('categoryType', 'author', 'dateCreation')
    search_fields = ('title',)


# Register your models here.

admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(PostCategory)
admin.site.register(Comment)
admin.site.register(Author)
admin.site.register(CategoryPost)
