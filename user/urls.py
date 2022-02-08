from django.urls import path
from .views import UserProfileView, ChangePasswordView, register, edit_profile
from django.contrib.auth import views

urlpatterns = [
    path("<int:pk>/", UserProfileView.as_view(), name="user-profile"),
    path("edit/", edit_profile, name="user-edit"),
    path("login/",views.LoginView.as_view(template_name="login.html", next_page=None), name="login",),
    path("logout/",views.LogoutView.as_view(template_name="article_list.html", next_page=None), name="logout",),
    path("password/", ChangePasswordView.as_view(), name="password_reset"),
    path("register/", register, name="register"),
]
