from .models import PersonalInfo
from rest_framework import viewsets
from .serializers import PersonalInfoSerializer


class PersonalInfoViewSet(viewsets.ModelViewSet):
    queryset = PersonalInfo.objects.all()
    serializer_class = PersonalInfoSerializer
    http_method_name = ['get', 'post', 'DELETE']

