"""""
We made this "article" app with the command,
>> python manage.py startapp AppName 
"""""

from django.urls import path
from . import views

# Assigning a name for this particular URL file in case there're other files that have "list" and "detail" paths.
app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name="list"),   # This is for the Home page.
    path('create/', views.article_create, name="create"),
    path('<slug:slug>/', views.article_detail, name="detail"),
    # We make create article above article detail because if we make it below, django may think that the word 'create' is a pre-made slug and it will try to fetch it.
]


