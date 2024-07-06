from .models import Blog, Comments
from django import forms
from django.contrib.auth.models import User
from django_ckeditor_5.widgets import CKEditor5Widget

class BlogCreate(forms.ModelForm):
    contents = forms.CharField(widget=CKEditor5Widget())
    class Meta:
        model = Blog
        fields = ['title', 'author', 'contents', 'tags', 'is_popular', 'cover_image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the title'}),
            'author': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the author'}),
            'tags': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter the tags'}),
            'is_popular': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'cover_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        
        
        
class CommentForm(forms.ModelForm):
    name = forms.CharField(
    max_length=100,
    widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name *'})
    )
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email Address *'})
    )
    text = forms.CharField(
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Leave a Comment', 'style': 'height: 10rem;'})
    )

    class Meta:
        model = Comments
        fields = ['name', 'email', 'text']
        