from rest_framework import serializers

from .models import ContentTypesNews, News, ContentTypesLegals, Legals, TypesRelationContacts, Contacts,\
    ActivityTypesClubs, Clubs, TrainingCourses, Events


class ContentTypesNewsSerializers(serializers.ModelSerializer):

    class Meta:

        model = ContentTypesNews
        fields = ('id', 'name')


class AllNewsSerializers(serializers.ModelSerializer):

    content_types = ContentTypesNewsSerializers(many=True)

    class Meta:

        model = News
        fields = ('id', 'title', 'post_date', 'description', 'image', 'detail', 'visitors_type', 'content_types')


class ContentTypesLegalsSerializers(serializers.ModelSerializer):

    class Meta:

        model = ContentTypesLegals
        fields = ('id', 'name')


class LegalsSerializers(serializers.ModelSerializer):

    content_type = ContentTypesLegalsSerializers()

    class Meta:

        model = Legals
        fields = ('id', 'name', 'detail', 'content_type')


class TypesRelationContactsSerializers(serializers.ModelSerializer):

    class Meta:

        model = TypesRelationContacts
        fields = ('id', 'name')


class ContactsSerializers(serializers.ModelSerializer):

    type_relation = TypesRelationContactsSerializers()

    class Meta:

        model = Contacts
        fields = ('id', 'label', 'content', 'type_relation')


class ActivityTypesClubsSerializers(serializers.ModelSerializer):

    class Meta:

        model = ActivityTypesClubs
        fields = ('id', 'name')


class AllClubsSerializers(serializers.ModelSerializer):

    activity_type = ActivityTypesClubsSerializers()

    class Meta:

        model = Clubs
        fields = ('id', 'name', 'description', 'image', 'detail',  'season_set', 'members_age', 'activity_type')


class AllTrainingCoursesSerializers(serializers.ModelSerializer):

    class Meta:

        model = TrainingCourses
        fields = ('id', 'name', 'description', 'image', 'detail')


class AllEventsSerializers(serializers.ModelSerializer):

    class Meta:

        model = Events
        fields = ('id', 'name', 'date_placing', 'detail')

