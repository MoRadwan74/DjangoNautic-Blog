from django.shortcuts import render, redirect
from .models import Article
from django.contrib.auth.decorators import login_required
from . import forms

# Create your views here.

def article_list(request):
    # We want to output the the articles titles inside html page, so we order them by date then pass them to the render method to be passed to the template.
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_list.html', {'articles': articles})

def article_detail(request, slug):
    # We should query the database to find an article with the given slug, so that we can show its data.
    # return HttpResponse(slug)
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article})

@login_required(login_url="/accounts/login")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES) # Uploaded files doesn't come with the post request.
        if form.is_valid():
            # Save article to database
            article_instance = form.save(commit=False)
            article_instance.author = request.user # Store the current logged user in the author field inside Article model.
            # commit = False, means hang on a minute. The form will be saved but don't commit just yet as We want to get this instance, then do something with it then save it.
            article_instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form': form})

