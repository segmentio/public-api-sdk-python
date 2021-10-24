from ..common import common
from .construct import Construct


class Labels(Construct):

    def all(self):
        """
        List Labels.
        """
        return self._segment.get('/labels').labels

    def add(self, key, value, description=None):
        """
        Create a Label.

        :param str key: Label name (key)
        :param str value: Label value
        :param str,optional description: Label description
        :return: List of all labels
        :rtype: list[papi.common.common.Object]
        """
        label = common.bunch(key=key, value=value)
        if description:
            label.description = description
        return self._segment.post('/labels', common.bunch(label=label)).labels

    def delete(self, key, value):
        """
        Delete a Label.

        :param str key: Label name (key)
        :param str value: Label value
        :return: Status object indicating whether if the operation was successful
        :rtype: papi.common.common.Object
        """
        return self._segment.delete(f'/labels/{key}/{value}', {'key': key, 'value': value})
