import re
from urllib.parse import parse_qs
from html import escape
from utils.http.status import STATUS_CHOICES, STATUS_INTERNAL_ERROR
from utils.views import internal_error, not_found

from urls import url_patterns


def router(path_info, request):
    try:
        for item in url_patterns:
            pattern, handler = item
            groups = re.search(pattern, path_info)
            if groups:
                return handler(request, groups)
    except Exception as exp:
        print('Error: {exp}'.format(exp=exp))
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
