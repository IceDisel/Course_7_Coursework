from datetime import datetime, timedelta

import pytz
from celery import shared_task

from django.utils.timezone import localtime
from config import settings
from habit_tracker.models import Habit
from habit_tracker.services import TelegramBot

tg_bot = TelegramBot()


@shared_task
def send_telegram_notification():
    time_zone = settings.TIME_ZONE
    current_time = datetime.now(pytz.timezone(time_zone))
    useful_habits_list = Habit.objects.filter(is_pleasurable=False)

    for habit in useful_habits_list:
        local_date = localtime(habit.date)
        formatted_date = local_date.strftime('%Y-%m-%d %H:%M')
        message_main = (
            f'{habit.user.first_name}, вам необходимо выполнить привычку - {habit.action} в {formatted_date}.'
            f'\nЕё нужно выполнить за {habit.time_required} в {habit.place}.\n')

        if habit.date <= current_time:
            if habit.frequency == 'day':
                habit.date += timedelta(days=1)
            elif habit.frequency == 'week':
                habit.date += timedelta(days=7)
            else:
                continue

            formatted_next_date = habit.date.strftime('%Y-%m-%d %H:%M')

            if habit.reward or habit.related_habit:
                text_reward = habit.reward if habit.reward else habit.related_habit
                message_extended = (f'\nПосле вы получите вознаграждение - {text_reward}.'
                                    f'\nДалее ваша привычка должна быть выполнена до {formatted_next_date}.')
            else:
                message_extended = f'\nДалее ваша привычка должна быть выполнена до {formatted_next_date}.'

            message = message_main + message_extended
            try:
                tg_bot.send_message(chat_id=habit.user.telegram_chat_id, text=message)
                habit.save()
            except Exception as e:
                print(f'Ошибка при отправке сообщения: {e}')
