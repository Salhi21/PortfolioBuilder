from django.urls import include, path
from rest_framework import routers
from . import views

from PortfolioBuilder.viewsets import PersonalInfoViewSet, PersonViewSet

router=routers.DefaultRouter() #get the default router object defined in rest_framework
#add router for each viewset (StudentViewest, GroupViewSet, AddressViewSet) to the router object
router.register(r'personalInfo', PersonalInfoViewSet)
router.register(r'Person', PersonViewSet)

#each time we use the path '/students' in the url,
#the StudentViewSet will be called
#the prefix r is used to indicate that the string is a raw string (not interpret the backslash as an escape character)

# #add the router to the urlpatterns
# urlpatterns = [
#     path('', include(router.urls)),
# ]


urlpatterns = [
    path('', include(router.urls)),
    path(r'personalInfo/all/', views.get_all_PersonalInfo),
    path(r'personalInfo/add/', views.add_personalInfo),
    path(r'personalInfo/delete/', views.delete_personalInfo),
    path(r'personalInfo/update/', views.update_personalInfo),
    path(r'Person/add/', views.add_account)
]

