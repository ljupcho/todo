# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone


class Category(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class Task(models.Model):
	description = models.TextField(blank=False)
	start_date = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))
	category = models.ForeignKey(Category, default="general")
	created_at = models.DateField(default=timezone.now().strftime("%Y-%m-%d"))

	def __str__(self):
		return self.description

