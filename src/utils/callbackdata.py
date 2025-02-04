from attr import dataclass
from aiogram.filters.callback_data import CallbackData
from core.database import Queue


@dataclass
class QueueCallback(CallbackData, prefix='queue_item'):
    # queue: Queue
    queue: list = []
