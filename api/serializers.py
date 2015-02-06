from django.contrib.auth.models import User, Group
from rest_framework import serializers
from users.models import UserProfile
from schedule.models import *
from submission.models import *

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'profile', 'groups')

class UserProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('url', 'user', 'display_name', 'bio', 'title', 'avatar')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ('url', 'name', 'user_set')

class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = ('url', 'shortname', 'fullname')

class TimeslotSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Timeslot
        fields = ('url', 'start', 'end', 'activity_set')

class ActivitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Activity
        fields = ('url', 'description', 'timeslot', 'room', 'submission')

class SubmissionSerializer(serializers.HyperlinkedModelSerializer):
    speaker = serializers.HyperlinkedRelatedField(source='user', view_name='user-detail', read_only=True)

    class Meta:
        model = Submission
        fields = ('url', 'speaker', 'title', 'type', 'abstract')