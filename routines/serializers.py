from rest_framework.serializers import ModelSerializer
from .models import CustomUser, Exerciser, Routine


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["email", "username"]


class ExerciserSerializer(ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Exerciser
        fields = "__all__"


class RoutineSerializer(ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Routine
        fields = "__all__"
