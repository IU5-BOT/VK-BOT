from simple_bot import Bot
from scheduled_bot import ScheduledBot
from longpoll_bot import LongPollBot
from nlu_longpoll_bot import NLULongPollBot

if __name__ == '__main__':
    # nlu_longpoll_bot = NLULongPollBot()
    # nlu_longpoll_bot.run_long_poll()
    # bot = Bot()
    # bot.send_message('202056822', 'Тестовое сообщение')
    long_poll_bot = LongPollBot()
    long_poll_bot.run_long_poll()
