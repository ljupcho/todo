# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.template import RequestContext
from django.views import View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from todolist.models import Category, Task
from todolist.tasks import adding_task


class HomePageView(View):
	def get(self, request):
		context = RequestContext(request)

		return render_to_response('todolist/index.html', {}, context)


class CategoryList(ListView):
	queryset = Category.objects.order_by('-name')


class CategoryDetailView(DetailView):
	model = Category
	template_name = 'todolist/category_detail.html'
	context_object_name = 'category'


class CategoryCreate(CreateView):
	model = Category
	fields = ('name',)
	template_name = 'todolist/category_create.html'


class CategoryUpdate(UpdateView):
	model = Category
	fields = ('name',)
	template_name = 'todolist/category_update.html'
	context_object_name = 'category'


class CategoryDelete(DeleteView):
	model = Category


class TaskCreate(CreateView):
	model = Task
	fields = ('description', 'category', 'start_date',)
	template_name = 'todolist/task_create.html'

	def post(self, request, *args, **kwargs):
		task = adding_task.depay(1, 1)
		return super(TaskCreate, self).post(self, request, *args, **kwargs)


class TaskUpdate(UpdateView):
	model = Task
	fields = ('description', 'category', 'start_date',)
	template_name = 'todolist/task_update.html'
	context_object_name = 'task'
