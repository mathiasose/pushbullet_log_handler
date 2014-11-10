import logging
import traceback
from pushbullet import PushBullet


class PushbulletLogHandler(logging.Handler):
    def __init__(self, api_key, stack_trace=False):
        logging.Handler.__init__(self)
        self.api_key = api_key
        self.stack_trace = stack_trace
        self.pb_session = PushBullet(self.api_key)

    def emit(self, record):
        message = '{}'.format(record.getMessage())

        if self.stack_trace and record.exc_info:
            message += '\n'
            message += '\n'.join(traceback.format_exception(*record.exc_info))

        _, _ = self.pb_session.push_note(message)
