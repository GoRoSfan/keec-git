from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from .models import ContentTypesNews, News
from .serializers import AllNewsSerializers

# Create your views here.


class AllNewsView(APIView):

    def get(self, request):
        news = News.objects.all()
        serializer = AllNewsSerializers(news, many=True)
        return Response({'data': serializer.data})
