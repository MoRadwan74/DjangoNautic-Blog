from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST) # Push the data to the form instance created with UserCreationForm.
        if form.is_valid():
            form.save() # If the form is valid, save it to the database and create new user.
            # Log the user in
            return redirect('articles:list') # When logged redirect the user to articles list.

    else:   # If the request if 'GET'
        form = UserCreationForm() # Create form instance and send it to the render method below.

    return render(request, 'accounts/signup.html', {'form': form})