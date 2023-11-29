from rest_framework.serializers import ModelSerializer
from .models import CustomUser, Exerciser, Routine


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["email", "username"]


class ExerciserInfoSerializer(ModelSerializer):
    class Meta:
        model = Exerciser
        fields = [
            "goal",
            "level",
            "exercise_place",
            "preferred_exercise",
            "exercise_duration",
        ]


class ExerciserSerializer(ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Exerciser
        fields = "__all__"


class RoutineSerializer(ModelSerializer):
    author = AuthorSerializer(read_only=True)
    exerciser_info = ExerciserInfoSerializer(read_only=True)

    class Meta:
        model = Routine
        fields = "__all__"
