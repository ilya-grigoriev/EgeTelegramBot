from bot_for_tg.init_for_bot import scheduler, dp
from bot_for_tg.start_bot import parse_tasks
from aiogram import executor


def main():
    scheduler.add_job(parse_tasks, trigger='cron', hour='0')
    scheduler.start()
    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    main()
