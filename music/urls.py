from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('reporter/', reporter, name='reporter'),
    path('reporter/<int:pk>', detail, name='detail'),
    path('create/', CreatePerson.as_view(), name='create'),
    path('create/article/', CreateArticle.as_view(), name='create_article'),
]
