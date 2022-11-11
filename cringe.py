import vk_api
from vk_api.utils import get_random_id  # снижение количества повторных отправок сообщения
from vk_api.longpoll import VkLongPoll, VkEventType  # использование VkLongPoll и VkEventType

WORDS = {
    "pig": {
        "свинка": "А может это ты свинка? Или попутал чи шо? На будущее - Dmirtiy Kirillovich или просто да: Boss",
        "свин": "Представился? Или чатиком ошибся? На будущее - Dmirtiy Kirillovich или просто да: Boss",
        "боров": "Воу воу, сыночек, ты явно попутал чатики. Ты щас тут не с рандом челиком базаришь, так что субординацию соблюдаем, щенок. На будущее - Dmirtiy Kirillovich или просто да: Boss",
        "свинья": "Воу воу, сыночек, ты явно попутал чатики. Ты щас тут не с рандом челиком базаришь, так что субординацию соблюдаем, щенок. На будущее - Dmirtiy Kirillovich или просто да: Boss"
    },
    "salutation": {
        "привет": "Привет.",
        "прив": "Прив.",
        "здарова": "Дарова",
        "здравствуй": "Ну здр",
        "здаров": "Угу, приветствую",
        "hi": "Hi. Вы из англии?",
        "хай": "Хай",
        "hello": "Bonjour",
        "салют": "Где? А меня почему не позвал?"
    },
    "you": {
        "ты": "ты"
    },
    "Dima": {
        "дим": "Ты явно что-то тут попутал, сынок. Димкать дома будешь, тут ты пишешь Дмитрию Кирилловичу.",
        "димааа": "Ты явно что-то тут попутал, сынок. Димкать дома будешь, тут ты пишешь Дмитрию Кирилловичу.",
        "димооон": "Ты явно что-то тут попутал, сынок. Димонкать дома будешь, тут ты пишешь Дмитрию Кирилловичу.",
        "димон": "Ты явно что-то тут попутал, сынок. Димонкать дома будешь, тут ты пишешь Дмитрию Кирилловичу.",
        "дима": "Ты явно что-то тут попутал, сынок. Димкать дома будешь, тут ты пишешь Дмитрию Кирилловичу.",
        "пермяк": "Ты явно что-то тут попутал, сынок. Пермякать дома будешь, тут ты пишешь Дмитрию Кирилловичу.",
        "дииим": "Ты явно что-то тут попутал, сынок. Димкать дома будешь, тут ты пишешь Дмитрию Кирилловичу.",
        "димасик": "Ты явно что-то тут попутал, сынок. Димаськать дома будешь, тут ты пишешь Дмитрию Кирилловичу."

    }
}


class Bot:
    vk_session = None
    vk_api_access = None
    authorized = False
    default_user_id = None

    def __init__(self):
        self.vk_api_access = self.do_auth()
        if self.vk_api_access is not None:
            self.authorized = True
        self.default_user_id = "248055283"

    def do_auth(self):
        ACCESS_TOKEN = "vk1.a.SurCHnOmMsXFjCbtgyHlq9hzH2E3rELd1oNrIlQFHUxwsOsGrcC_auoqCLjU28WbjLhqpliPSJWY5JehOclQx7OhuMJr5l4-vH3cmEBjfLpe-KL9BMFDKXyv6ordwKXX5TRkRZOJLhN3o9FKfUKpVf-MLfzxYRO8-w9QGcZOjfE51x50_dYqmRJqtKa4mXRo1T-cMKyZnkl1EK3fQefY1g"
        token = ACCESS_TOKEN
        try:
            self.vk_session = vk_api.VkApi(token=token)
            return self.vk_session.get_api()
        except Exception as error:
            print(error)
            return None

    def send_message(self, receiver_user_id: str = '202056822', message_text: str = "Сообщение боту от вк бота."):
        if not self.authorized:
            print("Unauthorized. Check if ACCESS_TOKEN is valid")
            return

        if receiver_user_id == '202056822':
            receiver_user_id = self.default_user_id

        try:
            self.vk_api_access.messages.send(user_id=receiver_user_id, message=message_text, random_id=get_random_id())
            print(f"Сообщение отправлено для ID {receiver_user_id} с текстом: {message_text}")
        except Exception as error:
            print(error)


class LongPollBot(Bot):
    long_poll = None

    def __init__(self):
        super().__init__()
        self.long_poll = VkLongPoll(self.vk_session)

    def run_long_poll(self):
        """
        Запуск бота
        """
        for event in self.long_poll.listen():

            # если пришло новое сообщение - происходит проверка текста сообщения
            if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:

                # TODO: Улучшить через regular'ы.
                if event.text in ['ты', 'нет ты', 'нет, ты']:
                    self.send_message(receiver_user_id=event.user_id, message_text='Нет, ты')

                checking_res: str | None = check_user_text(event.text)
                if checking_res is not None:

                    # ответ отправляется в личные сообщения пользователя (если сообщение из личного чата)
                    if event.from_user:
                        self.send_message(receiver_user_id=event.user_id, message_text=checking_res)

                    # ответ отпрвляется в беседу (если сообщение было получено в общем чате)
                    # elif event.from_chat:
                    #     self.send_message(receiver_user_id=event.chat_id, message_text=checking_res)


def check_user_text(text: str, filename: str = 'DATA_WORD/data.json') -> str | None:
    import re
    # Делим текст по словам. И проверяем каждое.
    for el in re.split(r'(\W+)', text):
        word = el.lower()
        res = [WORDS[key][word] for key, el in WORDS.items() if word in list(el.keys())]
        if len(res) != 0:
            return str(*res)
    return None


if __name__ == '__main__':
    # nlu_longpoll_bot = NLULongPollBot()
    # nlu_longpoll_bot.run_long_poll()
    # bot = Bot()
    # bot.send_message('202056822', 'Тестовое сообщение')
    long_poll_bot = LongPollBot()
    long_poll_bot.run_long_poll()
