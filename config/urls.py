from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path

from config.views import dashboard, health_check


urlpatterns = [

    path(
        "",
        dashboard,
        name="dashboard",
    ),

    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="accounts/login.html"
        ),
        name="login",
    ),

    path(
        "logout/",
        auth_views.LogoutView.as_view(),
        name="logout",
    ),

    path(
        "health/",
        health_check,
        name="health-check",
    ),

    path(
        "admin/",
        admin.site.urls,
    ),

]