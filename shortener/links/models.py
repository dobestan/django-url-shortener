from django.db import models

class Link(models.Model):
    original = models.URLField()
    shorten = models.CharField(max_length = 255, unique = True)
