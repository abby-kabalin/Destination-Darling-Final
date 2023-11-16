from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import (
    UpdateView, DeleteView, CreateView
)
from django.urls import reverse_lazy
from .models import Destination

# Create your views here.
class DestinationListView(ListView):
    model = Destination
    template_name = "destination_list.html"

class DestinationDetailView(DetailView):
    model = Destination
    template_name = "destination_detail.html"

class DestinationUpdateView(UpdateView):
    model = Destination
    fields = (
        "location",
        "details",
        "country",
    )
    template_name = "destination_edit.html"

class DestinationDeleteView(DeleteView):
    model = Destination
    template_name = "destination_delete.html"
    success_url = reverse_lazy("destination_list")

class DestinationCreateView(CreateView):
    model = Destination
    template_name = "destination_new.html"
    fields = (
        "location",
        "details",
        "country",
        "author",
    )
        
