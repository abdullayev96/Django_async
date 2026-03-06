from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Category
from .serializers import CategorySerializers
from asgiref.sync import sync_to_async
from django.views import View
from django.http import JsonResponse


#
# class AuthorListAPI(APIView):
#     def get(self, request):
#         categories = Category.objects.all()
#         serializer = CategorySerializers(categories, many=True)
#         return Response(serializer.data)


class CategoryListAPI(View):  # DRF emas, Django's View
    async def get(self, request):
        data = await sync_to_async(self.get_data)()
        return JsonResponse(data, safe=False)

    def get_data(self):
        categories = Category.objects.all()
        serializer = CategorySerializers(categories, many=True)
        return serializer.data