STATUS_NOT_FOUND = '404 Not Found'
STATUS_INTERNAL_ERROR = '500 Internal Server Error'

STATUS_CHOICES = {
    200: '200 OK',
    201: '201 Created',
    302: '301 Moved Permanently',
    400: '400 Bad Request',
    401: '401 Unauthorized',
    403: '403 Forbidden',
    404: STATUS_NOT_FOUND,
    500: STATUS_INTERNAL_ERROR,
}