from django.urls import path
from . import views

urlpatterns = [
    path("", views.post_list),
    path("new/", views.post_new),
    path("<int:pk>/", views.post_detail),
    path("<int:pk>/edit/", views.post_edit),
    path("<int:pk>/delete/", views.post_delete),
]
