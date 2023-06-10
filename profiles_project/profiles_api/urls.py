from django.urls import path

# new import
from profiles_api import views
from django.urls import include # for including lists in urls in the url pattern and assigning the list to a specific url
from django.urls import path
from rest_framework.routers import DefaultRouter

# register a specific viewset with our router
router = DefaultRouter()
# (name of the url, viewset that we want to register, used for retrieving urls from our router)
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')

urlpatterns = [

    # mapping a url view to api 
    # url: /api/hello-view/
    # as_view(): the standart func called to convert HelloApiView class to be rendered by our urls
    path('hello-view/', views.HelloApiView.as_view()),

    # create a default router
    # url: /api/
    # generates a list of urls that are associated with the viewset
    # that we path to the url patterns
    path('', include(router.urls)),
]
