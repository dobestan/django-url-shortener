from django.shortcuts import render
from django.shortcuts import get_object_or_404

from django.views.generic.base import RedirectView
from links.models import Link

class LinkRedirect(RedirectView):
    def get_redirect_url(self, shorten):
        link = get_object_or_404(Link, shorten = shorten)
        return link.original
