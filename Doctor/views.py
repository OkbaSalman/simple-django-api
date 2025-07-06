from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Doctor
from .serializers import DoctorSerializer
# Create your views here.
class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class=DoctorSerializer
    filter_backends=[DjangoFilterBackend]
    filterset_fields=["isAvailable"]