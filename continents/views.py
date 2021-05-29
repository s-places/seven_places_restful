"""API view"""
from rest_framework.generics import ListAPIView, RetrieveAPIView
from continents.serializers import ContinentSerializer
from continents.models import Continent


class ContinentView (RetrieveAPIView):
    """return: all objects type: Continent"""
    queryset = Continent.objects.all()
    serializer_class = ContinentSerializer


class ContinentsView (ListAPIView):
    """return: object type: Continent"""
    queryset = Continent.objects.all()
    serializer_class = ContinentSerializer
