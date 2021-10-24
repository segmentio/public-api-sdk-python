import logging
from ..lib import utils
from ..errors import errors
from ..common import common, settings
from .construct import Construct


class Sources(Construct):
    """
    Class for managing Segment Sources

    :ivar papi.constructs.sources.Settings settings: Object implementing Source Settings APIs
    :ivar papi.constructs.sources.Labels labels: Object implementing Source Labels APIs
    :ivar papi.constructs.sources.Regulations regulations: Object implementing Source Regulations APIs
    """

    def __init__(self, segment):
        super().__init__(segment)
        self.settings = Settings(segment)
        self.labels = Labels(segment)
        self.regulations = Regulations(segment)

    def add_from_source(self, source, slug=None, enabled=None, name=None, options=None):
        """
        Create a Source from an existing Source object.

        :param papi.common.common.Object source: Source object
        :param str,optional slug: Override the source slug
        :param bool,optional enabled: Override whether the source should be enabled or disabled on creation
        :param str,optional name: Override the source name
        :param dict[str, str],optional options: Override the source settings
        :return: Source object
        :rtype: papi.common.common.Object
        """
        logging.getLogger().debug('Adding source from an existing source object.')
        return self.add(
            source.metadata.slug,
            slug if slug else source.slug,
            enabled if enabled else source.enabled,
            name if name else source.name,
            options if options else source.settings
        )

    def add(self, catalog_slug, slug, enabled, name, options=None):
        """
        Create a Source.

        :param str catalog_slug: Catalog slug
        :param str slug: Source slug
        :param bool enabled: Whether to enable the source on creation
        :param str name: Source name
        :param dict[str, str],optional options: Source settings
        :return: Source object
        :rtype: papi.common.common.Object
        """
        source_metadata = self._segment.connections.catalog.get_source(catalog_slug)

        # settings.validate_settings(source_metadata.options, options)

        source = common.bunch(
            slug=slug,
            enabled=enabled,
            metadataId=source_metadata.id,
            name=name
        )

        if options:
            source.settings = settings.create_settings(options)

        logging.getLogger().debug('Adding source. %s', {'name': name, 'slug': slug, 'type': catalog_slug})
        response = self._segment.post('/sources', source)
        logging.getLogger().debug('Source added. %s', {'name': name, 'slug': slug, 'type': catalog_slug})
        return response.source

    def show(self):
        utils.print_table([[item.id, item.slug, item.name, item.enabled] for item in self.all()], ['ID', 'Slug', 'Name', 'Enabled'])

    def all(self):
        """
        List Sources.

        :return: Source iterator object
        :rtype: papi.lib.iterator.Iterator
        """
        return self._segment.iterator('/sources', 'sources')

    def delete(self, source_id):
        """
        Delete a Source.

        :param str source_id: Source identifier
        :return: Object indicating whether the deletion was successful or not
        :rtype: papi.common.common.Object
        """
        logging.getLogger().debug('Deleting source. %s', {'id': source_id})
        response = self._segment.delete(f'/sources/{source_id}', {'sourceId': source_id})
        logging.getLogger().debug('Source deleted. %s', {'id': source_id})
        return response

    def find(self, slug):
        """
        Find a Source by slug.

        :param str slug: Slug
        :return: Source object
        :rtype: papi.common.common.Object
        """
        for source in self.all():
            if source.slug == slug:
                logging.getLogger().debug('Found source. %s', {'id': source.id, 'slug': source.slug})
                return source
        logging.getLogger().debug('Source not found. %s', {'slug': slug})
        raise errors.ResourceNotFound(slug=slug, type='source')

    def get(self, source_id):
        """
        Get a Source.

        :param str source_id: Source identifier
        :return: Source object
        :rtype: papi.common.common.Object
        """
        logging.getLogger().debug('Retrieving source. %s', {'id': source_id})
        response = self._segment.get(f'/sources/{source_id}').source
        logging.getLogger().debug('Source retrieved. %s', {'id': source_id})
        return response

    def update(self, source_id, name=None, enabled=None, slug=None, options=None):
        """
        Update a Source.

        :param str source_id: Source identifier
        :param str,optional name: Source name
        :param bool,optional enabled: Whether to enable the source on creation
        :param str,optional slug: Source slug
        :param dict[str, str],optional options: Source settings
        :return: Source object
        :rtype: papi.common.common.Object
        """
        updates = common.bunch(sourceId=source_id)
        if name:
            updates.name = name
        if enabled:
            updates.enabled = enabled
        if slug:
            updates.slug = slug
        if options:
            updates.settings = settings.create_settings(options)
        logging.getLogger().debug('Updating source. %s', {'id': source_id})
        response = self._segment.patch(f'/sources/{source_id}', updates)
        logging.getLogger().debug('Source updated. %s', {'id': source_id})
        return response.source

    def destinations(self, source_id):
        """
        Get a list of Destinations connected to a Source.

        :param str source_id: Source identifier
        :return: List of connected destinations
        :rtype: list[papi.common.common.Object]
        """
        logging.getLogger().debug('Retrieving connected destinations. %s', {'id': source_id})
        response = self._segment.get(f'/sources/{source_id}/connected-destinations').destinations
        logging.getLogger().debug('Retrieved connected destinations. %s', {'id': source_id})
        return response

    def warehouses(self, source_id):
        """
        Get a list of Warehouses connected to a Source.

        :param str source_id: Source identifier
        :return: List of connected warehouses
        :rtype: list[papi.common.common.Object]
        """
        logging.getLogger().debug('Retrieving connected warehouses. %s', {'id': source_id})
        response = self._segment.get(f'/sources/{source_id}/connected-warehouses').warehouses
        logging.getLogger().debug('Retrieved connected warehouses. %s', {'id': source_id})
        return response


