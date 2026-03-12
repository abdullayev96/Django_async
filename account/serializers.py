from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth import authenticate
User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password],
        style={'input_type': 'password'}
    )

    password_confirm = serializers.CharField(
        write_only=True,
        required=True,
        style={'input_type': 'password'}
    )

    class Meta:
        model = User
        fields = ('id', 'email', 'password', 'password_confirm')

    def validate(self, attrs):
        if attrs['password'] != attrs['password_confirm']:
            raise serializers.ValidationError({"password": "Parollar mos kelmadi."})
        return attrs

    def create(self, validated_data):
        validated_data.pop('password_confirm')

        # UserManager.create_user metodini chaqiramiz
        # U o'zi parolni heshlaydi va emailni normallashtiradi
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(
        style={'input_type': 'password'},
        write_only=True
    )

    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if email and password:
            user = authenticate(request=self.context.get('request'),
                                email=email, password=password)

            if not user:
                raise serializers.ValidationError(
                    "Email yoki parol xato, yoki profil faollashtirilmagan.",
                    code='authorization'
                )
        else:
            raise serializers.ValidationError("Email va parolni kiritish shart.")

        attrs['user'] = user
        return attrs

class TokenSerializer(serializers.Serializer):
    """Token response serializer."""
    access = serializers.CharField()
    refresh = serializers.CharField()


class LoginResponseSerializer(serializers.Serializer):
    """Success response serializer."""
    data = TokenSerializer()
    message = serializers.CharField()


class ErrorResponseSerializer(serializers.Serializer):
    """Error response serializer."""
    message = serializers.CharField()
    errors = serializers.DictField(required=False)