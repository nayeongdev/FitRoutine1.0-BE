from django.shortcuts import render
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework import mixins
from .models import Exerciser, Routine
from .serializers import ExerciserSerializer, RoutineSerializer


class ExerciserViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet,
):
    """
    A viewset that provides `retrieve`, `create`, and `list` actions.
    """

    queryset = Exerciser.objects.all()
    serializer_class = ExerciserSerializer


class RoutineViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing routines.
    """

    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer
