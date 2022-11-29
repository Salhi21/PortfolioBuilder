from .models import PersonalInfo, Person
from rest_framework import viewsets
from .serializers import PersonalInfoSerializer, PersonSerializer


class PersonalInfoViewSet(viewsets.ModelViewSet):
    queryset = PersonalInfo.objects.all()
    serializer_class = PersonalInfoSerializer
    http_method_name = ['get', 'post', 'DELETE']


class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    http_method_name = ['post']
