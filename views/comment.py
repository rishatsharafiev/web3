from utils.template import get_template
from utils.views import not_found


class CommentView:
    """Comment View"""
    
    @staticmethod
    def add(request, groups):
        """Add new comment"""
        response_headers = [
            ('Content-Type', 'text/html; charset=utf-8'),
        ]
        request_method = request.get('environ', {}).get('REQUEST_METHOD')

        if request_method == 'POST':
            response_body = get_template('comment/show.html').safe_substitute(**{'request_method': request_method})
            response_status = 201
            return (response_body, response_headers, response_status)
        elif request_method == 'GET':
            response_body = get_template('comment/add.html').safe_substitute(**{'request_method': request_method})
            response_status = 200
            return (response_body, response_headers, response_status)
        else:
            not_found(request, groups)
