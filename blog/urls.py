from django.urls import path, include
from . import views_fbv
from . import views_cbv

fbv_urlpatterns = [
    path("", views_fbv.post_list),
    path("new/", views_fbv.post_new),
    path("<int:pk>/", views_fbv.post_detail),
    path("<int:pk>/edit/", views_fbv.post_edit),
    path("<int:pk>/delete/", views_fbv.post_delete),
]

cbv_urlpatterns = [
    path("", views_cbv.post_list),
    path("new/", views_cbv.post_new),
    path("<int:pk>/", views_cbv.post_detail),
    path("<int:pk>/edit/", views_cbv.post_edit),
    path("<int:pk>/delete/", views_cbv.post_delete),
]

urlpatterns = [
    path("", include(fbv_urlpatterns)),
    path("cbv/", include(cbv_urlpatterns)),
]
