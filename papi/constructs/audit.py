from .construct import Construct


class Audit(Construct):
    """
    Class for accessing a workspace audit log
    """

    def all(self, start_time=None, end_time=None, resource_id=None, resource_type=None):
        """
        List audit trail events

        :param datetime.datetime,optional start_time: Filter response to events that happened after this time
        :param datetime.datetime,optional end_time: Filter response to events that happened before this time, defaults to the current time.
        :param str resource_id: Filter response to events that affect a specific resource
        :param str resource_type: Filter response to events that affect a specific type
        :returns: List of audit trail events
        :rtype: papi.common.common.Object
        """
        # https://api.segmentapis.com/docs/admin/audit-trail/#list-audit-events
        params = {}
        if start_time:
            params['startTime'] = start_time.isoformat()
        if end_time:
            params['endTime'] = end_time.isoformat()
        if resource_id:
            params['resourceId'] = resource_id
        if resource_type:
            params['resourceType'] = resource_type
        return self._segment.iterator('/audit-trails', params).events
