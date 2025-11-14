import logging
import sys
from contextlib import contextmanager

class TeeLogger:
    def __init__(self, original_stream, logger, log_level):
        self.original_stream = original_stream
        self.logger = logger
        self.log_level = log_level

    def write(self, message):
        self.original_stream.write(message)
        if message and message.strip():
            self.logger.log(self.log_level, message.rstrip())

    def flush(self):
        self.original_stream.flush()
        for handler in self.logger.handlers:
            handler.flush()

@contextmanager
def logging_context(log_filename=None):
    logger = logging.getLogger("ltbox_logger")
    logger.setLevel(logging.INFO)
    
    handlers = []
    original_stdout = sys.stdout
    original_stderr = sys.stderr
    
    try:
        if log_filename:
            file_handler = logging.FileHandler(log_filename, encoding='utf-8')
            file_handler.setFormatter(logging.Formatter('%(message)s'))
            logger.addHandler(file_handler)
            handlers.append(file_handler)

            sys.stdout = TeeLogger(original_stdout, logger, logging.INFO)
            sys.stderr = TeeLogger(original_stderr, logger, logging.ERROR)
        
        yield logger

    finally:
        sys.stdout = original_stdout
        sys.stderr = original_stderr
        
        for handler in handlers:
            handler.close()
            logger.removeHandler(handler)