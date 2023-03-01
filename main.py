from longpoll_bot import LongPollBot
import subprocess

if __name__ == '__main__':
    while True:
        try:
            long_poll_bot = LongPollBot()
            long_poll_bot.run_long_poll()
        except:
            print('ЛОЛ')
