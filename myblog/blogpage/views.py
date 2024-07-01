from django.shortcuts import render, redirect,get_object_or_404
from .models import Blog
from .forms import BlogCreate
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
# Create your views here.
def home(request):
    blog = Blog.objects.all()
    return render(request, 'index.html',{'blog': blog})

def blogpost(request, title):
    blog = Blog.objects.all()
    return render(request, 'blogpost.html', {'blog': blog})


def createBlog(request):
    if request.method == 'POST':
        form = BlogCreate(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Your Post Has been Posted.")
            return redirect('homepage') 
        else:
            messages.error(request, f"Sorry, there was a problem publishing your post. Errors: {form.errors}")
    else:
        form = BlogCreate()
    
    return render(request, 'create_blog.html', {'form': form})
    
#login view code.   
def login_view(request):
    
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                messages.success(request, f"You are now logged in as {username}.")
                return redirect("homepage")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()
        return render(request, "login.html", {"form": form})
            
            
    return render(request, 'login.html')    

def logout_view(request):
        logout(request)
        messages.success(request,"You have been logged out.")
        redirect ('homepage')
    

def singleBlog(request, title):
    popularBlog = Blog.objects.filter(is_popular = True)
    blog = get_object_or_404(Blog, title=title)
    return render(request, 'single_post.html', {'blog': blog, 'popularblog': popularBlog})
    

