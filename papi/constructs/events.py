import logging
from .construct import Construct
from ..common import enum


class Events(Construct):
    """
    Class enumerating the workspace event volumes over time in minute increments.
    """

    def events(self, granularity, start_time, end_time,
               group_by=None, source_ids=None, event_names=None, event_types=None, app_versions=None):
        """
        Enumerate workspace event volumes over time in minute increments.

        :param papi.common.enum.EventGranularity granularity: Size of each bucket in the window requested
        :param datetime.datetime start_time: Beginning of the requested timeframe, inclusive
        :param datetime.datetime start_time: End of the requested timeframe, noninclusive.
         Segment recommend's lagging queries 1 minute behind clock time to reduce the risk for latency to impact the counts
        :param list[papi.common.enum.EventGroupBy],optional group_by: List of dimensions to group the result by
        :param list[str],optional source_id: Filter results to a list of sources
        :param list[str],optional event_names: Filter results to a list of event names
        :param list[str],optional event_types: Filter results to a list of event types
        :param list[str],optional app_versions: Filter results to a list of app versions
        :returns:
        :rtype:
        """
        enum.validate_enum_option(enum.EventGranularity, granularity)
        params = {
            'granularity': granularity,
            'startTime': start_time.isoformat(),
            'endTime': end_time.isoformat()
        }
        if group_by:
            for criteria in group_by:
                enum.validate_enum_option(enum.EventGroupBy, criteria)
            params['groupBy'] = group_by
        if source_ids:
            params['sourceId'] = source_ids
        if event_names:
            params['eventName'] = event_names
        if event_types:
            params['eventType'] = event_types
        if app_versions:
            params['appVersion'] = app_versions
        logging.getLogger().debug('Enumerating event volumes. %s', params)
        response = self._segment.get('/events/volume', params)
        return response.result
