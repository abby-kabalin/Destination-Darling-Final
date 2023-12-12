from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.views import View
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse
from .models import Attraction
from .forms import AttractionCommentForm


class AttractionListView(LoginRequiredMixin, ListView):
    model = Attraction
    template_name = "attraction_list.html"


class CommentGet(DetailView):
    model = Attraction
    template_name = "attraction_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = AttractionCommentForm()
        return context


class CommentPost(SingleObjectMixin, FormView):
    model = Attraction
    form_class = AttractionCommentForm
    template_name = "attraction_detail.html"

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        comment = form.save(commit=False)
        comment.attraction = self.object
        comment.author = self.request.user
        comment.save()
        return super().form_valid(form)

    def get_success_url(self):
        attraction = self.object
        return reverse("attraction_detail", kwargs={"pk": attraction.pk})


class AttractionDetailView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)


class AttractionUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Attraction
    fields = (
        "name",
        "image",
        "description",
        "address",
        "rating",
        "tags",
    )
    template_name = "attraction_edit.html"

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class AttractionDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Attraction
    template_name = "attraction_delete.html"
    success_url = reverse_lazy("attraction_list")

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user


class AttractionCreateView(LoginRequiredMixin, CreateView):
    model = Attraction
    template_name = "attraction_new.html"
    fields = (
        "name",
        "image",
        "description",
        "location",
        "address",
        "rating",
        "tags",
    )

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
