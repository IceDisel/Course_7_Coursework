from rest_framework import serializers

from habit_tracker.models import Habit
from habit_tracker.validators import validate_habit_fields, validate_time_required, validate_related_habit, \
    validate_pleasurable_habit


class HabitsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habit
        fields = '__all__'
        read_only_fields = ('user',)

    def validate(self, data):
        validate_habit_fields(data)
        validate_time_required(data)
        validate_related_habit(data)
        validate_pleasurable_habit(data)
        return data
