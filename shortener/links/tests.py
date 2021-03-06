from django.test import TestCase

# Import Exceptions
from django.db import IntegrityError

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

    def test_link_should_have_unique_shorten_url(self):
        link = Link(original = "http://www.example.com", shorten = "test_shorten")
        link.save()

        link_with_same_shorten = Link(original = "http://test.example.com", shorten = "test_shorten")

        self.assertRaises(IntegrityError, link_with_same_shorten.save)

    def test_link_save_with_no_shorten_should_have_random_shorten(self):
        link_save_with_no_shorten = Link(original = "http://test.example.com")
        link_save_with_no_shorten.save()

        self.assertNotEqual("", link_save_with_no_shorten.shorten)

    # should have implemented
    #   - shorten should not be blank ( ValidationError )
    #   - original should not be blank ( ValidationError )
    # having trouble with which module is responsible for this validation.
    # Model or Manager?
