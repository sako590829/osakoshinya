from django.shortcuts import render
from django.views.generic import TemplateView,ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from .models import Blog
from django.urls import reverse_lazy


class Main(TemplateView):
    template_name="top.html"

class BlogListView(ListView):
    model = Blog
    template_name="sako/blog_list.html"
    paginate_by = 3

class BlogCreateView(CreateView):
    model = Blog
    fields = '__all__'

class BlogUpdateView(UpdateView):
    model = Blog
    fields = '__all__'
    template_name_suffix = '_update_form'

class BlogDeleteView(DeleteView):
    model = Blog
    success_url = reverse_lazy('list')
    