import os
import logging

logger_config = dict(
    disabled=False,
    level=logging.INFO,
    log_format='%(asctime)s,%(msecs)3d %(levelname)7s [%(filename)s:%(lineno)d] [%(funcName)s] - %(message)s',
    date_format='%Y-%m-%d %H:%M:%S',
    log_file=os.environ.get('SEGMENT_PAPI_LOG_FILE')
)

pagination = dict(
    page_size=20
)
