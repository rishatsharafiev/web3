def redirect():
    """Redirect"""
    response_body = ''
    response_headers = [
        ('Location', '/')
    ]
    response_status = 301
    return (response_body, response_headers, response_status)
