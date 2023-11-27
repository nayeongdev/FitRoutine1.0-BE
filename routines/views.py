from django.shortcuts import render
from rest_framework import mixins
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import Exerciser, Routine
from .serializers import ExerciserSerializer, RoutineSerializer
from .permissions import IsAuthorOrReadOnly
import openai


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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)

        # ChatGPT와의 상호작용
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            max_tokens=1024,
            n=5,
            stop=None,
            temperature=0.5,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful exercise expert who plans personalized workout routines.",
                },
                {
                    "role": "user",
                    "content": f"사용자의 데이터에 맞춰서 운동 루틴을 계획하세요. 계획을 3줄 설명으로 요약한 다음 3개 목록으로 적어주세요. {serializer}",
                },
            ],
        )

        # ChatGPT의 응답을 가져와서 전달
        chat_gpt_response = response.choices[0].message["content"].strip()

        headers = self.get_success_headers(serializer.data)
        return Response(
            {"chat_gpt_response": chat_gpt_response},
            status=status.HTTP_201_CREATED,
            headers=headers,
        )


class RoutineViewSet(ModelViewSet):
    """
    A simple ViewSet for viewing and editing routines.
    """

    queryset = Routine.objects.all()
    serializer_class = RoutineSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    authentication_classes = [JWTAuthentication]
