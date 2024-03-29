

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django import forms
from django.views import View

from .models import Post
from .forms import NameForm

# from django.db.models import Q

class BlogListView(ListView):
	model = Post
	template_name = "home.html"

class BlogDetailView(DetailView):
	model = Post
	template_name = "post_detail.html"

class BlogCreateView(CreateView):
	model = Post
	template_name = "post_new.html"
	fields = ["title", "author", "body"]

class BlogUpdateView(UpdateView):
	model = Post
	template_name = "post_edit.html"
	fields = ["title", "body"]

class BlogDeleteView(DeleteView):
	model = Post
	template_name = "post_delete.html"
	success_url = reverse_lazy("home")

class SearchView(ListView):
	template_name = "search.html"
	model = Post

# jake code
def get_queryset(self, *args, **kwargs):
		qs = super().get_queryset(*args, **kwargs)
		query = self.request.GET.get('q')
		if query:
			return qs.filter(title=query)
		return qs

# stack overflow code
	# def get_queryset(self):
	# 	name = self.kwargs.get('name', '')
	# 	object_list = self.model.objects.all()
	# 	if name:
	# 		object_list = object_list.filter(body__icontains=name)
	# 	print(object_list)			
	# 	return object_list

	# this throws a name error
	# def get_queryset(self):
	# 	query = self.request.GET.get('q')
	# 	if query:
	# 		object_list = self.model.objects.filter(name__icontains=query)
	# 	else:
	# 		object_list = self.model.objects.none()
	# 	return object_list






