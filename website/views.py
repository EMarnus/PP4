from django.shortcuts import render
from django.views import generic
from .models import Event


class PostList(generic.ListView):
    model = Event
    queryset = Event.objects.order_by()  # Figure out why not working
    template_name = 'index.html'
    paginate_by = 6
