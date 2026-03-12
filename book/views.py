from django.shortcuts import render
from rest_framework.response import Response
from .models import Book
from .serializers import BookSerializers
from drf_spectacular.utils import extend_schema, extend_schema_view
from adrf.views import APIView


class BookListAPI(APIView):

    async def get(self, request):
        queryset = Book.objects.all()
        categories_list = [c async for c in queryset]

        serializer = BookSerializers(categories_list, many=True, context={"request":request})

        return Response(serializer.data)

