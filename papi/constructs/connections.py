from . import catalog, destinations, events, sources, warehouses
from ..common import types

from .construct import Construct


class Connections(Construct):
    """
    Class for managing Segment Connections

    :ivar papi.constructs.catalog.Catalog catalog: Object implementing Catalog APIs
    :ivar papi.constructs.sources.Sources sources: Object implementing Sources APIs
    :ivar papi.constructs.destinations.Destinations destinations: Object implementing Destinations APIs
    :ivar papi.constructs.warehouses.Warehouses warehouses: Object implementing Warehouses APIs
    """

    def __init__(self, segment):
        super().__init__(segment)
        self.catalog = catalog.Catalog(segment)
        self.destinations = destinations.Destinations(segment)
        self.events = events.Events(segment)
        self.sources = sources.Sources(segment)
        self.warehouses = warehouses.Warehouses(segment)

    def get(self):
        """
        Get a list of Connections.

        :returns: List of connections
        :rtype: list[papi.common.types.Connection]
        """
        for source in self.sources.all():
            for destination in self.sources.destinations(source.id):
                yield types.Connection(source, destination, False)
            for warehouse in self.sources.warehouses(source.id):
                yield types.Connection(source, warehouse, True)

    def export(self):
        pass
