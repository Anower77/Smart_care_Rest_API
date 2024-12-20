from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()  # Corrected the typo
router.register('', views.ServiceViewset)  # Changed 'view' to 'views'

urlpatterns = [
    path("", include(router.urls)),
]
