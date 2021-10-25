***************
Getting Started
***************

A Python SDK implementing the Segment app configuration management public API (PAPI).
Compatible with Python 3.8 or higher.

Installing Library Dependencies
-------------------------------

.. code-block:: console

   $ pip3 install -r requirements.txt

Importing the Library
---------------------
To get started, access the project directory and open a Python console:

.. code-block:: python

   >>> from papi import *
   >>> workspace = Segment.workspace('<api-token>', segment_enum.Region.euw1)  # access a Segment workspace in eu-west-1
   >>> print(workspace.info)
   >>> for source in workspace.connections.sources.all():
   ...     print(source.id, source.slug, source.name)

Once you have instantiated a workspace object, review the **User Guides** and the various modules.
To build the docs, see **Building Documentation** below.

Modules
-------
By importing the library, you gain access to the following modules:

1. **segment_enum** - Enumerator objects (e.g. Region, FunctionType, etc.)
2. **segment_types** - Classes, builders and named-tuples (e.g. Label, Connection, FunctionSettingsBuilder, etc.)
3. **segment_bunch** - Easy way to build key-value Python objects passed as function arguments
4. **segment_errors** - Exceptions and errors
5. **segment_settings** - Advanced system settings

Logging
-------
Log messages are printed to standard output, unless you choose to redirect them to a file.
The default log severity is set to ``logging.INFO``. To turn on verbose logging, change the log severity to ``logging.DEBUG``

* Changing the log severity: ``Logger.instance().level = logging.DEBUG``
* Redirecting logs to a file: ``export SEGMENT_PAPI_LOG_FILE=${pwd}/papi.log``

Building Documentation
----------------------
Documentation can be compiled by running ``make html`` from the ``docs``
directory. After compilation, access ``docs/build/html/index.html``.

Testing
-------

Use `tox <https://tox.readthedocs.org/>`_ to run tests in Python.
To install, use :code:`pip3 install tox`. Once installed, run `tox` from the project root directory.

.. code-block:: console

   $ tox
