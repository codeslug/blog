from django.urls import path
from .views import ( 
	BlogListView, 
	BlogDetailView, 
	BlogCreateView, 
	BlogUpdateView, 
	BlogDeleteView,
	PostListView,
	# SearchView,
)

urlpatterns = [

	path('', PostListView.as_view(), name='all'),
	# path("search/", SearchView.as_view(), name="search"),
	# path("contact/", ContactUs.as_view(), name="contact_form"),
	path("post/<int:pk>/delete/", BlogDeleteView.as_view(), name="post_delete"),
	path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name="post_edit"),
	path("post/new/", BlogCreateView.as_view(), name="post_new"),
	path("post/<int:pk>/", BlogDetailView.as_view(), name="post_detail"),
	# path("", BlogListView.as_view(), name="home"),
]