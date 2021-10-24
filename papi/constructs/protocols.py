from ..common import common, enum
from .construct import Construct


class Protocols(Construct):
    """
    Class for managing Segment Protocols

    :ivar papi.constructs.protocols.TrackingPlans tracking_plans: Object implementing Tracking Plans APIs
    """

    def __init__(self, segment):
        super().__init__(segment)
        self.tracking_plans = TrackingPlans(segment)


class TrackingPlans(Construct):
    """
    Class for managing Segment Tracking Plans

    :ivar papi.constructs.protocols.Sources sources: Object for managing Tracking Plan Sources
    :ivar papi.constructs.protocols.Rules rules: Object for managing Tracking Plan Rules
    """

    def __init__(self, segment):
        super().__init__(segment)
        self.sources = Sources(segment)
        self.rules = Rules(segment)

    def add(self, name, tracking_plan_type, description=None):
        """
        Add a Tracking Plan.

        :param papi.common.enum.TrackingPlanType tracking_plan_type: Tracking Plan Type
        :param str,optional description: Tracking Plan description
        :return: Source object
        :rtype: papi.common.common.Object
        """
        enum.validate_enum_option(enum.TrackingPlanType, tracking_plan_type)
        tracking_plan = common.bunch(name=name, type=tracking_plan_type)
        if description:
            tracking_plan.description = description
        return self._segment.post('/tracking-plans', tracking_plan)

    def all(self, tracking_plan_type):
        """
        List Tracking Plans.

        :param papi.common.enum.TrackingPlanType tracking_plan_type: Tracking Plan Type
        :return: Tracking Plans iterator object
        :rtype: papi.lib.iterator.Iterator
        """
        enum.validate_enum_option(enum.TrackingPlanType, tracking_plan_type)
        return self._segment.iterator('/tracking-plans', 'trackingPlans', {'type': tracking_plan_type})

    def delete(self, tracking_plan_id):
        """
        Delete a Tracking Plan.

        :param str tracking_plan_id: Tracking Plan identifier
        :return: Object indicating whether the deletion was successful or not
        :rtype: papi.common.common.Object
        """
        return self._segment.delete(f'/tracking-plans/{tracking_plan_id}', {'trackingPlanId': tracking_plan_id})

    def get(self, tracking_plan_id):
        """
        Get a Tracking Plan.

        :param str tracking_plan_id: Tracking Plan identifier
        :return: Tracking Plan object
        :rtype: papi.common.common.Object
        """
        return self._segment.get(f'/tracking-plans/{tracking_plan_id}').trackingPlan

    def update(self, tracking_plan_id, name=None, description=None):
        """
        Update a Tracking Plan.

        :param str tracking_plan_id: Tracking Plan identifier
        :param str,optional name: Tracking Plan name
        :param str,optional description: Tracking Plan description
        :return: Status object indicating whether if the operation was successful
        :rtype: papi.common.common.Object
        """
        updates = common.bunch(trackingPlanId=tracking_plan_id)
        if name:
            updates.name = name
        if description:
            updates.description = description
        return self._segment.patch(f'/tracking-plans/{tracking_plan_id}', updates)


class Sources(Construct):
    """
    Class for managing Tracking Plan Sources
    """

    def add(self, tracking_plan_id, source_id):
        """
        Connect a Source to a Tracking Plan

        :param str tracking_plan_id: Tracking Plan identifier
        :param str source_id: Source identifier
        :return: Status object indicating whether if the operation was successful
        :rtype: papi.common.common.Object
        """
        source = common.bunch(trackingPlanId=tracking_plan_id, sourceId=source_id)
        return self._segment.post(f'/tracking-plans/{tracking_plan_id}/sources', source)

    def all(self, tracking_plan_id):
        """
        List Sources connected to a Tracking Plan.

        :param str tracking_plan_id: Tracking Plan identifier
        :return: Source iterator object
        :rtype: papi.lib.iterator.Iterator
        """
        return self._segment.iterator(f'/tracking-plans/{tracking_plan_id}/sources', 'sources')

    def remove(self, tracking_plan_id, source_id):
        """
        Disconnect a Source from a Tracking Plan

        :param str tracking_plan_id: Tracking Plan identifier
        :param str source_id: Source identifier
        :return: Status object indicating whether if the operation was successful
        :rtype: papi.common.common.Object
        """
        return self._segment.delete(f'/tracking-plans/{tracking_plan_id}/sources',
                                    common.bunch(trackingPlanId=tracking_plan_id, sourceId=source_id))


class Rules(Construct):
    """
    Class for managing Tracking Plan Rules
    """

    def all(self, tracking_plan_id):
        """
        List Tracking Plan Rules.

        :param str tracking_plan_id: Tracking Plan identifier
        :return: Rules iterator object
        :rtype: papi.lib.iterator.Iterator
        """
        return self._segment.iterator(f'/tracking-plans/{tracking_plan_id}/rules', 'rules')

    # https://api.segmentapis.com/docs/protocols/tracking-plans/rules/#remove-rules-from-tracking-plan
    def remove(self, tracking_plan_id, rules):
        pass

    # https://api.segmentapis.com/docs/protocols/tracking-plans/rules/#update-rules-in-tracking-plan
    def update(self):
        pass
