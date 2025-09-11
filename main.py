import asyncio

from config import TelegramConfig

from module import routers

from tools.logger import LoggerTools

BOT = TelegramConfig.BOT
DISPATCHER = TelegramConfig.DISPATCHER

logger = LoggerTools.get_logger(__name__, info=True, error=True, critical=True)


async def main():
    DISPATCHER.include_routers(*routers)

    print("START BOT")

    try:
        await DISPATCHER.start_polling(BOT, polling_timeout=30)
    except (KeyboardInterrupt, SystemExit):
        print(f"ASYNCIO PROBLEM")

        await asyncio.sleep(1)

    await BOT.session.close()

    print("SESSION CLOSE")


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info(msg="PROGRAM INTERRUPTED")
    except SystemError:
        logger.critical(msg="EXTREMAL ERROR")
