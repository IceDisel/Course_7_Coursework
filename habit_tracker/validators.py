from django.core.exceptions import ValidationError


def validate_habit_fields(value):
    if value.get('reward') and value.get('related_habit'):
        raise ValidationError("Нельзя указывать одновременно вознаграждение и связанную привычку.")


def validate_time_required(value):
    if value.get('time_required').total_seconds() > 120:
        raise ValidationError("Время выполнения должно быть не больше 120 секунд.")


def validate_related_habit(value):
    if value.get('related_habit') and not value.get(
            'related_habit').is_pleasurable:
        raise ValidationError("В связанные привычки могут попадать только привычки с признаком приятной привычки.")


def validate_pleasurable_habit(value):
    if value.get('is_pleasurable') and (value.get('reward') or value.get('related_habit')):
        raise ValidationError("У приятной привычки не может быть вознаграждения или связанной привычки.")
