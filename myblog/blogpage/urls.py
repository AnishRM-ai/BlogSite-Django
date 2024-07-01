from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="homepage"),
    path('blog/', views.blogpost, name="blogpost"),
    path('blogcreate/', views.createBlog, name="blogcreate"),
    path('login/', views.login_view, name="login_form"),
    path('article/<str:title>', views.singleBlog, name="article"),
    path('logout/', views.logout_view, name="logout"),
]