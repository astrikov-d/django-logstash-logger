# coding: utf-8]
import pytz

import getpass
import logging

from datetime import datetime

from django.conf import settings

from ._compat import text_type


class LogstashFormatter(logging.Formatter):
    template = '''[%(level)s] [%(ts)s]: app: '%(app_label)s' username: '%(username)s' args: '%(args)s' exc: '%(exc_info)s' msg: '%(msg)s' '''
    app_label = 'django_application'
    timezone = getattr(settings, 'TIME_ZONE', 'UTC')

    def __init__(self, *args, **kwargs):
        self.app_label = kwargs.pop('app_label', self.app_label)
        super(LogstashFormatter, self).__init__(*args, **kwargs)

    def format(self, record):
        if record.args:
            msg = record.msg % record.args
        else:
            msg = record.msg

        timezone = pytz.timezone(self.timezone)

        context = {
            'app_label': self.app_label,
            'level': record.levelname,
            'username': getpass.getuser(),
            'msg': msg,
            'args': tuple(text_type(arg) for arg in record.args),
            'ts': timezone.localize(datetime.now()).strftime('%d/%b/%Y:%H:%M:%S %z'),
            'exc_info': ''
        }

        if hasattr(record, 'exc_info') and record.exc_info:
            context['exc_info'] = record.exc_info

        return self.template % context
