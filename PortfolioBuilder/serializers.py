from .models import PersonalInfo, Person


class PersonalInfoSerializer(PersonalInfo.ModelSerializer):
    class Meta:
        model = PersonalInfo
        fields = '__all__'


class PersonSerializer(Person.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'
