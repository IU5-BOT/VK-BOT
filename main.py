from longpoll_bot import LongPollBot

if __name__ == '__main__':
    try:
        long_poll_bot = LongPollBot()
        long_poll_bot.run_long_poll()
    except:
        print('ЛОЛ')
