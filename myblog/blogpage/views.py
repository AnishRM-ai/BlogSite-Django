from django.shortcuts import render, redirect
from .models import Blog
from .forms import BlogCreate
# Create your views here.
def home(request):
    blog = Blog.objects.all()
    return render(request, 'index.html',{'blog': blog})

def blogpost(request, title):
    blog = Blog.objects.all()
    return render(request, 'blogpost.html', {'blog': blog})


def createBlog(request):
   
    if request.method == 'POST':
        form = BlogCreate(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home') 
        
    else:
        form = BlogCreate()
        return render(request, 'create_blog.html', {'form': form})
    
    
def login_view(request):
    return render(request, 'login.html')

def logout_view(request):
    return render(request, 'logout.html')

def register(request):
    return render(request, 'register.html')

