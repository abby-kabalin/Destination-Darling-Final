from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from .models import Destination


# Create your views here.
class DestinationListView(LoginRequiredMixin, ListView):
    model = Destination
    template_name = "destination_list.html"


class DestinationDetailView(LoginRequiredMixin, DetailView):
    model = Destination
    template_name = "destination_detail.html"


class DestinationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Destination
    fields = (
        "location",
        "details",
        "country",
    )
    template_name = "destination_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class DestinationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Destination
    template_name = "destination_delete.html"
    success_url = reverse_lazy("destination_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class DestinationCreateView(LoginRequiredMixin, CreateView):
    model = Destination
    template_name = "destination_new.html"
    fields = (
        "location",
        "details",
        "country",
    )

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
