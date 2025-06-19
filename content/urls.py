from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="login"), name="logout"),

    # Provide /accounts/ routes for compatibility with Django defaults
    path("accounts/login/", auth_views.LoginView.as_view(template_name="registration/login.html")),
    path("accounts/logout/", auth_views.LogoutView.as_view(next_page="login")),
    path("accounts/register/", views.register),

    path("", views.content_list, name="content_list"),
    path("create/", views.content_create, name="content_create"),
    path("<int:pk>/", views.content_detail, name="content_detail"),
    path("<int:pk>/edit/", views.content_edit, name="content_edit"),
]
