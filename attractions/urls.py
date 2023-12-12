from django.urls import path

from .views import (
    AttractionListView,
    AttractionDetailView,
    AttractionUpdateView,
    AttractionDeleteView,
    AttractionCreateView,
)

urlpatterns = [
    path("new/", AttractionCreateView.as_view(), name="attraction_new"),
    path("<str:pk>/", AttractionDetailView.as_view(), name="attraction_detail"),
    path("<str:pk>/edit/", AttractionUpdateView.as_view(), name="attraction_edit"),
    path("<str:pk>/delete/", AttractionDeleteView.as_view(), name="attraction_delete"),
    path("", AttractionListView.as_view(), name="attraction_list"),
]
