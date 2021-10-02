from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView, DeleteView

from common.forms.mixin import JsonFormMixin
from common.views.mixin import DeletionMixin
from zone.forms import PostForm
from zone.models import Post


class PostList(ListView):
    template_name = 'zone/blocks/post_list.html'
    model = Post
    paginate_by = 5
    ordering = 'id'


class PostIndex(TemplateView):
    template_name = 'zone/index.html'

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data.update(form=PostForm())
        return context_data


class PostCreate(JsonFormMixin, CreateView):
    model = Post
    form_class = PostForm
    http_method_names = ['post']

    def get_form(self, form_class=None):
        form = super().get_form(form_class=form_class)
        form.instance.user = self.request.user
        return form


class PostDelete(DeletionMixin, DeleteView):
    model = Post
    json = True
