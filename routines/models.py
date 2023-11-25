from django.db import models
from accounts.models import CustomUser


class Exerciser(models.Model):
    LEVEL_CHOICES = (
        ("초급", "초급"),
        ("중급", "중급"),
        ("고급", "고급"),
    )

    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    goal = models.CharField(max_length=100, help_text="운동 목표")
    level = models.CharField(max_length=50, choices=LEVEL_CHOICES, help_text="운동 수준")
    exercise_place = models.CharField(max_length=100, help_text="운동 장소")
    preferred_exercise = models.CharField(max_length=100, help_text="선호하는 운동 종목")
    exercise_duration = models.IntegerField(help_text="운동 시간(분)")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.affiliation_type} - {self.level} 운동"


class Routine(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    exerciser_info = models.ForeignKey(Exerciser, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100, help_text="루틴 제목")
    content = models.TextField(help_text="루틴 내용")
    created_at = models.DateTimeField(auto_now_add=True, help_text="루틴 생성일")
    updated_at = models.DateTimeField(auto_now=True, help_text="루틴 최근 수정일")

    def __str__(self):
        return f"{self.title}"
