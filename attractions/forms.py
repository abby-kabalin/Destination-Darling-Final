from django import forms
from .models import AttractionComment

class AttractionCommentForm(forms.ModelForm):
    class Meta:
        model= AttractionComment
        fields = ("comment",)
