from .models import Blog
from django import forms
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field

class BlogCreate(forms.ModelForm):
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