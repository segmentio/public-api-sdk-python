from ..common import enum
from .construct import Construct


class Regulations(Construct):
    """
    Class for managing deletion and suppression requests
    """

    def all(self, regulation_status=None, regulation_types=None):
        """
        List Workspace Regulations.

        :param papi.common.enum.RegulationStatus,optional regulation_status: Regulation status
        :param list[papi.common.enum.RegulationType],optional regulation_types: List of regulation types
        :return: Regulation iterator object
        :rtype: papi.lib.iterator.Iterator
        """
        params = {}
        if regulation_status:
            enum.validate_enum_option(enum.RegulationStatus, regulation_status)
            params['status'] = regulation_status
        if regulation_types:
            for regulation_type in regulation_types:
                enum.validate_enum_option(enum.RegulationType, regulation_type)
            params['regulationTypes'] = ','.join(regulation_status)
        return self._segment.iterator('/regulations', 'regulations', params)

    def delete(self, regulation_id):
        """
        Deletes a Regulation.

        :param str regulation_id: Regulation identifier
        :return: Object indicating whether the deletion was successful or not
        :rtype: papi.common.common.Object
        """
        return self._segment.delete(f'/regulations/{regulation_id}', {'regulateId': regulation_id})

    def get(self, regulation_id):
        """
        Get a Regulation.

        :param str regulation_id: Regulation identifier
        :return: Regulation object
        :rtype: papi.common.common.Object
        """
        return self._segment.get(f'/regulations/{regulation_id}')

    def suppressions(self):
        """
        List Workspace Suppressions.

        :return: Suppression iterator object
        :rtype: papi.lib.iterator.Iterator
        """
        return self._segment.get('/suppressions').suppressed
