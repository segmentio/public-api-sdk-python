*******
Catalog
*******
.. toctree::
   :caption: Catalog
   :maxdepth: 2

Sources
-------

.. automethod:: papi.constructs.catalog.Catalog.show_sources
   :noindex:

.. code-block:: python

   workspace.connections.catalog.show_sources()

.. automethod:: papi.constructs.catalog.Catalog.get_source
   :noindex:

.. code-block:: python

   workspace.connections.catalog.get_source('javascript')

.. automethod:: papi.constructs.catalog.Catalog.get_sources
   :noindex:

.. code-block:: python

   sources = workspace.connections.catalog.get_source(['javascript', 'marketo', 'swift'])

.. automethod:: papi.constructs.catalog.Catalog.show_source_options
   :noindex:

.. code-block:: python

   workspace.connections.catalog.show_source_options('zendesk')

.. automethod:: papi.constructs.catalog.Catalog.get_source_metadata
   :noindex:

.. code-block:: python

   ajs = workspace.connections.catalog.get_source('javascript')
   ajs_metadata = workspace.connections.catalog.get_source_metadata(ajs.id)

Destinations
------------
.. automethod:: papi.constructs.catalog.Catalog.show_destinations
   :noindex:

.. code-block:: python

   workspace.connections.catalog.show_destinations()

.. automethod:: papi.constructs.catalog.Catalog.get_destination
   :noindex:

.. code-block:: python

   s3 = workspace.connections.catalog.get_destination('aws-s3')

.. automethod:: papi.constructs.catalog.Catalog.get_destinations
   :noindex:

.. code-block:: python

   destinations = workspace.connections.catalog.get_destination(['google-analytics', 'amazon-kinesis', 'eloqua'])

.. automethod:: papi.constructs.catalog.Catalog.show_destination_options
   :noindex:

.. code-block:: python

   workspace.connections.catalog.show_destination_options('aws-s3')

.. automethod:: papi.constructs.catalog.Catalog.get_destination_metadata
   :noindex:

   aws_s3 = workspace.connections.catalog.get_destination('aws-s3')
   aws_s3_metadata = workspace.connections.catalog.get_destination_metadata(aws_s3.id)

Warehouses
----------
.. automethod:: papi.constructs.catalog.Catalog.show_warehouses
   :noindex:

.. code-block:: python

   workspace.connections.catalog.show_warehouses()

.. automethod:: papi.constructs.catalog.Catalog.get_warehouse
   :noindex:

.. code-block:: python

   workspace.connections.catalog.get_warehouse('redshift')

.. automethod:: papi.constructs.catalog.Catalog.get_warehouses
   :noindex:

.. code-block:: python

   warehouses = workspace.connections.catalog.get_warehouse(['azuresqldb', 'db2', 'postgres'])

.. automethod:: papi.constructs.catalog.Catalog.show_warehouse_options
   :noindex:

.. code-block:: python

   workspace.connections.catalog.show_warehouse_options('postgres')

.. automethod:: papi.constructs.catalog.Catalog.get_warehouse_metadata
   :noindex:

.. code-block:: python

   redshift = workspace.connections.catalog.get_warehouse('redshift')
   redshift_metadata = workspace.connections.catalog.get_warehouse_metadata(redshift.id)
