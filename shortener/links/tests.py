from django.test import TestCase

from links.models import Link

class LinkModelTest(TestCase):
    def test_link_should_have_original_url(self):
        try:
            link = Link()
            link.original
        except AttributeError:
            self.fail("Link should have original field")

    def test_link_should_have_shorten_url(self):
        try:
            link = Link()
            link.shorten
        except AttributeError:
            self.fail("Link should have shorten field")


