from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.urls import reverse

# Additional imports we'll need:
from django.contrib.auth import authenticate, login, logout     # "authenticate" checks if username and password are correct

from .forms import SignUpForm
from django.contrib import messages


# displays info about currently signed in users (if they successfully log in)
def index(request):
    # If no user is signed in, return to login page:
    if not request.user.is_authenticated: # every request has a user associated with it. so if that user object is not signed in 
        return HttpResponseRedirect(reverse("login"))  # user is redirected back to login page
    return render(request, "users/profile.html") # render this template

def login_view(request):
    if request.method == "POST":
        # Accessing username and password from form data
        username = request.POST["username"]
        password = request.POST["password"]

        # Check if username and password are correct, returning User object if so
        user = authenticate(request, username=username, password=password)

        # If user object is returned, log in and route to index page:
        if user: # if user value in not None 
            login(request, user)
            return HttpResponseRedirect(reverse("index")) # back to original route
        # Otherwise, return login page again with new context
        else:
            return render(request, "users/login.html", { # render user login page again
                "message": "Invalid Credentials" # diaplay this statement
            }) 
        
    if request.GET.get('message'):
        # Get the message from the query parameters
        message = request.GET.get('message')
        return render(request, 'users/login.html', {'message': message})
    
    return render(request, "users/login.html")
  


def logout_view(request):
    logout(request) # call the function
    return render(request, "users/login.html", { # take users back to login page
                "message": "Logged Out"  # diaplay this statement
            })

 
def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  
            # load the profile instance created by the signal
            user.save()

            # After successful registration
            message = "Registration was completed successfully. Please log in."



            # Redirect to the login URL with the message as a query parameter
            return redirect(f'login/?message={message}')
        
            # return render(request, 'users/login.html', {'message': message}) # FOR EX RN

            # return redirect('login')  # Redirect to the 'login' URL name or path
            ### 2nd option
            # return HttpResponseRedirect(reverse("login"))  # user is redirected back to login page

            # redirect user to login page with a message
            # return render(request, 'users/login.html', {'message': message})
            

    else:
        form = SignUpForm()
    return render(request, 'users/signup.html', {'form': form})
