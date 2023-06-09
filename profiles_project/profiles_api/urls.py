from django.urls import path

# new import
from profiles_api import views

urlpatterns = [

    # mapping a url view to api 
    # url: /api/hello-view/
    # as_view(): the standart func called to convert HelloApiView class to be rendered by our urls
    path('hello-view/', views.HelloApiView.as_view()),
]