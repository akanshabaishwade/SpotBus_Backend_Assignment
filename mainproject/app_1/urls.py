from django.urls import path
from .api import *


urlpatterns = [
    # After register call (api/token/) to get token
    path('register/', RegisterApi.as_view()),
    path('login/', LoginView.as_view()),
    path('profile/', ProfileView.as_view()),

]