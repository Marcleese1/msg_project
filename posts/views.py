# posts/views.py
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.http import Http404


from . import models


class PostListView(LoginRequiredMixin, ListView): # new
    model = models.Post

    template_name = 'post_list.html'
    login_url = 'login'


class PostCreateView(LoginRequiredMixin, CreateView):
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
    #if user or superuser
    model = models.Post
    fields = ['message']
    template_name = 'post_edit.html'
    login_url = 'login'

#else call this
#FUNCTION TO ALLOW ONLY THE PERSON POSTING TO EDIT THEIR POSTS.
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise Http404("You are not allowed to edit this Post")#sllows you to show a 404 page when someone who didnt write the post tried to edit it
        return super(PostUpdateView, self).dispatch(request, *args, **kwargs)


class PostDeleteView(LoginRequiredMixin, DeleteView): # new
        model = models.Post
        template_name = 'post_delete.html'
        success_url = reverse_lazy('posts')
        login_url = 'login' # new

