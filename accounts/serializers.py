from rest_framework import serializers, exceptions
from rest_framework_simplejwt.tokens import RefreshToken, TokenError

# 중복 검사(회원 가입할 때 동일한 아이디가 있는지 검사 등)
from rest_framework.validators import UniqueValidator
from django.contrib.auth.password_validation import validate_password  # 비밀번호 유효성 검사
from .models import CustomUser
from django.contrib.auth import authenticate  # 인증 모듈


class RegistrationSerializer(serializers.ModelSerializer):
    """
    회원 가입 시리얼라이저
    """

    username = serializers.CharField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())],  # 중복 검사
    )

    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=CustomUser.objects.all())],  # 중복 검사
    )
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )  # 비밀번호 유효성 검사(너무 짧은 비밀번호 등)
    password2 = serializers.CharField(write_only=True, required=True)  # 비밀번호 확인 필드

    class Meta:
        model = CustomUser
        fields = [
            "email",
            "username",
            "password",
            "password2",
            "date_of_birth",
            "height",
            "weight",
            "gender",
        ]

    def validate(self, attrs):
        """비밀번호 일치 검사"""
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError({"password": "비밀번호가 일치하지 않습니다."})
        return attrs

    def create(self, validated_data):
        """Return user after creation."""
        user = CustomUser.objects.create(
            username=validated_data["username"], email=validated_data["email"]
        )
        user.set_password(validated_data["password"])  # 비밀번호 암호화
        user.save()
        
        user.date_of_birth = validated_data.get("date_of_birth", None)
        user.height = validated_data.get("height", None)
        user.weight = validated_data.get("weight", None)
        user.gender = validated_data.get("gender", None)
        user.save(update_fields=["date_of_birth", "height", "weight", "gender"])
        return user


class LoginSerializer(serializers.ModelSerializer):
    """
    로그인 시리얼라이저
    """

    email = serializers.CharField(required=True)
    password = serializers.CharField(
        write_only=True, required=True
    )  # write_only=True: password 필드는 읽기 전용으로 설정

    tokens = serializers.SerializerMethodField()

    def get_tokens(self, obj):  # type: ignore
        """Get user token."""
        user = CustomUser.objects.get(email=obj.email)

        return {"refresh": user.tokens["refresh"], "access": user.tokens["access"]}

    class Meta:
        model = CustomUser
        fields = ["email", "password", "password", "tokens"]

    def validate(self, data):
        """Validate and return user login."""
        email = data.get("email", None)
        password = data.get("password", None)

        if email is None:
            raise serializers.ValidationError("이메일 주소가 필요합니다.")

        if password is None:
            raise serializers.ValidationError("비밀번호가 필요합니다.")

        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError("이 이메일과 비밀번호를 가진 사용자를 찾을 수 없습니다.")

        if not user.is_active:
            raise serializers.ValidationError("활성화되지 않은 사용자입니다.")

        return user


class LogoutSerializer(serializers.ModelSerializer):
    """
    로그아웃 시리얼라이저
    """

    refresh = serializers.CharField()

    def validate(self, attrs):  # type: ignore
        """Validate token."""
        self.token = attrs["refresh"]
        return attrs

    def save(self, **kwargs):  # type: ignore
        """Validate save backlisted token."""

        try:
            RefreshToken(self.token).blacklist()

        except TokenError as ex:
            raise exceptions.AuthenticationFailed(ex)
