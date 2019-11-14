# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.views import View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from todolist.decorators import dispatch_task
from todolist.models import Category, Task, FailedTask
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

		response = super(TaskCreate, self).post(self, request, *args, **kwargs)

		def run_task():
			task = adding_task.delay(1)

		dispatch_task(run_task())

		return response


class TaskUpdate(UpdateView):
	model = Task
	fields = ('description', 'category', 'start_date',)
	template_name = 'todolist/task_update.html'
	context_object_name = 'task'

	def post(self, request, *args, **kwargs):

		response = super(TaskUpdate, self).post(self, request, *args, **kwargs)

		def run_task():
			task = adding_task.delay(1)

		dispatch_task(run_task())

		return response


class FailedTasks(View):
	def get(self, request):
		tasks = FailedTask.objects.all()

		def run_task(id):
			task = adding_task.delay(id)

		for task in tasks:
			dispatch_task(run_task(task.category_id), task.category_id)

		return HttpResponse('OK')







