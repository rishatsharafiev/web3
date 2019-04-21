def not_found(request, groups):
    response_headers = [
        ('Content-Type', 'text/html'),
    ]

    response_status = 404

    response_body = 'Page not found'

    return (response_body, response_headers, response_status)