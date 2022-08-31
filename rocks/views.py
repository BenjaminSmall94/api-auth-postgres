from .models import Rock
from .serializers import RockSerializer
from rest_framework.generics import ListAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from .permissions import IsOwnerOrReadOnly


# Create your views here.
class RockList(ListAPIView):
    queryset = Rock.objects.all()
    serializer_class = RockSerializer


class RockDetail(RetrieveAPIView):
    queryset = Rock.objects.all()
    serializer_class = RockSerializer


class RockUpdateDelete(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Rock.objects.all()
    serializer_class = RockSerializer


class RockCreate(ListCreateAPIView):
    queryset = Rock.objects.all()
    serializer_class = RockSerializer
