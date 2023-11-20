from django import forms
from .models import Attraction, Destination_Comment

class AttractionForm(forms.ModelForm):
    class Meta:
        model = Attraction
        fields = (
            "attraction",
            "description",
            "rating",
            "latitude",
            "longitude",
        )

class DestCommentForm(forms.ModelForm):
    class Meta:
        model = Destination_Comment
        fields = ("comment",)
            
