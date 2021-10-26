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
        self.sync_schedule = SyncSchedule(segment)
        self.sync_config = SyncConfig(segment)

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


class SyncSchedule(Construct):
    """
    Class for managing Warehouse selective synchronization schedule
    """

    def get(self, warehouse_id):
        """
        Get advanced sync schedule for a warehouse

        :param str warehouse_id: Warehouse identifier
        :return: Warehouse synchronization schedule
        :rtype: papi.common.common.Object
        """
        # https://api.segmentapis.com/docs/connections/warehouses/selective-sync-schedule/#get-advanced-sync-schedule-from-warehouse
        return self._segment.get(f'/warehouses/{warehouse_id}/advanced-sync-schedule')

    def replace(self, warehouse_id, enabled, schedule=None):
        """
        Update a warehouse sync schedule

        :param str warehouse_id: Warehouse identifier
        :param bool enabled: Turn on an advanced sync schedule for the warehouse
        :param papi.common.common.Object,optional schedule: Synchronization schedule
        :return: Warehouse synchronization schedule
        :rtype: papi.common.common.Object
        """
        # https://api.segmentapis.com/docs/connections/warehouses/selective-sync-schedule/#replace-advanced-sync-schedule-for-warehouse
        param = common.bunch(
            warehouseId=warehouse_id,
            enabled=enabled
        )
        if schedule:
            param.schedule = schedule
        return self._segment.put(f'/warehouses/{warehouse_id}/advanced-sync-schedule', param)


class SyncConfig(Construct):
    """
    Class for managing Warehouse selective synchronization configuration
    """

    def get_schema(self, warehouse_id, source_id):
        """
        Get warehouse schema for a given source

        :param str warehouse_id: Warehouse identifier
        :param str source_id: Source identifier
        :return: Warehouse schema
        :rtype: papi.common.common.Object
        """
        # https://api.segmentapis.com/docs/connections/warehouses/selective-sync-config/#list-selective-syncs-from-warehouse-and-source
        return self._segment.iterator(f'/warehouses/{warehouse_id}/connected-sources/{source_id}/selective-syncs', 'items')

    def syncs(self, warehouse_id):
        """
        Get latest syncs for all sources connected to a warehouse

        :param str warehouse_id: Warehouse identifier
        :return: Latest syncs for the specfied warehouse
        :rtype: papi.common.common.Object
        """
        # https://api.segmentapis.com/docs/connections/warehouses/selective-sync-config/#list-syncs-from-warehouse
        return self._segment.iterator(f'/warehouses/{warehouse_id}/syncs', 'reports')

    def source_syncs(self, warehouse_id, source_id):
        """
        Get latest syncs of a source connected to a warehouse

        :param str warehouse_id: Warehouse identifier
        :param str source_id: Source identifier
        :return: Latest syncs for the specfied warehouse-source pair
        :rtype: papi.common.common.Object
        """
        # https://api.segmentapis.com/docs/connections/warehouses/selective-sync-config/#list-syncs-from-warehouse-and-source
        return self._segment.iterator(f'/warehouses/{warehouse_id}/connected-sources/{source_id}/syncs', 'reports')

    def update_schema(self, warehouse_id, sync_overrides):
        """
        Configure a warehouse schema

        :param str warehouse_id: Warehouse identifier
        :param str sync_overrides: List of sync schema overrides to apply to this warehouse
        :return: Object indicating whether the update was successfull and any associated warnings
        :rtype: papi.common.common.Object
        """
        # https://api.segmentapis.com/docs/connections/warehouses/selective-sync-config/#update-selective-sync-for-warehouse
        param = common.bunch(
            warehouseId=warehouse_id,
            syncOverrides=sync_overrides
        )
        return self._segment.patch(f'/warehouses/{warehouse_id}/selective-sync', param)
