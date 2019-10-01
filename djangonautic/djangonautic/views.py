# from django.http import HttpResponse
# This allows us to send response to the user when they request.

from django.shortcuts import render

# Sofar, we need two functions. One for about and the second for home.

def homepage(request):
    # return HttpResponse('homepage')
    return render(request, 'homepage.html')

def about(request):
    # return HttpResponse('about')
    return render(request, 'about.html')