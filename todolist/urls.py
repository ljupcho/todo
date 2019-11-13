from django.conf.urls import url

from todolist.views import HomePageView, CategoryList, CategoryCreate, CategoryDetailView, CategoryDelete, \
    CategoryUpdate, TaskCreate
from . import views

urlpatterns = [
    url(r'^$', HomePageView.as_view()),
    url(r'^categories/$', CategoryList.as_view(), name='categories'),
    url(r'^categories/create/$', CategoryCreate.as_view(), name='category-create'),
    url(r'^categories/(?P<pk>[-\w]+)/$', CategoryDetailView.as_view(), name='category-detail'),
    url(r'^categories/(?P<pk>[-\w]+)/update/$', CategoryUpdate.as_view(), name='category-update'),
    url(r'^categories/(?P<pk>[-\w]+)/delete/$', CategoryDelete.as_view(), name='category-delete'),
    url(r'^tasks/create/$', TaskCreate.as_view(), name='task-create'),

]