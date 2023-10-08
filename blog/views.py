from django.shortcuts import render
from django.views.generic import ListView

from blog.models import *


# Create your views here.
class BlogIndex(ListView):
    model = Blog
    template_name = 'blog/index.html'

    def get_queryset(self):
        query = super(BlogIndex, self).get_queryset()
        deta = query.all()[:6].order_by('-create_time')
        return deta
