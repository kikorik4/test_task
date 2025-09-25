from django.contrib.auth.urls import urlpatterns
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import SecretInfoAPIList, SecretInfoAPIUpdate, SecretInfoAPIDelete

app_name = "auth"

urlpatterns = [
    path("info/", SecretInfoAPIList.as_view()),
    path("info/<int:pk>", SecretInfoAPIUpdate.as_view()),
    path("info/<int:pk>/delete", SecretInfoAPIDelete.as_view())
]