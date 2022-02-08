from django.urls import path, re_path
from django.conf.urls import include

from Register.views import UserAPI


urlpatterns = [
    re_path(r'^create_user/$', UserAPI.as_view()),
]