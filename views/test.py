from utils.template import get_template


def test(request, groups):
    response_headers = [
        ('Content-Type', 'text/html; charset=utf-8'),
    ]

    response_status = 200

    pk = groups.group('pk')
    from settings import BASE_DIR, TEMPLATE_DIR, STATIC_DIR
    response_body = get_template('index.html').safe_substitute(**{'who': pk})

    return (response_body, response_headers, response_status)
