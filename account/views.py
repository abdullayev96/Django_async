from django.shortcuts import render
from adrf.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import User
from .serializers import *
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth import authenticate
from django.middleware import csrf
from rest_framework_simplejwt.tokens import RefreshToken
from .permissions import IsLoggedInUserOrAdmin, IsAdminUser
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.sessions.models import Session
from django.utils.timezone import now
from datetime import timedelta
from asgiref.sync import sync_to_async
from drf_spectacular.utils import extend_schema, OpenApiResponse

import logging

logger = logging.getLogger(__name__)


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("api_requests.log"),
        logging.StreamHandler()
    ]
)


class RegisterAPI(APIView):
    async def post(self, request):
        serializer = RegisterSerializer(data=request.data)

        is_valid = await sync_to_async(serializer.is_valid)()

        if is_valid:
            try:
                user = await sync_to_async(serializer.save)()

                logger.info(f"Yangi foydalanuvchi: {user.email}")

                return Response({
                    "success": True,
                    "message": "Ro'yxatdan o'tish muvaffaqiyatli yakunlandi."
                }, status=status.HTTP_201_CREATED)

            except Exception as e:
                logger.error(f"Saqlashda xatolik: {e}")
                return Response({"error": "Ma'lumotlarni saqlashda xatolik."}, status=500)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh_token': str(refresh),
        'access_token': str(refresh.access_token),
    }


class LoginAPI(APIView):
    permission_classes = [AllowAny]
    serializer_class = LoginSerializer

    @extend_schema(
        request=LoginSerializer,
        responses={200: LoginResponseSerializer},
        summary='Foydalanuvchi logini'
    )
    async def post(self, request):
        serializer = self.serializer_class(
            data=request.data,
            context={'request': request}
        )
        is_valid = await sync_to_async(serializer.is_valid)()

        if not is_valid:
            return Response(
                {'message': 'Validatsiya xatosi', 'errors': serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )

        user = serializer.validated_data['user']

        if not user.is_active:
            return Response(
                {'message': 'Akkauntingiz faol emas'},
                status=status.HTTP_403_FORBIDDEN
            )

        try:
            # Token yaratish (asinxron oqimda)
            tokens = await sync_to_async(self._get_tokens_for_user)(user)
            logger.info(f'User logged in: {user.email}')

            return Response(
                {
                    'data': tokens,
                    'message': 'Muvaffaqiyatli login'
                },
                status=status.HTTP_200_OK
            )
        except Exception as e:
            logger.error(f'Token xatosi: {str(e)}')
            return Response(
                {'message': 'Serverda xatolik'},
                status=500
            )

    @staticmethod
    def _get_tokens_for_user(user):
        refresh = RefreshToken.for_user(user)
        return {
            'refresh_token': str(refresh),
            'access_token': str(refresh.access_token),
        }
