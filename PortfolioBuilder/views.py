from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import *
from .serializers import *

# Create your views here.


"""@api_view(['GET'])
def get_all_PersonalInfo(request):
    if request.method == 'GET':
        personal_info = PersonalInfo.objects.all()
        if not personal_info:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = PersonalInfoSerializer(personal_info, many=True)  # convert user objects to json
        return Response(serializer.data, status=status.HTTP_200_OK)
    return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
def add_personalInfo(request):
    if request.method == 'POST':
        personal_info = PersonalInfoSerializer(data=request.data)
        if personal_info.is_valid():
            personal_info.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(PersonalInfo.errors, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['DELETE'])
def delete_personalInfo(request, id):
    if request.method == 'DELETE':
        try:
            personalInfo = PersonalInfo.objects.get(pk=id)
            personalInfo.delete()
            return JsonResponse({"message": "the user has been successfuly removed."},
                                status=status.HTTP_202_ACCEPTED)
        except personalInfo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['PUT'])
def update_personalInfo(request):
    serializer = PersonalInfoSerializer(PersonalInfo, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(status=status.HTTP_202_ACCEPTED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_all_Person(request):
    if request.method == 'GET':
        person = Person.objects.all()
        if not person:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = PersonalInfoSerializer(person, many=True)  # convert user objects to json
        return Response(serializer.data, status=status.HTTP_200_OK)
    return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)"""


@api_view(['GET'])
def get_all_users(request):
    if request.method == 'GET':
        users = User.objects.all()  # get all  users from the database
        if not users:  # or if len(users) ==0 or if bool(users): #if there is no user in the list 
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = UserSerializer(users, many=True)  # convert user objects to json
        return Response(serializer.data, status=status.HTTP_200_OK)
    return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
def add_user(request):
    if request.method == 'POST':
        user = UserSerializer(data=request.data)  # get the user object from the request after deserialization
        if user.is_valid():  # check if the user object is valid (all required fields are filled and fields data types and format are correct)
            user.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(user.errors, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'PUT', 'DELETE'])
def get_update_or_delete_user(request, id):
    try:
        user = User.objects.get(pk=id)
        if request.method == 'GET':

            serializer = UserSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            serialzer = UserSerializer(user,
                                       data=request.data)  # get group informations from the request and update the instance of group geted by nid from the DB.
            if serialzer.is_valid():
                serialzer.save()
                return Response(status=status.HTTP_202_ACCEPTED)
            return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            User.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)  # to say that the deleted group no longer exists
            # or
            # return JsonResponse({"message":"The group was successuflly deleted"},status=status.HTTP_202_ACCEPTED)
        return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


"""*****************************************************************************************************"""


@api_view(['GET'])
def get_all_address(request):
    if request.method == 'GET':
        address = Address.objects.all()
        if not address:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = AddressSerializer(address, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
def add_address(request):
    if request.method == 'POST':
        address = AddressSerializer(data=request.data)
        if address.is_valid():  # check if the user object is valid (all required fields are filled and fields data types and format are correct)
            address.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(address.errors, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'PUT', 'DELETE'])
def get_update_or_delete_address(request, id):
    try:
        address = Address.objects.get(pk=id)
        if request.method == 'GET':

            serializer = AddressSerializer(address)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            serialzer = AddressSerializer(address,
                                          data=request.data)  # get group informations from the request and update the instance of group geted by nid from the DB.
            if serialzer.is_valid():
                serialzer.save()
                return Response(status=status.HTTP_202_ACCEPTED)
            return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            address.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)  # to say that the deleted group no longer exists
            # or
            # return JsonResponse({"message":"The group was successuflly deleted"},status=status.HTTP_202_ACCEPTED)
        return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    except address.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_all_admin(request):
    if request.method == 'GET':
        admin = Admin.objects.all()
        if not admin:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = AdminSerializer(admin, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
def add_admin(request):
    if request.method == 'POST':
        admin = AdminSerializer(data=request.data)
        if admin.is_valid():  # check if the user object is valid (all required fields are filled and fields data types and format are correct)
            admin.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(admin.errors, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'PUT', 'DELETE'])
