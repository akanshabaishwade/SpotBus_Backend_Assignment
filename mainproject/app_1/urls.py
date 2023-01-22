from django.urls import path
from .api import *


urlpatterns = [
    # After register call (api/token/) to get token
    path('register/', RegisterApi.as_view()),

]