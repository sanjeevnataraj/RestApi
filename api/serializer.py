from rest_framework import serializers
from api.models import User, ActivityPeriod

class ActivePeriodSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityPeriod
        fields = ['start_time', 'end_time']

class UserSerializer(serializers.ModelSerializer):
    activity_periods = ActivePeriodSerializer(many=True, read_only=True, source="current_activity_data")
    class Meta:
        model = User
        fields = ['id', 'real_name', 'tz', 'activity_periods']