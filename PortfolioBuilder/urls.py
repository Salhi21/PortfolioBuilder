from django.urls import include, path
from rest_framework import routers
from . import views

from PortfolioBuilder.viewsets import *

router = routers.DefaultRouter()  # get the default router object defined in rest_framework
# add router for each viewset to the router object
router.register(r'personalInfo', PersonalInfoViewSet)
router.register(r'Address', AddressViewSet)
router.register(r'User', UserViewSet)
router.register(r'Admin', AdminViewSet)
router.register(r'Awards', AwardsViewSet)
router.register(r'Transcripts', TranscriptsViewSet)
router.register(r'Experiences', ExperiencesViewSet)
router.register(r'References', ReferencesViewSet)
router.register(r'Volunteering', VolunteeringViewSet)




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

]
