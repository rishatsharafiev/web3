from utils.template import get_template
from utils.views import method_not_allowed
from utils.shortcuts import get_item
from utils.http import redirect

from repositories import CommentRepository, RegionRepository
from entities import CommentEntity

class CommentView:
    """Comment View"""

    @staticmethod
    def index(request, groups):
        """Index comment"""
        response_headers = [
            ('Content-Type', 'text/html; charset=utf-8'),
        ]
        request_method = request.environ.get('REQUEST_METHOD')

        if request_method == 'GET':
            comment_entities = CommentRepository.get_all()
            item_template = get_template('comment/item.html')
            content = [item_template.safe_substitute(**{
                'id': comment.id,
                'first_name': comment.first_name,
                'second_name': comment.second_name,
                'last_name': comment.last_name,
                'phone': comment.phone,
                'email': comment.email,
                'text': comment.text,
            }) for comment in comment_entities]

            response_context = {
                'content': "".join(content)
            }
            response_body = get_template('comment/index.html').safe_substitute(**response_context)
            response_status = 200
            return (response_body, response_headers, response_status)
        else:
            return method_not_allowed(request, groups)

    @staticmethod
    def remove(request, groups):
        """remove comment by pk"""
        response_headers = [
            ('Content-Type', 'text/html; charset=utf-8'),
        ]
        request_method = request.environ.get('REQUEST_METHOD')
        comment_id = groups.group('comment_id')

        if request_method == 'GET' and comment_id:
            CommentRepository.remove(pk=comment_id)
            return redirect(url='/view/')
        else:
            return method_not_allowed(request, groups)

    @staticmethod
    def add(request, groups):
        """Add new comment"""
        response_headers = [
            ('Content-Type', 'text/html; charset=utf-8'),
        ]
        request_method = request.environ.get('REQUEST_METHOD')

        if request_method == 'POST':
            last_name = get_item(request.form_input.get('last_name', []), None)
            first_name = get_item(request.form_input.get('first_name', []), None)
            second_name = get_item(request.form_input.get('second_name', []), None)
            city = get_item(request.form_input.get('city', []), None)
            phone = get_item(request.form_input.get('phone', []), None)
            email = get_item(request.form_input.get('email', []), None)
            text = get_item(request.form_input.get('text', []), None)

            try:
                city_id = city
            except ValueError:
                city_id = None
            
            result = None
            if last_name and first_name and text:
                comment_entity = CommentEntity(
                    _last_name=last_name,
                    _first_name=first_name,
                    _text=text,
                    _city_id=city_id,
                    _second_name=second_name, 
                    _phone=phone, 
                    _email=email,
                )
                result = CommentRepository.create(comment_entity)

            if result:
                return redirect(url='/comment/success/')
            else:
                return redirect(url='/comment/fail/')
        elif request_method == 'GET':
            regions = RegionRepository.get_all()
            option_template = get_template('comment/option.html')
            region_options = [option_template.safe_substitute(**{'id': region.id, 'name': region.name}) for region in regions]

            response_context = {
                'region_options': "".join(region_options)
            }
            response_body = get_template('comment/add.html').safe_substitute(**response_context)
            response_status = 200
            return (response_body, response_headers, response_status)
        else:
            return method_not_allowed(request, groups)

    @staticmethod
    def success(request, groups):
        """Success comment"""
        response_headers = [
            ('Content-Type', 'text/html; charset=utf-8'),
        ]
        response_body = get_template('comment/success.html').safe_substitute()
        response_status = 200
        return (response_body, response_headers, response_status)

    @staticmethod
    def fail(request, groups):
        """Fail comment"""
        response_headers = [
            ('Content-Type', 'text/html; charset=utf-8'),
        ]
        response_body = get_template('comment/fail.html').safe_substitute()
        response_status = 200
        return (response_body, response_headers, response_status)
