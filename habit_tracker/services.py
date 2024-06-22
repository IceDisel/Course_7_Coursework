import requests

from config import settings


class TelegramBot:
    URL = 'https://api.telegram.org/bot'
    TOKEN = settings.TELEGRAM_BOT_TOKEN

    def send_message(self, chat_id, text):
        requests.post(
            url=f'{self.URL}{self.TOKEN}/sendMessage',
            data={
                'chat_id': chat_id,
                'text': text
            }
        )
