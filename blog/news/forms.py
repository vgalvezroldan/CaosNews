from django.forms import ModelForm
from .models import Post, Tag
from django import forms


class CreatePost(ModelForm):
    
    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(),
    widget=forms.CheckboxSelectMultiple
    )
    
    class Meta:
        model = Post
        fields = ['title','excerpt', 'content', 'image', 'published',
                  'category', 'author', 'tags']
        
    