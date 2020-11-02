import json
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from .models import Post


def post_list(request):
    qs = Post.objects.all()
    post_list_obj = [
        {'id': post.id, 'title': post.title, 'content': post.content,
         'created_at': post.created_at, 'updated_at': post.updated_at }
        for post in qs
    ]
    return JsonResponse(post_list_obj, safe=False,
                        json_dumps_params={"ensure_ascii": False})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post_obj = {
        'id': post.id,
        'title': post.title,
        'content': post.content,
        'created_at': post.created_at,
        'updated_at': post.updated_at,
    }
    return JsonResponse(post_obj, json_dumps_params={"ensure_ascii": False})
