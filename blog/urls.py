from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views_fbv
from . import views_cbv
from . import views_api_dj
from . import views_api_drf

fbv_urlpatterns = [
    path("", views_fbv.post_list),
    path("new/", views_fbv.post_new),
    path("<int:pk>/", views_fbv.post_detail),
    path("<int:pk>/edit/", views_fbv.post_edit),
    path("<int:pk>/delete/", views_fbv.post_delete),
    path("<int:post_pk>/comments/new/", views_fbv.comment_new),
    path("<int:post_pk>/comments/<int:pk>/edit/", views_fbv.comment_edit),
    path("<int:post_pk>/comments/<int:pk>/delete/", views_fbv.comment_delete),
]

cbv_urlpatterns = [
    path("", views_cbv.post_list),
    path("new/", views_cbv.post_new),
    path("<int:pk>/", views_cbv.post_detail),
    path("<int:pk>/edit/", views_cbv.post_edit),
    path("<int:pk>/delete/", views_cbv.post_delete),
]

django_api_urlpatterns = [
    path("", views_api_dj.post_list),
    path("<int:pk>/", views_api_dj.post_detail),
]

router = DefaultRouter()
router.register("posts", views_api_drf.PostViewSet)
drf_api_urlpatterns = router.urls

urlpatterns = [
    path("", include(fbv_urlpatterns)),
    path("cbv/", include(cbv_urlpatterns)),
    path("api/", include(drf_api_urlpatterns)),
    path("api/dj/", include(django_api_urlpatterns)),
]
