import asyncio

from config import TelegramConfig

from tools.logger import LoggerTools

BOT = TelegramConfig.BOT
DISPATCHER = TelegramConfig.DISPATCHER

logger = LoggerTools.get_logger(__name__, info=True, error=True, critical=True)


async def main():
    ...


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info(msg="PROGRAM INTERRUPTED")
    except SystemError:
        logger.critical(msg="EXTREMAL ERROR")
