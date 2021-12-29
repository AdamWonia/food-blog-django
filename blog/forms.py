from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    name = forms.CharField(help_text="Max 50 characters")
    title = forms.CharField(help_text='Max 100 characters')

    class Meta:
        model = Post
        fields = ['name', 'title', 'text', 'created_date', 'published_date', 'image']
