from . import audit, groups, labels, roles, settings, users

from .construct import Construct


class Administrator(Construct):
    """
    Class for managing administrative settings

    :ivar papi.constructs.audit.Audit audit: Object implementing Auditing APIs
    :ivar papi.constructs.groups.Groups groups: Object implementing Groups APIs
    :ivar papi.constructs.labels.Labels labels: Object implementing Labels APIs
    :ivar papi.constructs.roles.Roles roles: Object implementing Roles APIs
    :ivar papi.constructs.settings.Settings settings: Object implementing Workspace settings APIs
    :ivar papi.constructs.users.Users users: Object implementing Users APIs
    """

    def __init__(self, segment):
        super().__init__(segment)
        self.audit = audit.Audit(segment)
        self.groups = groups.Groups(segment)
        self.labels = labels.Labels(segment)
        self.roles = roles.Roles(segment)
        self.settings = settings.Settings(segment)
        self.users = users.Users(segment)
