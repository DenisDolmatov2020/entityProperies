from rest_framework.generics import ListCreateAPIView

from item.models import Entity
from item.serializers import EntitySerializer


# Create your views here.


class CreateListEntityView(ListCreateAPIView):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer
