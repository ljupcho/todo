# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.core.urlresolvers import reverse
from django.db import models
from django.utils import timezone


class Category(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('category-detail', kwargs={'pk': self.pk})


class Task(models.Model):
	description = models.TextField(blank=False)
	start_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	created_at = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))

	def __str__(self):
		return self.description

