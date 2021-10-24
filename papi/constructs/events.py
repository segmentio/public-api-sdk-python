from .construct import Construct


class Events(Construct):
    """
    Class enumerating the workspace event volumes over time in minute increments.
    """

    # https://api.segmentapis.com/docs/connections/events/#get-events-volume-from-workspace
    def events(self, granularity, start_time, end_time,
               group_by=None, source_id=None, event_name=None, event_type=None, app_version=None):
        print(self, granularity, start_time, end_time, group_by, source_id, event_name, event_type, app_version)
        # return self._segment.get('/events/volume')
