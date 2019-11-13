# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.views import View


class HomePageView(View):
    def get(self, request):
        context = RequestContext(request)

        return render_to_response('todolist/index.html', {}, context)


# class CategoryView(View):
# 	def get(self, request):
# 		context = RequestContext(request)
#         return render_to_response('todolist/index.html', {}, context)



