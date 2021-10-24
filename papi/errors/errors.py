import json


class SegmentException(Exception):

    def __init__(self, message, **kwargs):
        super().__init__()
        self.message = message
        self.put(**kwargs)

    def put(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        return json.dumps(self, default=lambda o: o.__dict__, indent=5)


class InputError(SegmentException):
    pass


class ServerError(SegmentException):

    def __init__(self):
        super().__init__('Server error', code=500, description='Segment was unable to serve the request due to an internal failure')


class ClientError(SegmentException):

    def __init__(self, code, message, description, **kwargs):
        super().__init__(message, code=code, description=description, **kwargs)


class BadRequest(ClientError):

    def __init__(self, **kwargs):
        super().__init__(400, 'Bad Request',
                         'The server cannot or will not process the request due to an apparent client error', **kwargs)


class Unauthorized(ClientError):

    def __init__(self, **kwargs):
        super().__init__(401, 'UnAuthorized',
                         'No authorization, or incorrect authorization provided for the resource', **kwargs)


class Forbidden(ClientError):

    def __init__(self, **kwargs):
        super().__init__(403, 'Forbidden',
                         'No authorization, or incorrect authorization provided for the resource', **kwargs)


class ResourceNotFound(ClientError):

    def __init__(self, **kwargs):
        super().__init__(404, 'Resource not found',
                         'The requested resource does not exist or cannot be found', **kwargs)


class Conflict(ClientError):

    def __init__(self, **kwargs):
        super().__init__(409, 'Conflict',
                         'There was a conflict when processing this request that prevented it from being fulfilled', **kwargs)


class UnprocessableEntity(ClientError):

    def __init__(self, **kwargs):
        super().__init__(422, 'Unprocessable entity',
                         'The request contained invalid parameters and was not accepted', **kwargs)


class TooManyRequests(ClientError):

    def __init__(self, **kwargs):
        super().__init__(429, 'Too many requests',
                         'Too many sequential or concurrent requests to a specific resource or endpoint were made', **kwargs)


class UnknownError(SegmentException):

    def __init__(self, **kwargs):
        super().__init__('Unknown error', **kwargs)


class ErrorFactory:

    HTTP_CLIENT_ERRORS = {
        400: BadRequest(),
        401: Unauthorized(),
        403: Forbidden(),
        404: ResourceNotFound(),
        409: Conflict(),
        422: UnprocessableEntity(),
        429: TooManyRequests()
    }

    @staticmethod
    def create(code, **kwargs):
        error = ErrorFactory.HTTP_CLIENT_ERRORS.get(code, None)

        if not error:

            if code >= 500:
                error = ServerError()
            elif code >= 400:
                error = ClientError(code, 'Unclassified Client Error',
                                    'The server cannot or will not process the request due to an apparent client error')
            else:
                error = UnknownError()

        error.put(**kwargs)
        return error
