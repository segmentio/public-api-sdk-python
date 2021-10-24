from .construct import Construct


class Roles(Construct):
    """
    Class implementing Segment Roles APIs
    """

    def all(self):
        """
        List Roles.

        :return: Roles iterator object
        :rtype: papi.lib.iterator.Iterator
        """
        return self._segment.iterator('/roles', 'roles')
