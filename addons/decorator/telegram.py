import asyncio

import functools

from aiogram.exceptions import TelegramAPIError, TelegramForbiddenError

from tools.logger import LoggerTools

logger = LoggerTools.get_logger(__name__, error=True)


class TelegramDecorator:
    @staticmethod
    def log_call(prefix):
        def decorator(func):
            @functools.wraps(func)
            async def async_wrapper(*args, **kwargs):
                try:
                    result = await func(*args, **kwargs)

                    return result
                except TelegramForbiddenError:
                    logger.error(msg=f"CAll: {prefix} Telegram Forbidden Error, data: {args}, {kwargs}", exc_info=True)
                except TelegramAPIError as e:
                    logger.error(msg=f"CAll: {prefix} Telegram API Error: {e}, data: {args}, {kwargs}", exc_info=True)
                except Exception as e:
                    logger.error(msg=f"CAll: {prefix} Telegram Exception: {e}, data: {args}, {kwargs}")

                return None

            @functools.wraps(func)
            def sync_wrapper(*args, **kwargs):
                try:
                    result = func(*args, **kwargs)

                    return result
                except TelegramForbiddenError:
                    logger.error(msg=f"CAll: {prefix} Telegram Forbidden Error, data: {args}, {kwargs}", exc_info=True)
                except TelegramAPIError as e:
                    logger.error(msg=f"CAll: {prefix} Telegram API Error: {e}, data: {args}, {kwargs}", exc_info=True)
                except Exception as e:
                    logger.error(msg=f"CAll: {prefix} Telegram Exception: {e}, data: {args}, {kwargs}")

                return None

            return async_wrapper if asyncio.iscoroutinefunction(func) else sync_wrapper

        return decorator

    @staticmethod
    def log_del(prefix):
        def decorator(func):
            @functools.wraps(func)
            async def async_wrapper(*args, **kwargs):
                try:
                    await func(*args, **kwargs)
                except TelegramAPIError as e:
                    logger.error(msg=f"CAll: {prefix} Telegram API Error: {e}, data: {args}, {kwargs}", exc_info=True)
                except Exception as e:
                    logger.error(msg=f"CAll: {prefix} Telegram Exception: {e}, data: {args}, {kwargs}")

            @functools.wraps(func)
            def sync_wrapper(*args, **kwargs):
                try:
                    func(*args, **kwargs)
                except TelegramAPIError as e:
                    logger.error(msg=f"CAll: {prefix} Telegram API Error: {e}, data: {args}, {kwargs}", exc_info=True)
                except Exception as e:
                    logger.error(msg=f"CAll: {prefix} Telegram Exception: {e}, data: {args}, {kwargs}")

            return async_wrapper if asyncio.iscoroutinefunction(func) else sync_wrapper

        return decorator
    