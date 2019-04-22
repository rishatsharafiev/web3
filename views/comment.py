from utils.template import get_template
from utils.views import not_found
from utils.shortcuts import get_item
from utils.http import redirect


class CommentView:
    """Comment View"""
    
    @staticmethod
    def add(request, groups):
        """Add new comment"""
        response_headers = [
            ('Content-Type', 'text/html; charset=utf-8'),
        ]
        request_method = request.environ.get('REQUEST_METHOD')
        text_input = get_item(request.form_input.get('text', []), 'Hello')

        if request_method == 'POST':
            return redirect()
        elif request_method == 'GET':
            response_body = get_template('comment/add.html').safe_substitute()
            response_status = 200
            return (response_body, response_headers, response_status)
        else:
            not_found(request, groups)