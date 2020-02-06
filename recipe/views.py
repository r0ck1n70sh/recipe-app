from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import ContextMixin
from search_views.search import SearchListView
from search_views.filters import BaseFilter
from .forms import PostSearchForm
from .models import Post, Ingredient
from django.contrib.auth.models import User

class PostFilter(BaseFilter):
    search_fields={
        'search_text':['title','description','steps'],
    }

class PostListView(ListView):
    model=Post
    template_name='recipe/home.html'
    context_object_name='posts'
    paginate_by=6
    ordering=['-date_posted']

class PostDetailView(DetailView):
    model=Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model=Post
    fields =['title', 'description', 'post_pic', 'steps', 'used_ingredients']

    def form_valid(self, form):
        form.instance.author= self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin,UpdateView):
	model=Post
	enctype="multipart/form-data"
	fields =['title', 'description', 'post_pic', 'steps', 'used_ingredients']

	# def get_context_data(self, **kwargs):
	# 	context = super(PostUpdateView, self).get_context_data(**kwargs)
	# 	context['ingredients'] = Ingredient.objects.all()
	# 	return context

	def form_valid(self, form):
		form.instance.author= self.request.user
		return super().form_valid(form)

	def test_func(self):
		post= self.get_object()
		if self.request.user == post.author:
			return True
		return False

class IngreUpdateView(UpdateView):
	model=Ingredient
	template_name='recipe/post_form.html'
	fields =['name']	

class PostDeletelView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model=Post
    success_url='/'

    def test_func(self):
        post= self.get_object()
        if self.request.user == post.author:
            return True
        return False

class UserPostListView(ListView):
    model=Post
    template_name = 'recipe/user_posts.html'
    context_object_name= 'posts'
    paginate_by= 6

    def get_queryset(self):
        user= get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(author=user).order_by('-date_posted')

class PostSearchList(SearchListView):
    model=Post
    paginated_by=6
    context_object_name='posts'
    ordering=['-date_posted']
    form_class=PostSearchForm
    filter_class= PostFilter
    template_name= "recipe/search_post.html"

def about(request):
    return render(request, 'recipe/about.html')