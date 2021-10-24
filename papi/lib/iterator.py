from ..lib import utils


class Iterator:  # pylint: disable=too-many-instance-attributes

    def __init__(self, function, return_attribute, parameters, pagination_count, pagination_cursor):
        self._function = function
        self._return_attribute = return_attribute
        self._parameters = parameters if parameters else {}
        self._pagination_count = pagination_count
        self._pagination_cursor = pagination_cursor
        self._objects = []
        self._total_entries = 0
        self._more = True

    def __iter__(self):
        return self

    def __next__(self):

        if not self._objects:

            if self._more:

                response = self._function(utils.merge(self._parameters, {
                    'pagination.count': self._pagination_count,
                    'pagination.cursor': self._pagination_cursor
                }))

                self._objects = getattr(response, self._return_attribute)

                if not self._objects:  # no results
                    raise StopIteration

                self._total_entries = self._total_entries + len(self._objects)
                self._pagination_cursor = response.pagination.next

                if hasattr(response.pagination, 'totalEntries') and not self._total_entries < response.pagination.totalEntries:

                    if not self._objects:
                        raise StopIteration

                    self._more = False

            else:
                raise StopIteration

        return self._objects.pop(0)
