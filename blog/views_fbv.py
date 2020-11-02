from django.http import HttpResponse, Http404
from django.shortcuts import get_object_or_404, redirect, render
from .models import Post
from .forms import PostForm, PostEditForm


def post_list(request):
    q = request.GET.get("q", "")  # dict과 유사한 인터페이스

    qs = Post.objects.all()  # QuerySet
    if q:
        qs = qs.filter(title__icontains=q)

    return render(request, "blog/post_list.html", {"post_list": qs,})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("/blog/")  # TODO: URL Reverse
    else:  # GET 요청
        form = PostForm()

    return render(request, "blog/post_form.html", {"form": form})


def post_detail(request, pk):
    # id => Primary Key
    # pk => Primary Key에 대한 alias
    # try:
    #     post = Post.objects.get(
    #         pk=pk
    #     )  # Post.DoesNotExist, Post.MultipleObjectsReturned
    # except Post.DoesNotExist:
    #     raise Http404

    post = get_object_or_404(Post, pk=pk)
    return render(request, "blog/post_detail.html", {"post": post})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = PostEditForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect("/blog/")  # TODO: URL Reverse
    else:  # GET 요청
        form = PostEditForm(instance=post)

    return render(request, "blog/post_form.html", {"form": form, "post": post})


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        # post.title = "삭제된 포스팅"
        # post.content = ""
        # post.save()
        post.delete()
        return redirect("/blog/")  # TODO: URL Reverse
    else:
        pass
    return render(request, "blog/post_confirm_delete.html", {"post": post})
