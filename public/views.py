from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from .models import News, Contacts, Legals, Clubs, TrainingCourses, Events
from .serializers import AllNewsSerializers, LegalsSerializers, ContactsSerializers, AllClubsSerializers,\
    AllTrainingCoursesSerializers, AllEventsSerializers

# Create your views here.


class AllNewsView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        news = News.objects.all()
        serializer = AllNewsSerializers(news, many=True)
        return Response({'data': serializer.data})


class LegalsView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        legals = Legals.objects.all()
        serializer = LegalsSerializers(legals, many=True)
        return Response({'data': serializer.data})


class ContactsView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        contacts = Contacts.objects.all()
        serializer = ContactsSerializers(contacts, many=True)
        return Response({'data': serializer.data})


class AllClubsView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        clubs = Clubs.objects.all()
        serializer = AllClubsSerializers(clubs, many=True)
        return Response({'data': serializer.data})


class AllTrainingCoursesView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        training_courses = TrainingCourses.objects.all()
        serializer_courses = AllTrainingCoursesSerializers(training_courses, many=True)
        return Response({'data': serializer_courses.data})


class AllEventsView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        events = Events.objects.all()
        serializer = AllEventsSerializers(events, many=True)
        return Response({'data': serializer.data})

