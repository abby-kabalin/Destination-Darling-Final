from django import forms
from .models import Destination_Comment

class DestCommentForm(forms.ModelForm):
    class Meta:
        model = Destination_Comment
        fields = ("comment",)
            
