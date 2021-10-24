import logging
import itertools
from ..common import common, enum
from .construct import Construct


class Functions(Construct):
    """
    Class for managing Segment Functions
    """

    def add_from_function(self, function, code=None, settings=None, display_name=None, logo_url=None, description=None):
        """
        Create a Function from an existing Function object.

        :param papi.common.common.Object function: Function object
        :param str,optional code: Override function code
        :param papi.common.common.Object,optional settings: Override function settings
        :param str,optional display_name: Override function display name
        :param str,optional logo_url: Override function logo url
        :param str,optional description: Override function description
        :return: Function object
        :rtype: papi.common.common.Object
        """

        logging.getLogger().debug('Adding function from an existing function object.')
        return self.add(
            function.resourceType,
            code if code else function.code,
            settings if settings else function.settings,
            display_name if display_name else function.displayName,
            logo_url if logo_url else function.logoUrl,
            description if description else function.description
        )

    def add(self, function_type, code, settings, display_name, logo_url=None, description=None):
        """
        Create a Function.

        :param papi.common.enum.FunctionType function_type: Function type
        :param str code: Function code
        :param papi.common.common.Object settings: Function settings
        :param str display_name: Function display name
        :param str,optional logo_url: Function logo url
        :param str,optional description: Function description
        :return: Function object
        :rtype: papi.common.common.Object
        """
        enum.validate_enum_option(enum.FunctionType, function_type)
        function = common.bunch(code=code, settings=settings, resourceType=function_type, displayName=display_name)
        if logo_url:
            function.logoUrl = logo_url
        if description:
            function.description = description

        logging.getLogger().debug('Adding %s function. %s', function_type.lower(), {'display_name': display_name})
        response = self._segment.post('/functions', function).function
        logging.getLogger().debug('%s function added. %s', function_type.capitalize(), {'display_name': display_name})
        return response

    def all(self, function_type=None):
        """
        List Functions.

        :param papi.common.enum.FunctionType,optional function_type: Filter by function type
        :return: Function iterator object
        :rtype: papi.lib.iterator.Iterator
        """
        if function_type:
            enum.validate_enum_option(enum.FunctionType, function_type)
            logging.getLogger().debug('Retrieving %s functions.', function_type.lower())
            return self._segment.iterator('/functions', 'functions', {'resourceType': function_type})

        logging.getLogger().debug('Retrieving all functions.')
        return itertools.chain(
            self._segment.iterator('/functions', 'functions', {'resourceType': enum.FunctionType.SOURCE}),
            self._segment.iterator('/functions', 'functions', {'resourceType': enum.FunctionType.DESTINATION})
        )

    def deploy(self, function_id):
        """
        Deploy a Function.

        :param str function_id: Function identifier
        :return: Status object indicating whether if the operation was successful
        :rtype: papi.common.common.Object
        """
        logging.getLogger().debug('Deploying function. %s', {'id': function_id})
        response = self._segment.post(f'/functions/{function_id}/deploy').functionDeployment
        logging.getLogger().debug('Deployed function. %s', {'id': function_id})
        return response

    def delete(self, function_id):
        """
        Delete a Function.

        :param str function_id: Function identifier
        :return: Object indicating whether the deletion was successful or not
        :rtype: papi.common.common.Object
        """
        logging.getLogger().debug('Deleting function. %s', {'id': function_id})
        response = self._segment.delete(f'/functions/{function_id}', {'functionId': function_id})
        logging.getLogger().debug('Function deleted. %s', {'id': function_id})
        return response

    def get(self, function_id):
        """
        Get a Function.

        :param str function_id: Function identifier
        :return: Function object
        :rtype: papi.common.common.Object
        """
        return self._segment.get(f'/functions/{function_id}').function

    def update(self, function_id, code=None, settings=None, display_name=None, logo_url=None, description=None):
        """
        Update a Function.

        :param str function_id: Function identifier
        :param str,optional code: Function code
        :param papi.common.common.Object,optional settings: Function settings
        :param str,optional display_name: Function display name
        :param str,optional logo_url: Function logo url
        :param str,optional description: Function description
        :return: Function object
        :rtype: papi.common.common.Object
        """
        updates = common.bunch(functionId=function_id)
        if code:
            updates.code = code
        if settings:
            updates.settings = settings
        if display_name:
            updates.displayName = display_name
        if logo_url:
            updates.logoUrl = logo_url
        if description:
            updates.description = description
        logging.getLogger().debug('Updating function. %s', {'id': function_id})
        response = self._segment.patch(f'/functions/{function_id}', updates)
        logging.getLogger().debug('Function updated. %s', {'id': function_id})
        return response.function

    def get_function_code(self, function_id):
        """
        Get Function code.

        :return: Function code
        :rtype: str
        """
        logging.getLogger().debug('Retrieving function code. %s', {'id': function_id})
        return self.get(function_id).code
