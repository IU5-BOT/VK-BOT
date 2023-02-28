from simple_bot import Bot  # базовый класс бота из файла simple_bot
from vk_api.longpoll import VkLongPoll, VkEventType  # использование VkLongPoll и VkEventType
from units.functions import check_user_text
from DATA_WORD.important_persons import IMPORTANT_PERSONS
import re


class LongPollBot(Bot):
    """
    Бот, прослушивающий в бесконечном цикле входящие сообщения и способный отвечать на некоторые из них
    Бот отвечает на строго заданные сообщения
    """

    # длительное подключение
    long_poll = None

    def __init__(self):
        """
        Иинициализация бота
        """
        super().__init__()
        self.long_poll = VkLongPoll(self.vk_session)

    def run_long_poll(self):
        """
        Запуск бота
        """
        for event in self.long_poll.listen():

            # если пришло новое сообщение - происходит проверка текста сообщения
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
                user_id: str = event.user_id
                checking_res = check_user_text(event.text)
                pattern = re.compile(
                    r'(^(((н|h)+(е|e)+т*)|(n+o+)|(н|h(о|o)+у|y))*\s*,*\.*\s*((т+ы+)+|(y|у+o|о+u+)+|u+))[\.,]*\W*$')
                if pattern.match(event.text.strip().lower()) and user_id is not IMPORTANT_PERSONS:
                    self.send_message(receiver_user_id=user_id, message_text='Нет, ты')

                elif checking_res is not None:
                    # ответ отправляется в личные сообщения пользователя (если сообщение из личного чата)
                    if event.from_user and user_id is not IMPORTANT_PERSONS:
                        self.send_message(receiver_user_id=user_id, message_text=checking_res)

                    # ответ отпрвляется в беседу (если сообщение было получено в общем чате)
                    # elif event.from_chat:
                    #     self.send_message(receiver_user_id=event.chat_id, message_text=checking_res)
