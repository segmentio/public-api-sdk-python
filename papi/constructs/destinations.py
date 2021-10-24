import logging
from ..common import common, settings
from .construct import Construct


class Destinations(Construct):
    """
    Class for managing Segment Destinations

    :ivar papi.constructs.destinations.Filters filters: Object implementing Destination Filters APIs
    """

    def __init__(self, segment):
        super().__init__(segment)
        self.filters = Filters(segment)

    def add_from_destination(self, destination, source_slug, name=None, enabled=None, options=None):
        """
        Create a Destination from an existing Destination object.

        :param papi.common.common.Object destination: Destination object
        :param str,optional name: Override the destination name
        :param bool,optional enabled: Override whether the destination should be enabled or disabled on creation
        :param dict[str, str],optional options: Override the destination settings
        :return: Destination object
        :rtype: papi.common.common.Object
        """
        logging.getLogger().debug('Adding destination from an existing destination object.')
        return self.add(
            destination.metadata.slug,
            name if name else destination.name,
            source_slug,
            enabled if enabled else destination.enabled,
            options if options else destination.settings
        )

    def add(self, catalog_slug, name, source_slug, enabled=False, options=None):
        """
        Create a Destination.

        :param str catalog_slug: Catalog slug
        :param str name: Destination name
        :param str source_slug: Source slug
        :param bool,optional enabled: Whether to enable the destination on creation
        :param papi.common.common.Object,optional options: Destination settings
        :return: Destination object
        :rtype: papi.common.common.Object
        """
        destination_metadata = self._segment.connections.catalog.get_destination(catalog_slug)

        # settings.validate_settings(destination_metadata.options, options)

        destination = common.bunch(
            enabled=enabled,
            metadataId=destination_metadata.id,
            name=name,
            sourceId=self._segment.connections.sources.find(source_slug).id,
        )

        if options:
            destination.settings = options

        logging.getLogger().debug('Adding destination. %s', {'name': name, 'source_slug': source_slug})
        response = self._segment.post('/destinations', destination).destination
        logging.getLogger().debug('Destination added. %s', {'name': name, 'source_slug': source_slug})
        return response

    def all(self):
        """
        List Destinations.

        :return: Source iterator object
        :rtype: papi.lib.iterator.Iterator
        """
        return self._segment.iterator('/destinations', 'destinations')

    def get(self, destination_id):
        """
        Get a Destination.

        :param str destination_id: Destination identifier
        :return: Destination object
        :rtype: papi.common.common.Object
        """
        return self._segment.get(f'/destinations/{destination_id}').destination

    def delete(self, destination_id):
        """
        Delete a Destination.

        :param str destination_id: Destination identifier
        :return: Object indicating whether the deletion was successful or not
        :rtype: papi.common.common.Object
        """
        logging.getLogger().debug('Deleting destination. %s', {'id': destination_id})
        response = self._segment.delete(f'/destinations/{destination_id}', {'destinationId': destination_id})
        logging.getLogger().debug('Destination deleted. %s', {'id': destination_id})
        return response

    def update(self, destination_id, name=None, enabled=None, options=None):
        """
        Update a Destination.

        :param str destination_id: Destination identifier
        :param str,optional name: Destination name
        :param bool,optional enabled: Whether to enable the destination on creation
        :param dict[str, str],optional options: Destination settings
        :return: Destination object
        :rtype: papi.common.common.Object
        """
        updates = common.bunch(destinationId=destination_id)
        if name:
            updates.name = name
        if enabled:
            updates.enabled = enabled
        if options:
            updates.settings = settings.create_settings(options)
        logging.getLogger().debug('Updating destination. %s', {'id': destination_id})
        response = self._segment.patch(f'/destinations/{destination_id}', updates).destination
        logging.getLogger().debug('Destination updated. %s', {'id': destination_id})
        return response


class Filters(Construct):
    """
    Class for managing Destination filters
    """

    def add(self):
        pass

    def all(self):
        pass

    def get(self):
        pass

    def remove(self):
        pass

    def update(self):
        pass
