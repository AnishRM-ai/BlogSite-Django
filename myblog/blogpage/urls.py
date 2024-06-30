from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="homepage"),
    path('blog/', views.blogpost, name="blogpost"),
    path('blogcreate/', views.createBlog, name="blogcreate"),
]