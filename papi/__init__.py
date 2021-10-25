from .objects.Segment import Segment  # noqa: E402, F401
from .common import enum as segment_enum  # noqa: E402, F401
from .common import types as segment_types  # noqa: E402, F401
from .common import bunch as segment_bunch  # noqa: E402, F401
from .settings import settings as segment_settings  # noqa: E402, F401
from .errors import errors as segment_errors  # noqa: E402, F401
from .lib import Logger  # noqa: E402, F401

Logger.instance()
