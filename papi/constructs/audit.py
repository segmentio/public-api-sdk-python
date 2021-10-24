from .construct import Construct


class Audit(Construct):
    """
    Class for accessing a workspace audit log
    """

    # use custom get function with additional headers
    # https://api.segmentapis.com/docs/admin/audit-trail/#list-audit-events
    def all(self, start_time, end_time, resource_id, resource_type):
        print(self, start_time, end_time, resource_id, resource_type)
        # return self._segment.iterator('/audit-events', 'events')
