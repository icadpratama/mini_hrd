from rest_framework.generics import ListAPIView, RetrieveAPIView
from karyawan.models import Karyawan
from karyawan.api.serializers import KaryawanSerializer, DaftarKaryawanSerializer

class KaryawanListAPIView(ListAPIView):
    queryset = Karyawan.objects.all()
    serializer_class = KaryawanSerializer

class KaryawanDetailAPIView(RetrieveAPIView):
    queryset = Karyawan.objects.all()
    serializer_class = DaftarKaryawanSerializer
    lookup_fields = ('id')
