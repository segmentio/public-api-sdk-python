from collections import namedtuple
from . import common


Label = namedtuple('Label', ('key', 'value'))
Label.__doc__ = 'Tuple representing a label'
Label.key.__doc__ = 'The label key'
Label.value.__doc__ = 'The label value'


class Connection(common.Object):
    """
    Class representing a Segment Connection
    """

    def __init__(self, source, destination, is_warehouse):
        self._source = source
        self._destination = destination
        self._is_warehouse = is_warehouse

    @property
    def source(self):
        """
        Get Source

        :returns: Connection Source
        :rtype: papi.common.common.Object
        """
        return self._source

    @property
    def destination(self):
        """
        Get Destination

        :returns: Connection Destination
        :rtype: papi.common.common.Object
        """
        return self._destination

    @property
    def is_warehouse(self):
        """
        Check if the destination is a warehouse

        :returns: ``True`` if the destination is a warehouse, ``False`` otherwise.
        :rtype: bool
        """
        return self._is_warehouse

    def __str__(self):
        return str(
            common.bunch(
                source_id=self._source.id,
                destination_id=self._destination.id,
                is_warehouse=self._is_warehouse
            )
        )


class FunctionSettingsBuilder:
    """
    Builder class for Segment Function settings
    """

    def __init__(self):
        self._name = None
        self._label = None
        self._description = None
        self._type = None
        self._required = False
        self._sensitive = False

    def name(self, name):
        """
        Set name.

        :param str name: Setting name
        :return: Self, the builder object
        :rtype: papi.common.types.FunctionSettingsBuilder
        """
        self._name = name
        return self

    def label(self, label):
        """
        Set label.

        :param str label: Setting label
        :return: Self, the builder object
        :rtype: papi.common.types.FunctionSettingsBuilder
        """
        self._label = label
        return self

    def description(self, description):
        """
        Set description.

        :param str description: Setting description
        :return: Self, the builder object
        :rtype: papi.common.types.FunctionSettingsBuilder
        """
        self._description = description
        return self

    def type(self, function_type):
        """
        Set function setting type.

        :param str function_type: Setting type
        :return: Self, the builder object
        :rtype: papi.common.types.FunctionSettingsBuilder
        """
        self._type = function_type
        return self

    def required(self, required=False):
        """
        Set as required.

        :param bool required: Set as required, defaults to ``False``
        :return: Self, the builder object
        :rtype: papi.common.types.FunctionSettingsBuilder
        """
        self._required = required
        return self

    def sensitive(self, sensitive=False):
        """
        Set as sensitive.

        :param bool required: Set as sensitive, defaults to ``False``
        :return: Self, the builder object
        :rtype: papi.common.types.FunctionSettingsBuilder
        """
        self._sensitive = sensitive
        return self

    def to_server_object(self):
        """
        Convert to a server object.

        :return: Function settings object
        :rtype: papi.common.common.Object
        """
        return common.bunch(
            name=self._name,
            label=self._label,
            type=self._type,
            required=self._required,
            sensitive=self._sensitive
        )