def get_update_or_delete_admin(request, id):
    try:
        admin = Admin.objects.get(pk=id)
        if request.method == 'GET':

            serializer = AdminSerializer(admin)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            serialzer = AdminSerializer(admin,
                                        data=request.data)  # get group informations from the request and update the instance of group geted by nid from the DB.
            if serialzer.is_valid():
                serialzer.save()
                return Response(status=status.HTTP_202_ACCEPTED)
            return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            admin.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)  # to say that the deleted group no longer exists
            # or
            # return JsonResponse({"message":"The group was successuflly deleted"},status=status.HTTP_202_ACCEPTED)
        return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    except admin.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_all_personalInfo(request):
    if request.method == 'GET':
        personalInfo = PersonalInfo.objects.all()
        if not personalInfo:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = PersonalInfoSerializer(personalInfo, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
def add_personalInfo(request):
    if request.method == 'POST':
        personalInfo = PersonalInfoSerializer(data=request.data)
        if personalInfo.is_valid():  # check if the user object is valid (all required fields are filled and fields data types and format are correct)
            personalInfo.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(personalInfo.errors, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'PUT', 'DELETE'])
def get_update_or_delete_personalInfo(request, id):
    try:
        personalInfo = PersonalInfo.objects.get(pk=id)
        if request.method == 'GET':

            serializer = PersonalInfoSerializer(personalInfo)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            serialzer = PersonalInfoSerializer(personalInfo,
                                               data=request.data)  # get group informations from the request and update the instance of group geted by nid from the DB.
            if serialzer.is_valid():
                serialzer.save()
                return Response(status=status.HTTP_202_ACCEPTED)
            return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            personalInfo.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)  # to say that the deleted group no longer exists
            # or
            # return JsonResponse({"message":"The group was successuflly deleted"},status=status.HTTP_202_ACCEPTED)
        return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    except personalInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_all_awards(request):
    if request.method == 'GET':
        awards = Awards.objects.all()
        if not awards:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = AwardsSerializer(awards, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
def add_award(request):
    if request.method == 'POST':
        awards = AwardsSerializer(data=request.data)
        if awards.is_valid():  # check if the user object is valid (all required fields are filled and fields data types and format are correct)
            awards.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(awards.errors, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'PUT', 'DELETE'])
def get_update_or_delete_award(request, id):
    try:
        awards = Awards.objects.get(pk=id)
        if request.method == 'GET':

            serializer = AwardsSerializer(awards)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            serialzer = AwardsSerializer(awards,
                                         data=request.data)  # get group informations from the request and update the instance of group geted by nid from the DB.
            if serialzer.is_valid():
                serialzer.save()
                return Response(status=status.HTTP_202_ACCEPTED)
            return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            awards.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)  # to say that the deleted group no longer exists
            # or
            # return JsonResponse({"message":"The group was successuflly deleted"},status=status.HTTP_202_ACCEPTED)
        return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    except awards.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_all_transcripts(request):
    if request.method == 'GET':
        transcripts = Transcripts.objects.all()
        if not Transcripts:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = TranscriptsSerializer(transcripts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
def add_transcripts(request):
    if request.method == 'POST':
        transcripts = TranscriptsSerializer(data=request.data)
        if Transcripts.is_valid():  # check if the user object is valid (all required fields are filled and fields data types and format are correct)
            transcripts.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(transcripts.errors, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'PUT', 'DELETE'])
