from rest_framework.serializers import ModelSerializer

from kehadiran.models import Kehadiran

class KehadiranSerializer(ModelSerializer):
    class Meta:
        model = Kehadiran
        fields = [
            'id',
            'jenis_kehadiran',
            'waktu',
        ]
