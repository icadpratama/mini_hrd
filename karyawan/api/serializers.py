from rest_framework.serializers import ModelSerializer

from karyawan.models import Karyawan

class KaryawanSerializer(ModelSerializer):
    class Meta:
        model = Karyawan
        fields = [
            'id',
            'nama',
            'alamat',
            'jenis_kelamin'
        ]

class DaftarKaryawanSerializer(ModelSerializer):
    class Meta:
        model = Karyawan
        fields = [
            'nama',
            'alamat',
            'jenis_kelamin',
            'jenis_karyawan',
        ]
