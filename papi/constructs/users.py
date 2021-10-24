from ..common import common
from .construct import Construct


class Users(Construct):
    """
    Class for managing Segment workspace users

    :ivar papi.constructs.users.Invites invites: Object implementing user invitation APIs
    """

    def __init__(self, segment):
        super().__init__(segment)
        self.invites = Invites(segment)

    def all(self):
        """
        List Users.

        :return: User iterator object
        :rtype: papi.lib.iterator.Iterator
        """
        return self._segment.iterator('/users', 'users')

    def get(self, user_id):
        """
        Get a User.

        :param str user_id: User identifier
        :return: User object
        :rtype: papi.common.common.Object
        """
        return self._segment.get(f'/users/{user_id}').user

    def groups(self, user_id):
        """
        List User Groups.

        :param str user_id: User identifier
        :return: Group iterator object
        :rtype: papi.lib.iterator.Iterator
        """
        return self._segment.iterator(f'/users/{user_id}/groups', 'groups')

    def delete(self, *user_ids):
        return self._segment.delete('/users', common.bunch(userIds=list(user_ids)))


class Invites(Construct):
    """
    Class for managing Segment workspace user invitations
    """

    def all(self):
        """
        List User Invitations.

        :return: Invitations iterator object
        :rtype: papi.lib.iterator.Iterator
        """
        return self._segment.iterator('/invites', 'invites').invites

    def delete(self, emails):
        """
        Delete User Invitations.

        :param list[str] emails: List of emails
        :return: Object indicating whether the deletion was successful or not
        :rtype: papi.common.common.Object
        """
        return self._segment.delete('/invites', common.bunch(emails=emails))
