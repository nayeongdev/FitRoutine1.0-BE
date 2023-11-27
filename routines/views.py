from django.shortcuts import render
from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Exerciser, Routine
from .serializers import ExerciserSerializer, RoutineSerializer
from .permissions import IsAuthorOrReadOnly


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
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    authentication_classes = [JWTAuthentication]


class RoutineViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing routines.
    """

    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    authentication_classes = [JWTAuthentication]
