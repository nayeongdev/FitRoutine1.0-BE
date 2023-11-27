from rest_framework.serializers import ModelSerializer
from .models import Exerciser, Routine


class ExerciserSerializer(ModelSerializer):
    class Meta:
        model = Exerciser
        fields = "__all__"


class RoutineSerializer(ModelSerializer):
    class Meta:
        model = Routine
        fields = "__all__"
