# posts/views.py
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from . import models


class PostListView(LoginRequiredMixin, ListView): # new
    model = models.Post
    template_name = 'post_list.html'
    login_url = 'login' # new


class PostCreateView(LoginRequiredMixin, CreateView): # new
    model = models.Post
    template_name = 'post_new.html'
    fields = ['message']
    login_url = 'login' # new

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostDetailView(LoginRequiredMixin, DetailView): # new
    model = models.Post
    template_name = 'post_detail.html'
    login_url = 'login' # new


class PostUpdateView(LoginRequiredMixin, UpdateView): # new
    model = models.Post
    fields = ['message']
    template_name = 'post_edit.html'
    login_url = 'login' # new


class PostDeleteView(LoginRequiredMixin, DeleteView): # new
    model = models.Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('posts')
    login_url = 'login' # new

