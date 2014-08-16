# REST Framework
from rest_framework import generics

# Custom Model
from links.models import Link

# Custom Serializers
from links.serializers import LinkSerializer

class LinkList(generics.ListCreateAPIView):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer
