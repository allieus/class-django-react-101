from django.http import request
from blog.views_fbv import post_list
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post
from .forms import PostForm, PostEditForm


class PostListView(ListView):
    model = Post

    def get_queryset(self):
        self.q = self.request.GET.get("q", "")

        qs = super().get_queryset()
        if self.q:
            qs = qs.filter(title__icontains=self.q)
        return qs


post_list = PostListView.as_view()


post_new = CreateView.as_view(model=Post, form_class=PostForm, success_url="/blog/")

post_detail = DetailView.as_view(model=Post)

post_edit = UpdateView.as_view(
    model=Post, form_class=PostEditForm, success_url="/blog/"
)

post_delete = DeleteView.as_view(model=Post, success_url="/blog/")
