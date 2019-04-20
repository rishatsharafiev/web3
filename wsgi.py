from urllib.parse import parse_qs
from html import escape


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
    get_parameters = parse_qs(environ.get('QUERY_STRING', ''))

    # application/x-www-form-urlencoded
    if environ.get('CONTENT_TYPE') == 'application/x-www-form-urlencoded':
        form_input = {}

        for key, value in request_body.items():
            if isinstance(value, list):
                form_input[key] = [escape(item) for item in value]
            else:
                form_input[key] = escape(value)

        response_body = str(form_input).encode('utf-8')
    else:
        response_body = str(get_parameters).encode('utf-8')

    # router
    routes = [
        r'', handler,
        
    ]


    status = '200 OK'


    # call router with requests object, return status{str}, response_body{str}

    response_headers = [
        ('Content-Type', 'text/html'),
        ('Content-Length', str(len(response_body)))
    ]

    start_response(status, response_headers)
    return [response_body]
