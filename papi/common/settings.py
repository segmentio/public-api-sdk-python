from . import common
from ..errors import errors


def create_settings(options):
    settings = common.Object()
    for setting_name, setting_value in options.items():
        if '-' in setting_name:
            new_setting_name = setting_name.replace('-', '_')
            setattr(settings, new_setting_name, setting_value)
            if not getattr(settings, '__rename', None):
                settings.__rename = {}   # pylint: disable=protected-access
            settings.__rename[new_setting_name] = setting_name   # pylint: disable=protected-access
        else:
            setattr(settings, setting_name, setting_value)
    return settings


def validate_settings(options, settings=None):
    settings = settings if settings else {}
    if options:
        for option in options:
            if option.required and settings.get(option.name, None) is None:
                required = [option.name for option in options if option.required]
                raise errors.InputError('No value for required field', field=option.name, required=required)
