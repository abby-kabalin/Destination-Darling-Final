from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy, reverse
from .models import Destination
from .forms import AttractionForm, DestCommentForm


class AttractionGet(DetailView):
    model = Destination
    template_name = "destination_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = AttractionForm()
        return context

class AttractionPost(SingleObjectMixin, FormView):
    model = Destination
    form_class = AttractionForm
    template_name = "destination_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        attraction = form.save(commit=False)
        attraction.location = self.object
        attraction.author = self.request.user
        attraction.save()
        return super().form_valid(form)

    def get_success_url(self):
        destination = self.object
        return reverse("destination_detail", kwargs={"pk": destination.pk})
    

class DestinationDetailView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        view = AttractionGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = AttractionPost.as_view()
        return view(request, *args, **kwargs)


# Create your views here.
class DestCommentGet(LoginRequiredMixin, ListView):
    model = Destination
    template_name = "destination_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = DestCommentForm()
        return context

class DestCommentPost(SingleObjectMixin, FormView):
    pass


class DestinationListView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        view = DestCommentGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = DestCommentPost.as_view()
        return view(request, *args, **kwargs)


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
