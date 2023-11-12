from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + (
            "email",
            "country",
        )


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = (  # I had to get rid of UserChangeForm.Meta.fields because it was causing an error
            # and crashing my server
            "email",
            "country",
        )
