def internal_error(request, groups):
    response_headers = [
        ('Content-Type', 'text/html'),
    ]

    response_status = 500

    response_body = 'Internal Error'

    return (response_body, response_headers, response_status)
