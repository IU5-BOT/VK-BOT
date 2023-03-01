# Документация библиотеки vk_api: https://github.com/python273/vk_api
# Официальная документация VK API по разделу сообщений: https://vk.com/dev/messages
# Получить токен: https://vkhost.github.io/

import vk_api
from vk_api.utils import get_random_id  # снижение количества повторных отправок сообщения
# from dotenv import load_dotenv
import os


class Bot:
    """
    Базовый класс бота ВКонтакте
    """

    # текущая сессия ВКонтакте
    vk_session = None

    # доступ к API ВКонтакте
    vk_api_access = None

    # пометка авторизованности
    authorized = False

    # id пользователя ВКонтакте (например, 1234567890) в виде строки
    # можно использовать, если диалог будет вестись только с конкретным человеком
    default_user_id = None

    def __init__(self):
        """
        Инициализация бота при помощи получения доступа к API ВКонтакте
        """
        # load_dotenv()

        # авторизация
        self.vk_api_access = self.do_auth()

        if self.vk_api_access is not None:
            self.authorized = True

        self.default_user_id = os.getenv("USER_ID")

    def do_auth(self):
        """
        Авторизация за пользователя (не за группу или приложение)
        Использует переменную, хранящуюся в файле настроек окружения .env в виде строки ACCESS_TOKEN="1q2w3e4r5t6y7u8i9o..."
        :return: возможность работать с API
        """
        ACCESS_TOKEN = "vk1.a.c--F-gyV_BW1sQTjHI_HLLvneq3qlVSJW4TOCcx9OkoCaPWkbox-sz6iJUmHhAtYuLOeeqmBpusUEG7F3iGae-sSOGqKdPQd_ucv25rgA_VxjbbNI6XAZBg8pN-6XaZSo7mIj-ttiR9tyiMJcx5JX49D9Fymr7uNe3ppqS_2c1cQgeeH1QooscAW2boN8vF7Fqm2O_5W7sViVlGBMZeJPg"
        user_id = "248055283"
        token = ACCESS_TOKEN
        try:
            self.vk_session = vk_api.VkApi(token=token)
            return self.vk_session.get_api()
        except Exception as error:
            print(error)
            return None

    def send_message(self, receiver_user_id: str = '202056822', message_text: str = "Сообщение боту от вк бота."):
        """
        Отправка сообщения от лица авторизованного пользователя
        :param receiver_user_id: уникальный идентификатор получателя сообщения
        :param message_text: текст отправляемого сообщения
        """
        if not self.authorized:
            print("Unauthorized. Check if ACCESS_TOKEN is valid")
            return

        try:
            self.vk_api_access.messages.send(user_id=receiver_user_id, message=message_text, random_id=get_random_id())
            # print(f"Сообщение отправлено для ID {receiver_user_id} с текстом: {message_text}")
        except Exception as error:
            print(error)
