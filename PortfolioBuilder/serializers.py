from .models import *
from rest_framework import serializers


class PersonalInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = PersonalInfo
        fields = '__all__'


class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'




class AwardsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Awards
        fields = '__all__'


class TranscriptsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transcripts
        fields = '__all__'


class ExperiencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Experiences
        fields = '__all__'


class ReferencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = References
        fields = '__all__'


class VolunteeringSerializer(serializers.ModelSerializer):
    class Meta:
        model = Volunteering
        fields = '__all__'
