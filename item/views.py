from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response

from item.models import Entity
from item.serializers import EntitySerializer


# Create your views here.


class CreateEntityView(CreateAPIView):
    queryset = Entity.objects.all()
    serializer_class = EntitySerializer

    def create(self, request, *args):
        data = request.data
        data['modified_by'] = request.user.id
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
