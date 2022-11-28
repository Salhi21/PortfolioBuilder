from django.shortcuts import render
from .models import PersonalInfo
from .serializers import PersonalInfoSerializer


# Create your views here.


@api_view(['GET'])
def get_all_PersonalInfo(request):
    if request.method == 'GET':
        PersonalInfo = PersonalInfo.objects.all()
        if not PersonalInfo:
            return Response(status=status.HTTP_204_NO_CONTENT)
        serializer = PersonalInfoSerializer(students, many=True)  # convert student objects to json
        return Response(serializer.data, status=status.HTTP_200_OK)
    return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['POST'])
def add_personalInfo(request):
    if request.method == 'POST':
        personal_info = PersonalInfoSerializer(data=request.data)
        if personal_info.is_valid():
            personal_info.save()
            return Response(status=status.HTTP_201_CREATED)
        return Response(student.errors, status=status.HTTP_400_BAD_REQUEST)
    return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)


@api_view(['DELETE'])
def delete_personalInfo(request, id):
    if request.method == 'DELETE':
        try:
            personalInfo = personalInfo.objects.get(pk=id)
            personalInfo.delete()
            return JsonResponse({"message": "the student has been successfuly removed."},
                                status=status.HTTP_202_ACCEPTED)
        except personalInfo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    return JsonResponse({"message": "The method is not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
