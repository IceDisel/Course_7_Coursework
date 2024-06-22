from celery import shared_task
from django.core.mail import send_mail

from config import settings


@shared_task
def send_mail_notification(user_email):
    subject = 'Уведомление о регистрации'
    message = 'Вы успешно зарегистрировались на сайте'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user_email]
    send_mail(subject, message, from_email, recipient_list)
