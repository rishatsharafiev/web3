def test(request, groups):
    response_headers = [
        ('Content-Type', 'text/html; charset=utf-8'),
    ]

    response_status = 200

    pk = groups.group('pk')
    response_body = f'<html><header><title>Hello</title></header><body>Hello {pk}</body></html>'

    return (response_body, response_headers, response_status)
