from ..common import common
from .construct import Construct


class Groups(Construct):
    """
    Class for managing Segment workspace user groups

    :ivar papi.constructs.groups.Users settings: Object implementing group user APIs
    :ivar papi.constructs.groups.Permissions labels: Object implementing group permission APIs
    """

    def __init__(self, segment):
        super().__init__(segment)
        self.users = Users(segment)
        self.permissions = Permissions(segment)

    def add(self, name):
        """
        Create a Group.

        :param str name: Group name
        :return: Group object including the group id, name and member count
        :rtype: papi.common.common.Object
        """
        return self._segment.post('/groups', common.bunch(name=name)).userGroup

    def all(self):
        """
        List Groups.

        :return: Group iterator object
        :rtype: papi.lib.iterator.Iterator
        """
        return self._segment.iterator('/groups', 'userGroups')

    def get(self, group_id):
        """
        Get a Group.

        :param str group_id: Group identifier
        :return: Group object
        :rtype: papi.common.common.Object
        """
        return self._segment.get(f'/groups/{group_id}').userGroup

    def delete(self, group_id):
        """
        Delete a Group.

        :param str group_id: Group identifier
        :return: Object indicating whether the deletion was successful or not
        :rtype: papi.common.common.Object
        """
        return self._segment.delete(f'/groups/{group_id}', {'userGroupId': group_id})

    def rename(self, group_id, name):
        """
        Rename a Group.

        :param str group_id: Group identifier
        :param str name: Group name
        :return: Group object
        :rtype: papi.common.common.Object
        """
        return self._segment.patch(f'/groups/{group_id}', common.bunch(userGroupId=group_id, name=name))


class Users(Construct):
    """
    Class for managing Segment workspace users in groups
    """

    def invites(self, group_id):
        """
        List Invites.

        :param str group_id: Group identifier
        :return: List of emails
        :rtype: list[str]
        """
        return self._segment.iterator(f'/groups/{group_id}/invites', 'emails')

    def all(self, group_id):
        """
        List Users.

        :param str group_id: Group identifier
        :return: User iterator object
        :rtype: papi.lib.iterator.Iterator
        """
        return self._segment.iterator(f'/groups/{group_id}/users', 'users')

    def add(self, group_id, *emails):
        """
        Add Users to a Group.

        :param str group_id: Group identifier
        :param list[str] emails: List of emails
        :return: The updated group object
        :rtype: papi.common.common.Object
        """
        return self._execute(self._segment.post, group_id, *emails)

    def remove(self, group_id, *emails):
        """
        Remove Users from a Group.

        :param str group_id: Group identifier
        :param list[str] emails: List of emails
        :return: Status object indicating whether if the operation was successful
        :rtype: papi.common.common.Object
        """
        return Users._execute(self._segment.delete, group_id, *emails)

    def replace(self, group_id, *emails):
        """
        Replace Users in a Group.

        :param str group_id: Group identifier
        :param list[str] emails: List of emails
        :return: The updated group object
        :rtype: papi.common.common.Object
        """
        return Users._execute(self._segment.put, group_id, *emails)

    @staticmethod
    def _execute(function, group_id, *emails):
        return function(f'/groups/{group_id}/users', common.bunch(userGroupId=group_id, emails=list(emails)))


class Permissions(Construct):
    """
    Class for managing group access permissions
    """

    # add a builder class for permissions
    # https://api.segmentapis.com/docs/admin/iam/groups/#add-permissions-to-user-group
    def add(self, group_id, permissions):
        """
        Add a list of access permissions to a User Group.

        :param str group_id: Group identifier
        :param list[papi.common.common.Object] permissions: List of permissions
        :return: The updated list of permissions
        :rtype: list[papi.common.common.Object]
        """
        return Permissions._execute(self._segment.post, group_id, permissions)

    def replace(self, group_id, permissions):
        """
        Update the list of access permissions for a User Group.

        :param str group_id: Group identifier
        :param list[papi.common.common.Object] permissions: List of permissions
        :return: The updated list of permissions
        :rtype: list[papi.common.common.Object]
        """
        return Permissions._execute(self._segment.put, group_id, permissions)

    @staticmethod
    def _execute(function, group_id, permissions):
        return function(f'/groups/{group_id}/permissions', common.bunch(userGroupId=group_id, permissions=permissions))
