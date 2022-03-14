from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path("", views.NewsViewSet.as_view({"get": "list", "post": "create"}), name="news"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
