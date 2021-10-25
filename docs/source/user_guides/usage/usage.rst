*****
Usage
*****

.. toctree::
   :caption: Usage
   :maxdepth: 2

.. automethod:: papi.constructs.usage.Sources.daily
   :noindex:

.. code-block:: python

   """Get per-source api call count"""
   for daily_source_api_usage in workspace.usage.sources.api.daily('2021-11-01'):
       print(daily_source_api_usage)

   """Get per-source mtu count"""
   for daily_source_mtu_usage in workspace.usage.sources.mtu.daily('2021-11-01'):
       print(daily_source_mtu_usage)

.. automethod:: papi.constructs.usage.Workspace.daily
   :noindex:

.. code-block:: python

   """Get daily workspace api call count"""
   for daily_workspace_api_usage in workspace.usage.workspace.api.daily('2021-11-01'):
       print(daily_source_api_usage)

   """Get daily workspace mtu count"""
   for daily_workspace_mtu_usage in workspace.usage.workspace.mtu.daily('2021-11-01'):
       print(daily_workspace_mtu_usage)
