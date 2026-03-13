from django.shortcuts import render
# adrf.views dan APIView import qilinadi
from adrf.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .permissions import *  # Sizning custom permission
from .models import UserProfile
from .serializers import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from adrf.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import UserSerializer
from account.models import User
from asgiref.sync import sync_to_async
from drf_spectacular.utils import extend_schema
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny


class UserBalanceAPI(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrAdmin]

    async def get(self, request):
        try:
            # Asinxron tarzda profilni olish
            profile = await UserProfile.objects.aget(user=request.user)
            serializer = UserProfileSerializer(profile)

            return Response({
                "data": serializer.data,
                "status": status.HTTP_200_OK
            }, status=status.HTTP_200_OK)

        except UserProfile.DoesNotExist:
            return Response(
                {"error": "Profil topilmadi!"},
                status=status.HTTP_404_NOT_FOUND
            )


class ProfileAPI(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [JWTAuthentication]

    def get_queryset(self):
        user = self.request.user
        if user.is_staff or user.is_superuser:
            return User.objects.all()
        return User.objects.filter(id=user.id)

    def get_permissions(self):
        if self.action == 'create':
            # Ro'yxatdan o'tish hamma uchun ochiq
            return [AllowAny()]
        elif self.action in ['list', 'destroy']:
            # Ro'yxatni ko'rish va o'chirish faqat adminlarga
            return [permissions.IsAdminUser()]
        else:
            # retrieve, update, partial_update uchun:
            # login bo'lishi va o'z egasi bo'lishi shart
            return [IsAuthenticated(), IsOwnerOrAdmin()]

    def perform_update(self, serializer):
        # Bu yerda qo'shimcha logika yozish mumkin (masalan, email yuborish)
        serializer.save()