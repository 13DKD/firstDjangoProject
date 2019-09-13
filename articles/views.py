# from django.http import HttpResponse
#
# def index(request):
#     return HttpResponse('Hello World!')
#
# def test(request):
#     return HttpResponse('Еще один тест роутов') # вложеный юрл в артиклес
from django.shortcuts import render # для передачи данных в браузер
from django.http import Http404, HttpResponseRedirect
from .models import Article, Comment
from django.urls import reverse # для получения ссылки


def index(request):
    latest_articles_list = Article.objects.order_by('-pub_date')[:5]    # - (в обратную сторону), [:5] - последние 5 статьей.
    return render(request, 'articles/list.html', {'latest_articles_list': latest_articles_list})


def test(request):
    return render(request, 'base.html')


def detail(request, article_id):
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404('Статья не найдена!')
    latest_comments_list = a.comment_set.order_by('-id')[:10]
    return render(request, 'articles/detail.html', {'article': a,
                                                    'latest_comments_list': latest_comments_list})


def leave_comment(request, article_id):
    try:
        a = Article.objects.get(id = article_id)
    except:
        raise Http404('Статья не найдена!')
    a.comment_set.create(author_name = request.POST['name'], comment_text = request.POST['text'])
    return HttpResponseRedirect(reverse('articles:detail', args = (a.id,)))