"""This module is designed for launching program."""
# pylint: skip-file
from work_with_bot.init_for_bot import scheduler, dp
from work_with_bot.start_bot import parse_tasks
from aiogram import executor


def main():
    scheduler.add_job(parse_tasks, trigger="cron", hour="0")
    scheduler.start()
    executor.start_polling(dp, skip_updates=True)


if __name__ == "__main__":
    main()
