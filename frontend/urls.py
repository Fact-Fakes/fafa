from django.urls import path
from frontend.views import *

app_name = "frontend"

urlpatterns = [path("", IndexView.as_view(), name="index")]

