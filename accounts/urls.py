from django.urls import path
from .views import SignUpView, UserProfileView

urlpatterns = [
    path("signup/", SignUpView.as_view(), name="signup"),
    path("user-profile/", UserProfileView.as_view(), name="user_profile"),
]

from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns += staticfiles_urlpatterns()
