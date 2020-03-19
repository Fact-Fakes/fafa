from django.urls import path

from backend.views import *

app_name = "backend"

urlpatterns = [path("get_cookie", CookieView.as_view(), name="get_cookie")]

