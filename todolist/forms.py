from django import forms

from todolist.models import Category


class CategoryForm(forms.ModelForm):
	name = forms.CharField(max_length=100, help_text="Please enter the category name.")

	class Meta:
		model = Category
		fields = ('name',)
