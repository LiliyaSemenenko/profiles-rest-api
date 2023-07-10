from django.urls import path

# new import
from users import views
from django.urls import include # for including lists in urls in the url pattern and assigning the list to a specific url
# from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('', views.index, name="index"),
    path("login/", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup_view, name="signup")
]
