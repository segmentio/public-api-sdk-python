from ..common import common, settings
from .construct import Construct


class Warehouses(Construct):
    """
    Class for managing Segment Warehouses

    :ivar papi.constructs.warehouses.Sources sources: Object implementing Warehouse Sources APIs
    """

    def __init__(self, segment):
        super().__init__(segment)
        self.sources = Sources(segment)

    def add(self, catalog_slug, name, enabled=False, options=None):
        """
        Create a Warehouse.

        :param str catalog_slug: Catalog slug
        :param str name: Warehouse name
        :param bool,optional enabled: Whether to enable the warehouse on creation
        :param dict[str, str],optional options: Warehouse settings
        :return: Warehouse object
        :rtype: papi.common.common.Object
        """
        warehouse_metadata = self._segment.connections.catalog.get_warehouse(catalog_slug)

        settings.validate_settings(warehouse_metadata.options, options)

        warehouse = common.bunch(
            enabled=enabled,
            metadataId=warehouse_metadata.id,
            name=name,
            settings=settings.create_settings(options)
        )

        return self._segment.post('/warehouses', warehouse)

    def all(self):
        """
        List Warehouses.

        :return: Warehouse iterator object
        :rtype: papi.lib.iterator.Iterator
        """
        return self._segment.iterator('/warehouses', 'warehouses')

    def get(self, warehouse_id):
        """
        Get a Warehouse.

        :param str warehouse_id: Warehouse identifier
        :return: Warehouse object
        :rtype: papi.common.common.Object
        """
        return self._segment.get(f'/warehouses/{warehouse_id}').warehouse

    def delete(self, warehouse_id):
        """
        Delete a Warehouse.

        :param str warehouse_id: Warehouse identifier
        :return: Object indicating whether the deletion was successful or not
        :rtype: papi.common.common.Object
        """
        return self._segment.delete(f'/warehouses/{warehouse_id}', {'warehouseId': warehouse_id})

    def update(self, warehouse_id, name=None, enabled=None, options=None):
        """
        Update a Warehouse.

        :param str warehouse_id: Warehouse identifier
        :param str,optional name: Warehouse name
        :param bool,optional enabled: Whether to enable the warehouse on creation
        :param dict[str, str],optional options: Warehouse settings
        :return: Warehouse object
        :rtype: papi.common.common.Object
        """
        updates = common.bunch(warehouseId=warehouse_id)
        if name:
            updates.name = name
        if enabled:
            updates.enabled = enabled
        if options:
            updates.settings = settings.create_settings(options)
        return self._segment.patch(f'/warehouses/{warehouse_id}', updates)

    def get_connection_state(self, warehouse_id):
        """
        Get Warehouse connection state.

        :param str warehouse_id: Warehouse identifier
        :return: Object representing the Warehouse connection state
        :rtype: papi.common.common.Object
        """
        return self._segment.get(f'/warehouses/{warehouse_id}/connection-state')


class Sources(Construct):
    """
    Class for managing Segment Warehouse Sources
    """

    def all(self, warehouse_id):
        """
        Get all sources connected to a warehouse.

        :param str warehouse_id: Warehouse identifier
        :return: List of sources
        :rtype: list[papi.common.common.Object]
        """
        return self._segment.get(f'/warehouses/{warehouse_id}/connected-sources').sources

    def add(self, warehouse_id, source_id):
        """
        Connect a source to a warehouse.

        :param str warehouse_id: Warehouse identifier
        :param str source_id: Source identifier
        :return: Status object indicating whether if the operation was successful
        :rtype: papi.common.common.Object
        """
        return self._segment.post(f'/warehouses/{warehouse_id}/connected-sources/{source_id}')

    def remove(self, warehouse_id, source_id):
        """
        Disconnect a source from a warehouse.

        :param str warehouse_id: Warehouse identifier
        :param str source_id: Source identifier
        :return: Status object indicating whether if the operation was successful
        :rtype: papi.common.common.Object
        """
        return self._segment.delete(f'/warehouses/{warehouse_id}/connected-sources/{source_id}')
