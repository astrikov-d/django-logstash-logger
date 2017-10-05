# coding: utf-8
import logging

from .formatters import LogstashFormatter


class LogstashHandler(logging.FileHandler):
    """
    Writes message to logstash log file.
    """
    app_label = 'Django Application'

    def __init__(self, *args, **kwargs):
        app_label = kwargs.pop('app_label', self.app_label)
        super(LogstashHandler, self).__init__(*args, **kwargs)
        self.formatter = LogstashFormatter(app_label=app_label)
