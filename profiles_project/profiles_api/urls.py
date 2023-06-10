from django.urls import path

# new import
from profiles_api import views
from django.urls import include # for including lists in urls in the url pattern and assigning the list to a specific url
from django.urls import path
from rest_framework.routers import DefaultRouter


### register a specific viewset with our router
router = DefaultRouter()
# (name of the url, viewset that we want to register, used for retrieving urls from our router)
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')


### register a UserProfileViewSet as 'profile'

# Note: no need to specify "basename=" bcs we have a queryset object
# so Django REST framework can get a name out of the model that's assigned to it.
# You only need to specify the base name if you are creating a view set 
# that doesn't have a query set or if you want to override the name of the query set that is associated to it.

router.register('profile', views.UserProfileViewSet)


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
