

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django import forms
from django.views import View

from .models import Post
from .forms import NameForm

from django.db.models import Q

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
	model = Post
	template_name = "search.html"

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})


    



