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
    path('<slug:slug>/', views.article_detail, name="detail"),
]