class Settings(Construct):
    """
    Class for managing Segment Source settings
    """

    def get(self, source_id):
        """
        Get a Source settings.

        :param str source_id: Source identifier
        :return: Source settings object
        :rtype: papi.common.common.Object
        """
        logging.getLogger().debug('Retrieving source settings. %s', {'id': source_id})
        response = self._segment.get(f'/sources/{source_id}/settings').settings
        logging.getLogger().debug('Source settings retrieved. %s', {'id': source_id})
        return response

    def update(self, source_id, track_settings=None,
               identify_settings=None, group_settings=None,
               forward_violations_to=None, forward_blocked_events_to=None):
        """
        Update a Source.

        :param str source_id: Source identifier
        :param papi.common.common.Object,optional track_settings: Track settings
        :param papi.common.common.Object,optional identify_settings: Identify settings
        :param papi.common.common.Object,optional group_settings: Group settings
        :param str,optional forward_violations_to: Source id to forward violations to
        :param str,optional forward_blocked_events_to: Source id to forward blocked events to
        :return: Source settings object
        :rtype: papi.common.common.Object
        """
        updates = common.bunch(sourceId=source_id)
        if track_settings:
            updates.track = track_settings
        if identify_settings:
            updates.identify = identify_settings
        if group_settings:
            updates.group = group_settings
        if forward_violations_to:
            updates.forwardingViolationsTo = forward_violations_to
        if forward_blocked_events_to:
            updates.forwardingBlockedEventsTo = forward_blocked_events_to
        logging.getLogger().debug('Updating source settings. %s', {'id': source_id})
        response = self._segment.patch(f'/sources/{source_id}/settings', updates)
        logging.getLogger().debug('Source settings updated. %s', {'id': source_id})
        return response


class Labels(Construct):
    """
    Class for managing Segment Source labels
    """

    def add(self, source_id, labels):
        """
        Assign Labels to a Source.

        :param str source_id: Source identifier
        :param list[tuple(str, str)]: List of label named-tuples
        :return: List of labels
        :rtype: list[papi.common.common.Object]
        """
        logging.getLogger().debug('Adding source labels. %s', {'id': source_id, 'labels': labels})
        response = Labels._execute(self._segment.post, source_id, labels)
        logging.getLogger().debug('Source labels added. %s', {'id': source_id, 'labels': labels})
        return response

    def replace(self, source_id, labels):
        """
        Replace all Labels assigned to a Source.

        :param str source_id: Source identifier
        :param list[tuple(str, str)]: List of label named-tuples
        :return: List of labels
        :rtype: list[papi.common.common.Object]
        """
        logging.getLogger().debug('Replacing source labels. %s', {'id': source_id, 'labels': labels})
        response = Labels._execute(self._segment.put, source_id, labels)
        logging.getLogger().debug('Source labels replaced. %s', {'id': source_id, 'labels': labels})
        return response

    @staticmethod
    def _execute(function, source_id, labels):
        return function(f'/sources/{source_id}/labels', common.bunch(sourceId=source_id, labels=labels)).labels


class Regulations(Construct):
    """
    Class for managing Segment Source regulations
    """

    # https://api.segmentapis.com/docs/deletion-and-suppression/#create-source-regulation
    def add(self, source_id, regulation_type, subject_type, subject_ids, cloud_source=False):
        """
        Create a Source Regulation.

        :param str source_id: Source identifier
        :param papi.common.enum.RegulationType regulation_type: Regulation type
        :param str subject_type: Subject type
        :param list[str] subject_ids: List of subject identifiers
        :param bool,optional cloud_source: Create a cloud source regulation, defaults to ``False``
        :return: Object including the regulation identifier
        :rtype: papi.common.common.Object
        """

    # https://api.segmentapis.com/docs/deletion-and-suppression/#list-regulations-from-source
    def all(self, source_id, regulation_status=None, regulation_types=None):
        """
        List Source Regulations.

        :param str source_id: Source identifier
        :param papi.common.enum.RegulationStatus,optional regulation_status: Regulation status
        :param list[papi.common.enum.RegulationType],optional regulation_types: List of regulation types
        :return: Regulation iterator object
        :rtype: papi.lib.iterator.Iterator
        """
        if regulation_status:
            self._segment.regulations._validate_regulation_status(regulation_status)  # pylint: disable=protected-access
        if regulation_types:
            self._segment.regulations._validate_regulation_types(regulation_types)  # pylint: disable=protected-access
        return self._segment.iterator(f'/regulations/sources/{source_id}', 'regulations')
