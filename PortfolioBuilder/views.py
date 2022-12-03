from django.http import JsonResponse
from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import PersonalInfo, Person
from .serializers import PersonalInfoSerializer, PersonSerializer


# Create your views here.


@api_view(['GET'])
def get_all_PersonalInfo(request):
    if request.method == 'GET':
        personal_info = PersonalInfo.objects.all()
        if not personal_info:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = PersonalInfoSerializer(personal_info, many=True)  # convert student objects to json
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
            return JsonResponse({"message": "the student has been successfuly removed."},
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
        serializer = PersonalInfoSerializer(person, many=True)  # convert student objects to json
        return Response(serializer.data, status=status.HTTP_200_OK)
    return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

