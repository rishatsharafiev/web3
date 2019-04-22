def redirect(url='/'):
    """Redirect"""
    response_body = ''
    response_headers = [
        ('Location', url)
    ]
    response_status = 301
    return (response_body, response_headers, response_status)
