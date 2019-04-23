from utils.views import method_not_allowed
from utils.template import get_template

from repositories import CityRepository, RegionRepository


class StatView:
    """Stat View"""
    
    @staticmethod
    def regions(request, groups):
        """Show regions"""
        response_headers = [
            ('Content-Type', 'text/html; charset=utf-8'),
        ]
        request_method = request.environ.get('REQUEST_METHOD')

        if request_method == 'GET':
            region_entities = RegionRepository.get_stat()
            item_template = get_template('comment/region_tr.html')
            content = [item_template.safe_substitute(**{
                'id': region.id,
                'name': region.name,
                'comment_count': region.comment_count,
            }) for region in region_entities]

            response_context = {
                'content': "".join(content)
            }
            response_body = get_template('comment/region_stat.html').safe_substitute(**response_context)
            response_status = 200
            return (response_body, response_headers, response_status)
        else:
            return method_not_allowed(request, groups)

    @staticmethod
    def cities(request, groups):
        """Show cities"""
        response_headers = [
            ('Content-Type', 'text/html; charset=utf-8'),
        ]
        request_method = request.environ.get('REQUEST_METHOD')
        region_id = groups.group('region_id')

        if request_method == 'GET':
            city_entities = CityRepository.get_stat(region_id=region_id)
            item_template = get_template('comment/city_tr.html')
            content = [item_template.safe_substitute(**{
                'id': city.id,
                'name': city.name,
                'comment_count': city.comment_count,
            }) for city in city_entities]

            response_context = {
                'content': "".join(content)
            }
            response_body = get_template('comment/city_stat.html').safe_substitute(**response_context)
            response_status = 200
            return (response_body, response_headers, response_status)
        else:
            return method_not_allowed(request, groups)