from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.socialaccount.models import SocialAccount
from django.http.request import HttpRequest
from django.urls import reverse


class CustomAdapter(DefaultSocialAccountAdapter):
    def get_connect_redirect_url(
        self, request: HttpRequest, socialaccount: SocialAccount
    ):
        assert request.user.is_authenticated
        url = reverse("profile_index")
        return url
