from utils.template import get_template
from utils.views import not_found
from utils.shortcuts import get_item
from utils.http import redirect

from repositories import RegionRepository


class CommentView:
    """Comment View"""
    
    @staticmethod
    def add(request, groups):
        """Add new comment"""
        response_headers = [
            ('Content-Type', 'text/html; charset=utf-8'),
        ]
        request_method = request.environ.get('REQUEST_METHOD')

        if request_method == 'POST':
            text_input = get_item(request.form_input.get('text', []), None)
            text_input = get_item(request.form_input.get('text', []), None)
            text_input = get_item(request.form_input.get('text', []), None)

            return redirect()
        elif request_method == 'GET':
            regions = RegionRepository.get_all()
            option_template = get_template('comment/option.html')
            region_options = [option_template.safe_substitute(**{'id': region.id, 'name': region.name}) for region in regions]

            response_context = {
                'region_options': region_options
            }
            response_body = get_template('comment/add.html').safe_substitute(**response_context)
            response_status = 200
            return (response_body, response_headers, response_status)
        else:
            return not_found(request, groups)
