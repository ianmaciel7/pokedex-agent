import functools
import logging

logger = logging.getLogger(__name__)

def safe_fetch(func):
    """Decorator to catch exceptions during PokéAPI tool calls and return clean error messages."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as exc:
            logger.exception(
                "Error executing tool %s with args=%s kwargs=%s",
                func.__name__,
                args,
                kwargs,
            )
            return f"Error executing tool '{func.__name__}': {exc}"
    return wrapper
