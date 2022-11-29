from .models import PersonalInfo


class PersonalInfoSerializer(PersonalInfo.ModelSerializer):
    class Meta:
        model = PersonalInfo
        fields = '__all__'
