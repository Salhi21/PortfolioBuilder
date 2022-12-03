from .models import *
from rest_framework import viewsets
from .serializers import *


class PersonalInfoViewSet(viewsets.ModelViewSet):
    queryset = PersonalInfo.objects.all()
    serializer_class = PersonalInfoSerializer
    http_method_name = ['get', 'post', 'put', 'delete', 'patch']


"""class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer
    http_method_name = ['get', 'post', 'put', 'delete', 'patch']"""


class AddressViewSet(viewsets.ModelViewSet):
    queryset = Address.objects.all()
    serializer_class = AddressSerializer
    http_method_name = ['get', 'post', 'put', 'delete', 'patch']


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    http_method_name = ['get', 'post', 'put', 'delete', 'patch']


class AdminViewSet(viewsets.ModelViewSet):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    http_method_name = ['get', 'post', 'put', 'delete', 'patch']



class AwardsViewSet(viewsets.ModelViewSet):
    queryset = Awards.objects.all()
    serializer_class = AwardsSerializer
    http_method_name = ['get', 'post', 'put', 'delete', 'patch']


class TranscriptsViewSet(viewsets.ModelViewSet):
    queryset = Transcripts.objects.all()
    serializer_class = TranscriptsSerializer
    http_method_name = ['get', 'post', 'put', 'delete', 'patch']


class ExperiencesViewSet(viewsets.ModelViewSet):
    queryset = Experiences.objects.all()
    serializer_class = ExperiencesSerializer
    http_method_name = ['get', 'post', 'put', 'delete', 'patch']


class ReferencesViewSet(viewsets.ModelViewSet):
    queryset = References.objects.all()
    serializer_class = ReferencesSerializer
    http_method_name = ['get', 'post', 'put', 'delete', 'patch']


class VolunteeringViewSet(viewsets.ModelViewSet):
    queryset = Volunteering.objects.all()
    serializer_class = VolunteeringSerializer
    http_method_name = ['get', 'post', 'put', 'delete', 'patch']