from django.urls import path
from .api import *


urlpatterns = [
    # After register call (api/token/) to get token
    path('register/', RegisterApi.as_view()),
    path('login/', LoginView.as_view()),
    path('profile/', ProfileViewApi.as_view()),
    path('schoolapi/', SchoolApi.as_view({'get': 'list', 'post': 'create'})),
    path('stopsapi/', StopsApi.as_view({'get': 'list', 'post': 'create'})),


]