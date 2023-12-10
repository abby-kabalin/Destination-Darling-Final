from django import forms
from .models import DestinationComment


class DestinationCommentForm(forms.ModelForm):
    class Meta:
        model = DestinationComment
        fields = ("comment",)
