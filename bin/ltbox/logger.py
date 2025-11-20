import logging
import sys
from contextlib import contextmanager
from typing import Optional, TextIO

class TeeLogger:
    def __init__(self, original_stream: TextIO, logger: logging.Logger, log_level: int):
        self.original_stream = original_stream
        self.logger = logger
        self.log_level = log_level

    def write(self, message: str) -> None:
        self.original_stream.write(message)
        if message and message.strip():
            self.logger.log(self.log_level, message.rstrip())

    def flush(self) -> None:
        self.original_stream.flush()
        for handler in self.logger.handlers:
            handler.flush()

@contextmanager
def logging_context(log_filename: Optional[str] = None):
    logger = logging.getLogger("ltbox_logger")
    logger.setLevel(logging.INFO)
    
    handlers = []
    original_stdout = sys.stdout
    original_stderr = sys.stderr
    
    try:
        if log_filename:
            file_handler = logging.FileHandler(log_filename, encoding='utf-8')
            file_handler.setFormatter(logging.Formatter('%(asctime)s - %(message)s', datefmt='%H:%M:%S'))
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