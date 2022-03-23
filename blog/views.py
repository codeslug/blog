

from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse
from django import forms
from django.views import View
from django.contrib.humanize.templatetags.humanize import naturaltime

from .utils import dump_queries
from .models import Post
from .forms import ContactForm, FeedbackForm, SurveyForm

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

# class ContactUs(FormView):
#     form = ContactForm
#     template = 'contact_form.html'

#     def get_success_url(self):
#         return reverse('some-form-success-view')

#     def form_valid(self, form):
#         # Do something with the form data like send an email.
#         return super().form_valid(form)

# class SearchView(request, *args, **kwargs):
	
# 	template_name = "search.html"

	# return HTTPResponse("<h1>Your search results</h1>")

	# if request.method == "GET": # if the form is submitted
	# 	search_query = request.GET.get("search_box", None)	
		# do whatever you need with what the user looked for
	# more code

class PostListView(View):
    template_name = "list.html"
    def get(self, request) :
        strval =  request.GET.get("search", False)
        if strval :
            # Simple title-only search
            # objects = Post.objects.filter(title__contains=strval).select_related().order_by('-updated_at')[:10]
            # Multi-field search
            # __icontains for case-insensitive search
            query = Q(title__icontains=strval) 
            query.add(Q(text__icontains=strval), Q.OR)
            post_list = Post.objects.filter(query).select_related()
        else :
            post_list = Post.objects.all()
        # Augment the post_list
        # for obj in post_list:
        #     obj.natural_updated = naturaltime(obj.updated_at)




