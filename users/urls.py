from django.urls import include, path
from . import views
from .views import (SocialLoginView)

urlpatterns = [
    path('', views.UserListView.as_view()),
    path('oauth/login/', SocialLoginView.as_view())
]