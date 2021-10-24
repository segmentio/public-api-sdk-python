from ..lib import utils
from ..errors import errors
from .construct import Construct


class Catalog(Construct):
    """
    Class for accessing the Segment app catalog
    """

    def __init__(self, segment):
        super().__init__(segment)
        self.cache = dict(sources=None, destinations=None, warehouses=None)

    @staticmethod
    def _create_connection_index(iterable):
        return {connection.slug: connection for connection in iterable}

    def show_sources(self):
        """
        Print Sources.
        """
        Catalog._show_catalog(self.get_sources())

    def show_destinations(self):
        """
        Print Destinations.
        """
        Catalog._show_catalog(self.get_destinations())

    def show_warehouses(self):
        """
        Print Warehouses.
        """
        Catalog._show_catalog(self.get_warehouses())

    @staticmethod
    def _show_catalog(catalog):
        table = [[item.id, item.slug, item.name] for item in sorted(catalog, key=lambda x: x.slug)]
        utils.print_table(table, ['ID', 'Slug', 'Name'])

    def get_sources(self, slugs=None, from_cache=True):
        """
        Get Sources from catalog. By default, all sources will be returned unless you specify a list of source slugs.

        :param list[str],optional slugs: One or more slugs to retrieve, defaults to ``None``
        :param bool,optional from_cache: Get results from cache, defaults to ``True``
        :return: List of sources
        :rtype: list[papi.common.common.Object]
        """
        sources = self._list_catalog(from_cache, 'sources', self._get_sources)
        return Catalog._filter_catalog(sources, slugs)

    def get_source(self, slug, from_cache=True):
        """
        Get a Source from catalog.

        :param str slug: Source slug
        :param bool,optional from_cache: Get results from cache, defaults to ``True``
        :return: Source object
        :rtype: papi.common.common.Object
        """
        sources = self.get_sources([slug], from_cache)
        if not sources:
            raise errors.ResourceNotFound(slug=slug, type='source')
        return sources[0]

    def show_source_options(self, slug, from_cache=True):
        """
        Print Source options.

        :param str slug: Source slug
        :param bool,optional from_cache: Get results from cache, defaults to ``True``
        """
        Catalog._show_catalog_options(self.get_source, slug, from_cache)

    def get_destinations(self, slugs=None, from_cache=True):
        """
        Get Destinations from catalog. By default, all destinations will be returned unless you specify a list of destination slugs.

        :param list[str],optional slugs: One or more slugs to retrieve, defaults to ``None``
        :param bool,optional from_cache: Get results from cache, defaults to ``True``
        :return: List of destinations
        :rtype: list[papi.common.common.Object]
        """
        destinations = self._list_catalog(from_cache, 'destinations', self._get_destinations)
        return Catalog._filter_catalog(destinations, slugs)

    def get_destination(self, slug, from_cache=True):
        """
        Get a Destination from catalog.

        :param str slug: Destination slug
        :param bool,optional from_cache: Get results from cache, defaults to ``True``
        :return: Destination object
        :rtype: papi.common.common.Object
        """
        destinations = self.get_destinations([slug], from_cache)
        if not destinations:
            raise errors.ResourceNotFound(slug=slug, type='destination')
        return destinations[0]

    def show_destination_options(self, slug, from_cache=True):
        """
        Print Destination options.

        :param str slug: Destination slug
        :param bool,optional from_cache: Get results from cache, defaults to ``True``
        """
        Catalog._show_catalog_options(self.get_destination, slug, from_cache)

    def get_warehouses(self, slugs=None, from_cache=True):
        """
        Get Warehouses from catalog. By default, all warehouses will be returned unless you specify a list of warehouse slugs.

        :param list[str],optional slugs: One or more slugs to retrieve, defaults to ``None``
        :param bool,optional from_cache: Get results from cache, defaults to ``True``
        :return: List of warehouses
        :rtype: list[papi.common.common.Object]
        """
        warehouses = self._list_catalog(from_cache, 'warehouses', self._get_warehouses)
        return Catalog._filter_catalog(warehouses, slugs)

    def get_warehouse(self, slug, from_cache=True):
        """
        Get a Warehouse from catalog.

        :param str slug: Warehouse slug
        :param bool,optional from_cache: Get results from cache, defaults to ``True``
        :return: Warehouse object
        :rtype: papi.common.common.Object
        """
        warehouses = self.get_warehouses([slug], from_cache)
        if not warehouses:
            raise errors.ResourceNotFound(slug=slug, type='warehouse')
        return warehouses[0]

    def show_warehouse_options(self, slug, from_cache=True):
        """
        Print Warehouse options.

        :param str slug: Warehouse slug
        :param bool,optional from_cache: Get results from cache, defaults to ``True``
        """
        Catalog._show_catalog_options(self.get_warehouse, slug, from_cache)

    @staticmethod
    def _filter_catalog(catalog, slugs):
        if slugs:
            return [catalog[slug] for slug in slugs if catalog.get(slug, None) is not None]
        return catalog.values()

    def _list_catalog(self, from_cache, key, function):
        cache = self.cache.get(key, None)
        if from_cache and cache:
            return cache
        self.cache[key] = function()
        return self.cache[key]

    @staticmethod
    def _show_catalog_options(function, slug, from_cache=True):
        item = function(slug, from_cache)
        options = [[option.name, getattr(option, 'description', '-'), option.type, option.required] for option in item.options]
        if not options:
            print(f'No options found for slug: {slug}')
        utils.print_table(options, ['Name', 'Description', 'Type', 'Required'])

    def _get_sources(self):
        return Catalog._create_connection_index(self._segment.iterator('/catalog/sources', 'sourcesCatalog'))

    def _get_destinations(self):
        return Catalog._create_connection_index(self._segment.iterator('/catalog/destinations', 'destinationsCatalog'))

    def _get_warehouses(self):
        return Catalog._create_connection_index(self._segment.iterator('/catalog/warehouses', 'warehousesCatalog'))

    def get_source_metadata(self, source_id):
        """
        Get Source metadata from catalog.

        :param str source_id: Warehouse slug
        :return: Source metadata object
        :rtype: papi.common.common.Object
        """
        return self._segment.get(f'/catalog/sources/{source_id}').sourceMetadata

    def get_destination_metadata(self, destination_id):
        """
        Get Destination metadata from catalog.

        :param str source_id: Warehouse slug
        :return: Source metadata object
        :rtype: papi.common.common.Object
        """
        return self._segment.get(f'/catalog/destinations/{destination_id}').destinationMetadata

    def get_warehouse_metadata(self, warehouse_id):
        """
        Get Warehouse metadata from catalog.

        :param str source_id: Warehouse slug
        :return: Source metadata object
        :rtype: papi.common.common.Object
        """
        return self._segment.get(f'/catalog/warehouses/{warehouse_id}').warehouseMetadata
