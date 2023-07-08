from django.shortcuts import render
from django.views import generic
from .models import Event


class PostList(generic.ListView):
    model = Event
    queryset = Post.object.order_by(event_date)
    template_name = 'index.html'
    paginate_by = 6
