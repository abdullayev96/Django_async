from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Author
from .serializers import AuthorSerializers
from adrf.views import APIView


class AuthorListAPI(APIView):
    async def get(self, request):
        queryset = Author.objects.all()
        categories_list = [c async for c in queryset]

        serializer = AuthorSerializers(categories_list, many=True, context={'request': request})

        return Response(serializer.data)
