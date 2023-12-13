from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views import View
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse

from .models import Destination
from .forms import DestinationCommentForm


class DestinationListView(LoginRequiredMixin, ListView):
    model = Destination
    template_name = "destination_list.html"

    http_method_names = ["get", "post"]


class CommentGet(DetailView):
    model = Destination
    template_name = "destination_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = DestinationCommentForm()
        return context

    http_method_names = ["get", "post"]


class CommentPost(SingleObjectMixin, FormView):
    model = Destination
    form_class = DestinationCommentForm
    template_name = "destination_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.destination = self.object
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        destination = self.object
        return reverse("destination_detail", kwargs={"pk": destination.pk})

    http_method_names = ["get", "post"]


class DestinationDetailView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)

    http_method_names = ["get", "post"]


class DestinationUpdateView(LoginRequiredMixin, UpdateView):
    model = Destination
    fields = (
        "location",
        "details",
        "country",
        "image",
    )
    template_name = "destination_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    http_method_names = ["get", "post"]


class DestinationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Destination
    template_name = "destination_delete.html"
    success_url = reverse_lazy("destination_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

    http_method_names = ["get", "post"]


class DestinationCreateView(LoginRequiredMixin, CreateView):
    model = Destination
    template_name = "destination_new.html"
    fields = (
        "location",
        "details",
        "country",
        "image",
    )

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    http_method_names = ["get", "post"]
