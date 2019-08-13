# coding: utf-8
import logging

from .formatters import LogstashFormatter


class LogstashHandler(logging.FileHandler):
    """
    Writes message to logstash log file.
    """
    app_label = 'Django Application'
    log_format = 'plain'
    ensure_ascii = False

    def __init__(self, *args, **kwargs):
        app_label = kwargs.pop('app_label', self.app_label)
        log_format = kwargs.pop('log_format', self.log_format)
        ensure_ascii = kwargs.pop('ensure_ascii', self.ensure_ascii)
        super(LogstashHandler, self).__init__(*args, **kwargs)
        self.formatter = LogstashFormatter(app_label=app_label, log_format=log_format, ensure_ascii=ensure_ascii)
