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
    path(r'user/', views.get_all_users),
    path(r'user/add/', views.add_user),
    path(r'user/<int:id>', views.get_update_or_delete_user),
    path(r'address/', views.get_all_address),
    path(r'address/add/', views.add_address),
    path(r'address/<int:id>', views.get_update_or_delete_address),
    path(r'admin/', views.get_all_admin),
    path(r'admin/add/', views.add_admin),
    path(r'admin/<int:id>', views.get_update_or_delete_admin),
    path(r'personalInfo/', views.get_all_personalInfo),
    path(r'personalInfo/add/', views.add_personalInfo),
    path(r'personalInfo/<int:id>', views.get_update_or_delete_personalInfo),
    path(r'awards/', views.get_all_awards),
    path(r'awards/add/', views.add_award),
    path(r'awards/<int:id>', views.get_update_or_delete_award),
    path(r'transcripts/', views.get_all_transcripts),
    path(r'transcripts/add/', views.add_transcripts),
    path(r'transcripts/<int:id>', views.get_update_or_delete_transcripts),
    path(r'experiences/', views.get_all_experiences),
    path(r'experiences/add/', views.add_experience),
    path(r'experiences/<int:id>', views.get_update_or_delete_experience),
    path(r'references/', views.get_all_references),
    path(r'references/add/', views.add_reference),
    path(r'references/<int:id>', views.get_update_or_delete_reference),
    path(r'volunteering/', views.get_all_references),
    path(r'volunteering/add/', views.add_reference),
    path(r'volunteering/<int:id>', views.get_update_or_delete_reference),
]
