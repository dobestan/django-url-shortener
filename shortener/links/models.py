from django.db import models

class Link(models.Model):
    original = models.URLField()
