"""mySecoundProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views


app_name = 'articles'   # для уникальности( для того, что бы индекс и тд, смогли повторятся в проектах),  <a href="{% url 'articles:detail' a.id %}">{{ a.article_title }}</a>
urlpatterns = [
    path('', views.index, name = 'index'),
    path('test/', views.test, name = 'test'),
    path('<int:article_id>/', views.detail, name = 'detail'),    # name для привязки для вывода данных в шаблон
    path('<int:article_id>/leave_comment', views.leave_comment, name = 'leave_comment')   # /article/1/leave_comment
]
