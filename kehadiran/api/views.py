from rest_framework.generics import ListAPIView, RetrieveAPIView
from kehadiran.models import Kehadiran
from kehadiran.api.serializers import KehadiranSerializer

class KehadiranRetrieveAPIView(RetrieveAPIView):
    queryset = Kehadiran.objects.all()
    serializer_class = KehadiranSerializer
    lookup_fields = ('id')

class KehadiranListAPIView(ListAPIView):
    queryset = Kehadiran.objects.all()
    serializer_class = KehadiranSerializer
