def method_not_allowed(request, groups):
    response_headers = [
        ('Content-Type', 'text/html'),
    ]

    response_status = 405

    response_body = 'Method not allowed'

    return (response_body, response_headers, response_status)