def get_update_or_delete_transcripts(request, id):
    try:
        transcripts = Transcripts.objects.get(pk=id)
        if request.method == 'GET':

            serializer = TranscriptsSerializer(transcripts)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            serialzer = TranscriptsSerializer(transcripts,
                                              data=request.data)  # get group informations from the request and update the instance of group geted by nid from the DB.
            if serialzer.is_valid():
                serialzer.save()
                return Response(status=status.HTTP_202_ACCEPTED)
            return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            transcripts.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)  # to say that the deleted group no longer exists
            # or
            # return JsonResponse({"message":"The group was successuflly deleted"},status=status.HTTP_202_ACCEPTED)
        return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    except transcripts.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_all_experiences(request):
    if request.method == 'GET':
        experiences = Experiences.objects.all()
        if not experiences:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = ExperiencesSerializer(experiences, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
def add_experience(request):
    if request.method == 'POST':
        experiences = ExperiencesSerializer(data=request.data)
        if experiences.is_valid():  # check if the user object is valid (all required fields are filled and fields data types and format are correct)
            experiences.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(experiences.errors, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'PUT', 'DELETE'])
def get_update_or_delete_experience(request, id):
    try:
        experiences = Experiences.objects.get(pk=id)
        if request.method == 'GET':

            serializer = ExperiencesSerializer(experiences)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            serialzer = ExperiencesSerializer(experiences,
                                              data=request.data)  # get group informations from the request and update the instance of group geted by nid from the DB.
            if serialzer.is_valid():
                serialzer.save()
                return Response(status=status.HTTP_202_ACCEPTED)
            return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            experiences.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)  # to say that the deleted group no longer exists
            # or
            # return JsonResponse({"message":"The group was successuflly deleted"},status=status.HTTP_202_ACCEPTED)
        return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    except experiences.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_all_references(request):
    if request.method == 'GET':
        references = References.objects.all()
        if not references:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = ReferencesSerializer(references, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
def add_reference(request):
    if request.method == 'POST':
        references = ReferencesSerializer(data=request.data)
        if references.is_valid():  # check if the user object is valid (all required fields are filled and fields data types and format are correct)
            references.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(references.errors, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'PUT', 'DELETE'])
def get_update_or_delete_reference(request, id):
    try:
        references = References.objects.get(pk=id)
        if request.method == 'GET':

            serializer = ReferencesSerializer(references)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            serialzer = ReferencesSerializer(references,
                                             data=request.data)  # get group informations from the request and update the instance of group geted by nid from the DB.
            if serialzer.is_valid():
                serialzer.save()
                return Response(status=status.HTTP_202_ACCEPTED)
            return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            references.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)  # to say that the deleted group no longer exists
            # or
            # return JsonResponse({"message":"The group was successuflly deleted"},status=status.HTTP_202_ACCEPTED)
        return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    except references.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_all_volunteering(request):
    if request.method == 'GET':
        volunteering = Volunteering.objects.all()
        if not volunteering:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = VolunteeringSerializer(volunteering, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
def add_reference(request):
    if request.method == 'POST':
        volunteering = VolunteeringSerializer(data=request.data)
        if volunteering.is_valid():  # check if the user object is valid (all required fields are filled and fields data types and format are correct)
            volunteering.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(volunteering.errors, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['GET', 'PUT', 'DELETE'])
def get_update_or_delete_reference(request, id):
    try:
        volunteering = Volunteering.objects.get(pk=id)
        if request.method == 'GET':

            serializer = VolunteeringSerializer(volunteering)
            return Response(serializer.data, status=status.HTTP_200_OK)

        elif request.method == 'PUT':
            serialzer = VolunteeringSerializer(volunteering,
                                       data=request.data)  # get group informations from the request and update the instance of group geted by nid from the DB.
            if serialzer.is_valid():
                serialzer.save()
                return Response(status=status.HTTP_202_ACCEPTED)
            return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE':
            volunteering.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)  # to say that the deleted group no longer exists
            # or
            # return JsonResponse({"message":"The group was successuflly deleted"},status=status.HTTP_202_ACCEPTED)
        return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
    except volunteering.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)