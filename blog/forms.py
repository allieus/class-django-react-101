from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["author_name", "title", "content"]

    # author_name = forms.CharField()
    # title = forms.CharField()
    # content = forms.CharField(widget=forms.Textarea)


class PostEditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["content"]
