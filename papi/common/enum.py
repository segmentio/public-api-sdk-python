from ..errors import errors


class APIVersion:
    """
    Public API Version

    :ivar str ALPHA: Alpha
    :ivar str BETA: Beta
    :ivar str STABLE: Stable
    """

    ALPHA = 'alpha'
    BETA = 'beta'
    STABLE = 'stable'


class FunctionType:
    """
    Function Type

    :ivar str SOURCE: SOURCE
    :ivar str DESTINATION: DESTINATION
    """

    SOURCE = 'SOURCE'
    DESTINATION = 'DESTINATION'


class FunctionSettingType:
    """
    Function Setting Type

    :ivar str ARRAY: Array
    :ivar str BOOLEAN: Boolean
    :ivar str STRING: String
    :ivar str TEXT_MAP: Text-map
    """

    ARRAY = 'array'
    BOOLEAN = 'boolean'
    STRING = 'string'
    TEXT_MAP = 'text-map'


class TrackingPlanType:
    """
    Tracking Plan Type

    :ivar str LIVE: Live
    :ivar str PROPERTY_LIBRARY: Property library
    :ivar str RULE_LIBRARY: Rule library
    :ivar str TEMPLATE: Template
    """

    LIVE = 'LIVE'
    PROPERTY_LIBRARY = 'PROPERTY_LIBRARY'
    RULE_LIBRARY = 'RULE_LIBRARY'
    TEMPLATE = 'TEMPLATE'


class TrackingPlanRuleType:
    """
    Tracking Plan Rule Type

    :ivar str COMMON: Common
    :ivar str GROUP: Group
    :ivar str IDENTIFY: Identify
    :ivar str PAGE: Page
    :ivar str SCREEN: Screen
    :ivar str TRACK: Track
    """
    COMMON = 'COMMON'
    GROUP = 'GROUP'
    IDENTIFY = 'IDENTIFY'
    PAGE = 'PAGE'
    SCREEN = 'SCREEN'
    TRACK = 'TRACK'


class RegulationType:
    """
    Regulation Type

    :ivar str SUPPRESS_ONLY: Only suppress
    :ivar str DELETE_ONLY: Only delete
    :ivar str SUPPRESS_WITH_DELETE: Suppress and delete
    :ivar str UNSUPPRESS: Unsuppress
    :ivar str BULK_DELETE_ONLY: Only bulk delete
    :ivar str DELETE_INTERNAL: Internal delete
    """

    SUPPRESS_ONLY = 'suppressOnly'
    DELETE_ONLY = 'deleteOnly'
    SUPPRESS_WITH_DELETE = 'suppressWithDelete'
    UNSUPPRESS = 'unsuppress'
    BULK_DELETE_ONLY = 'bulkDeleteOnly'
    DELETE_INTERNAL = 'deleteInternal'


class RegulationStatus:
    """
    Regulation Status

    :ivar str FAILED: Failed
    :ivar str FINISHED: Finished
    :ivar str INITIALIZED: Initialized
    :ivar str INVALID: Invalid
    :ivar str NOT_SUPPORTED: Not supported
    :ivar str PARTIAL_SUCCESS: Partial success
    :ivar str RUNNING: Running
    """

    FAILED = 'failed'
    FINISHED = 'finished'
    INITIALIZED = 'initialized'
    INVALID = 'invalid'
    NOT_SUPPORTED = 'notSupported'
    PARTIAL_SUCCESS = 'partialSuccess'
    RUNNING = 'running'


class Region:
    """
    Segment Region

    :ivar str euw1: Dublin, Ireland (eu-west-1)
    :ivar str usw2: Oregon (us-west-2)
    """
    euw1 = 'eu1'
    usw2 = ''


class EventGranularity:
    """
    Event Granularity

    :ivar str DAY: Day
    :ivar str HOUR: Hour
    :ivar str MINUTE: Minute
    """
    DAY = 'day'
    HOUR = 'hour'
    MINUTE = 'minute'


class EventGroupBy:
    """
    Event Group By

    :ivar str DAY: Day
    :ivar str HOUR: Hour
    :ivar str MINUTE: Minute
    """
    EVENT_NAME = 'eventName'
    EVENT_TYPE = 'eventType'
    SOURCE = 'source'


def validate_enum_option(enum, option):
    options = [v for k, v in enum.__dict__.items() if not k.startswith('_')]
    if option not in options:
        raise errors.InputError('Invalid option.', option=option, options=options)
