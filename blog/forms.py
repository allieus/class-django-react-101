from django import forms
from .models import Post, Comment


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


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["author_name", "message"]
