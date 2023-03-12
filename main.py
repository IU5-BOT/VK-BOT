from longpoll_bot import LongPollBot
import datetime

if __name__ == '__main__':
    while True:
        print(f'Бот начал работать {datetime.datetime.now()}')
        try:
            long_poll_bot = LongPollBot()
            long_poll_bot.run_long_poll()
        except:
            print(f'Бот уснул в: {datetime.datetime.now()}')
