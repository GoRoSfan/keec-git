from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from .models import News, Contacts, Legals, Clubs, TrainingCourses, Events
from .serializers import AllNewsSerializers, LegalsSerializers, ContactsSerializers, AllClubsSerializers,\
    AllTrainingCoursesSerializers, AllEventsSerializers

# Create your views here.


class AllNewsView(APIView):

    def get(self, request):
        news = News.objects.all()
        serializer = AllNewsSerializers(news, many=True)
        return Response({'data': serializer.data})


class LegalsView(APIView):

    def get(self, request):
        legals = Legals.objects.all()
        serializer = LegalsSerializers(legals, many=True)
        return Response({'data': serializer.data})


class ContactsView(APIView):

    def get(self, request):
        contacts = Contacts.objects.all()
        serializer = ContactsSerializers(contacts, many=True)
        return Response({'data': serializer.data})


class AllClubsView(APIView):

    def get(self, request):
        clubs = Clubs.objects.all()
        training_courses = TrainingCourses.objects.all()
        serializer_clubs = AllClubsSerializers(clubs, many=True)
        serializer_courses = AllTrainingCoursesSerializers(training_courses, many=True)
        serializer = {'serializer_courses': serializer_courses.data, 'serializer_clubs': serializer_clubs}
        return Response({'data': serializer})
