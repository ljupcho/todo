from django.conf.urls import url

from todolist.views import HomePageView
from . import views

urlpatterns = [
    url(r'^$', HomePageView.as_view()),
]