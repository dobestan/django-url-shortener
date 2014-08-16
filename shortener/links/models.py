from django.db import models

# Import Exceptions
from django.core.exceptions import ValidationError

class Link(models.Model):
    def init_shorten():
        import random
        import string

        while True:
            shorten = ""
            for i in range(6):
                shorten += random.choice(string.digits + string.letters)
            try:
                Link.objects.get(shorten = shorten)
            except:
                return shorten

    original = models.URLField()
    shorten = models.CharField(
                max_length = 255,
                unique = True,
                blank = True,
                default = init_shorten
            )
