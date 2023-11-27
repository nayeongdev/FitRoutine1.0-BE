from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("routines", views.RoutineViewSet)
router.register("maker", views.ExerciserViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
