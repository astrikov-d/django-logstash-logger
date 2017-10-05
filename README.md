# django-logstash-logger
Simple logstash-compatible logger for Django-based projects

## Installation

At the moment, this package is not distributing via PyPi, so you can install it directly from GitHub:

```
pip install git+https://github.com/astrikov-d/django-logstash-logger
```

## Setup

Setup logging handlers in your `settings.py` inside your Django application like this:

```
LOGGING = {
    ...
    'handlers': {
        'app_name_logstash_log_handler': {
            'level': 'DEBUG',
            'class': 'django_logstash_logger.handlers.LogstashHandler',
            'filename': '/whatever/log/path.txt',
            'app_label': 'app_name'
        }
    },
    'loggers': {
        'app_name_logger': {
            'level': 'DEBUG',
            'handlers': ['app_name_logstash_log_handler'],
            'propagate': False
        }
    },
    ...
}
```

## Usage

Use logger inside your app:

```
from logging import getLogger

logger = getLogger('app_name_logger')

logger.debug('Debug message')
logger.info('Info message')
logger.error('Error message')
logger.warning('Warning message')
```