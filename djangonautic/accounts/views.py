from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) # Push the data to the form instance created with UserCreationForm.
        if form.is_valid():
            user = form.save() # If the form is valid, save it to the database and create new user.
            # After signing up successfully, log the user in automatically.
            login(request, user)
            return redirect('articles:list') # When logged redirect the user to articles list (Check articles/urls.py).

    else:   # If the request if 'GET'
        form = UserCreationForm() # Create form instance and send it to the render method below.

    # Remember, the third parameter is a dictionary of data can be sent down.
    return render(request, 'accounts/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # Log in the user
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:  # If the 'next' parameter occurs in request.POST (sent along the request), means that the user come from specific url.
                return redirect(request.POST.get('next')) # redirect the path which the user comes from in the requests
            else:
                return redirect('articles:list')
    else:
        # Send login form and render it in the browser
        form = AuthenticationForm()
    return  render(request, 'accounts/login.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('articles:list')