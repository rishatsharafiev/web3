from urllib.parse import parse_qs
from html import escape
from urls import url_patterns
import re

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

def not_found(request, groups):
    response_headers = [
        ('Content-Type', 'text/html'),
    ]

    response_status = 404

    response_body = 'Page not found'

    return (response_body, response_headers, response_status)


def internal_error(request, groups):
    response_headers = [
        ('Content-Type', 'text/html'),
    ]

    response_status = 500

    response_body = 'Internal Error'

    return (response_body, response_headers, response_status)


def router(path_info, request):
    try:
        for item in url_patterns:
            pattern, handler = item
            groups = re.search(pattern, path_info)
            if groups:
                return handler(request, groups)
    except Exception as exp:
        return internal_error(request, groups)
    return not_found(request, groups)

def application(environ, start_response):
    """Application handler"""
    
    # content length
    try:
        request_body_size = int(environ.get('CONTENT_LENGTH', 0))
    except (ValueError):
        request_body_size = 0

    # request body
    if 'wsgi.input' in environ:
        request_body = parse_qs(environ['wsgi.input'].read(request_body_size).decode('utf-8'))
    else:
        request_body = ''

    # query string
    query_parameters = parse_qs(environ.get('QUERY_STRING', ''))

    # application/x-www-form-urlencoded
    form_input = {}
    if environ.get('CONTENT_TYPE') == 'application/x-www-form-urlencoded':
        for key, value in request_body.items():
            if isinstance(value, list):
                form_input[key] = [escape(item) for item in value]
            else:
                form_input[key] = escape(value)

    # request
    request = {
        'body': request_body,
        'query_parameters': query_parameters,
        'form_input': form_input,
        'environ': environ,
    }

    # router
    path_info = environ.get('PATH_INFO', '/')
    response_body, response_headers, response_status = router(path_info, request)

    # body
    response_body = response_body.encode('utf-8')

    # response status
    response_status = STATUS_CHOICES.get(response_status, STATUS_INTERNAL_ERROR)

    # response headers
    response_headers = [
        ('Content-Length', str(len(response_body))),  # must be after response_body last call
    ]

    start_response(response_status, response_headers)
    return [response_body]
