import math

from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.renderers import JSONRenderer

from .models import News, Contacts, Legals, Clubs, TrainingCourses, Events, Employees
from .serializers import AllNewsSerializers, LegalsSerializers, ContactsSerializers, AllClubsSerializers,\
    AllTrainingCoursesSerializers, AllEventsSerializers, AllEmployeesSerializers


def paginator(model, current_page, items=2):
    first_item = (current_page - 1) * items
    last_item = current_page * items

    model_part = model[first_item:last_item]

    return model_part

# Create your views here.


class AllNewsView(APIView):
    permission_classes = [permissions.AllowAny]

    renderer_classes = [JSONRenderer]

    def get(self, request, format=None):
        page_size = 3
        current_page = int(request.GET.get('current_page'))
        all_news = News.objects.all()

        response_news = paginator(all_news, current_page, page_size)
        serializer = AllNewsSerializers(response_news, many=True)

        total_news = all_news.count()

        content = {'data': serializer.data, 'total_news': total_news, 'page_size': page_size}
        return Response(content)


class LegalsView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        type_filter = request.GET.get('type_filter')

        if type_filter != '':
            legals = Legals.objects.filter(content_type=type_filter)
        else:
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

    renderer_classes = [JSONRenderer]

    def get(self, request):

        first_connection = request.GET.get('connection')

        if first_connection:
            last_event = Events.objects.last()
            first_event = Events.objects.first()

            last_year = getattr(last_event, 'date_placing').year
            first_year = getattr(first_event, 'date_placing').year

            count_year = last_year - first_year

        events = Events.objects.all()
        serializer = AllEventsSerializers(events, many=True)

        content = {'data': serializer.data}
        return Response(content)


