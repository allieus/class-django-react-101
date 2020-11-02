from django.http import HttpResponse
from django.shortcuts import render
from .models import Post


def post_list(request):
    q = request.GET.get("q", "")  # dict과 유사한 인터페이스

    qs = Post.objects.all()  # QuerySet
    if q:
        qs = qs.filter(title__icontains=q)

    return render(request, "blog/post_list.html", {"post_list": qs,})


def post_new(request):
    pass


def post_detail(request, pk):
    pass


def post_edit(request, pk):
    pass


def post_delete(request, pk):
    pass
