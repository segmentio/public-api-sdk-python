from .construct import Construct


class Echo(Construct):
    """
    Class used for testing the Segment Public API
    """

    def echo(self, message, delay=None, trigger_error=False,
             trigger_multiple_errors=False, trigger_unexpected_error=False, status_code=None):
        """
        Echo.

        :param str message: Sets the response ``message`` field. The response contains this field as-is
        :param int delay: Delays the response by the given number of milliseconds.
        :param bool trigger_error: If ``True``, returns an HTTP 4xx error, with ``message`` as the error message
        :param bool trigger_multiple_errors: If ``True``, returns an HTTP 4xx error, with copies of ``message`` as the error message array.
         This has no effect if the request sets ``triggerError``.
        :param bool trigger_unexpected_error: If ``True``, triggers a 500 error.
         This has no effect if the request sets either ``triggerError`` or ``triggerMultipleErrors``.
        :param int status_code: Sets the HTTP status code to return.
        """
        params = {'message': message}
        if delay:
            params['delay'] = delay
        if trigger_error:
            params['triggerError'] = trigger_error
        elif trigger_multiple_errors:
            params['triggerMultipleErrors'] = trigger_multiple_errors
        elif trigger_unexpected_error:
            params['triggerUnexpectedError'] = trigger_unexpected_error
        elif status_code:
            params['statusCode'] = status_code
        return self._segment.get('/echo', params)
