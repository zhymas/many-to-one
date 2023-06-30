from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import CreateView, ListView, DetailView
from .models import *
from .forms import *
from django.urls import reverse_lazy


def index(request):
    return render(request, 'music/index.html')


class CreatePerson(CreateView):
    model = Reporter
    form_class = ReporterForm
    template_name = 'music/create.html'
    success_url = reverse_lazy('index')


def reporter(request):
    person = Reporter.objects.all()
    return render(request, 'music/reporter.html', {'person': person})


def detail(request, pk):
    reporters = Reporter.objects.get(pk=pk)
    article = Article.objects.get(pk=pk)
    context = {
        'reporter': reporters,
        'article': article,
    }
    return render(request, 'music/detail.html', context)


class CreateArticle(CreateView):
    model = Article
    form_class = ArticleForm
    template_name = 'music/create_article.html'
    success_url = reverse_lazy('index')



