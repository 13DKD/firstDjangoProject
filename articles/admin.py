from django.contrib import admin
from . models import Article, Comment

admin.site.register(Article)    # для вывода в myAdmin новостей
admin.site.register(Comment)
