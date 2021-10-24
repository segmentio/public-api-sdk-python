import logging
from ..lib import Iterator, Command
from ..http import SegmentClient
from ..constructs import admin, connections, echo, functions, protocols, usage, regulations
from ..settings import settings as segment_settings


class Workspace:  # pylint: disable=too-many-instance-attributes
    """
    Class for managing a Segment workspace configuration

    :ivar papi.constructs.admin.Administrator admin: Object implementing Workspace administration APIs
    :ivar papi.constructs.connections.Connections connections: Object implementing Connections APIs
    :ivar papi.constructs.functions.Functions functions: Object implementing Functions APIs
    :ivar papi.constructs.protocols.Protocols protocols: Object implementing Protocols APIs
    :ivar papi.constructs.regulations.Regulations regulations: Object implementing Regulation APIs
    :ivar papi.constructs.usage.Usage usage: Object implementing Usage APIs
    """

    def __init__(self, token, region=None):
        """
        :param str token: Public API token
        :param int region: Target region
        """
        self._region = region
        self._domain = (f'{self._region}.' if self._region else '') + 'api.segmentapis.com'
        self._segment = SegmentClient(token)

        self.admin = admin.Administrator(self)
        self.connections = connections.Connections(self)
        self.echo = echo.Echo(self).echo
        self.functions = functions.Functions(self)
        self.protocols = protocols.Protocols(self)
        self.regulations = regulations.Regulations(self)
        self.usage = usage.Usage(self)

    def get(self, path, params=None):
        return self._segment.get(self.baseurl, path, params or {})

    def show(self, path, params=None):
        print(self.get(path, params))

    def put(self, path, data):
        return self._segment.put(self.baseurl, path, data)

    def post(self, path, data):
        return self._segment.post(self.baseurl, path, data)

    def delete(self, path, params=None):
        return self._segment.delete(self.baseurl, path, params)

    def patch(self, path, data):
        return self._segment.patch(self.baseurl, path, data)

    def iterator(self, path, return_attribute, params=None):
        page_size = segment_settings.pagination['page_size']
        logging.getLogger().debug('Creating iterator. %s', {'path': path, 'page_size': page_size})
        return Iterator(Command(self.get, path), return_attribute, params, page_size, None)

    @property
    def domain(self):
        """
        Get domain.

        :return: The Segment API endpoint fully qualified domain name
        :rtype: str
        """
        return self._domain

    @property
    def info(self):
        """
        Get Workspace information.

        :return: Object including the workspace id, name and slug
        :rtype: papi.common.common.Object
        """
        return self.admin.settings.get()

    @property
    def baseurl(self):
        return f'https://{self._domain}'

    @staticmethod
    def _api_version(version):
        return f'application/vnd.segment.{version}+json'


class Segment:

    @staticmethod
    def workspace(token, region=None):
        return Workspace(token, region)
