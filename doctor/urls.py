from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()  # Corrected the typo

router.register('list', views.DoctorViewset)  # Changed 'view' to 'views'
router.register('specialization', views.SpecializationViewset)  # Changed 'view' to 'views'
router.register('available_time', views.AvailableTimeViewset)  # Changed 'view' to 'views'
router.register('designation', views.DesignationViewset)  # Changed 'view' to 'views'
router.register('reviews', views.ReviewViewset)  # Changed 'view' to 'views'

urlpatterns = [
    path("", include(router.urls)),
]
    