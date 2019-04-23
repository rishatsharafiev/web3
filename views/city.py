import json
from utils.views import not_found

from repositories import CityRepository


class CityView:
    """City View"""
    
    @staticmethod
    def show(request, groups):
        """Show cities"""
        response_headers = [
            ('Content-Type', 'application/json; charset=utf-8'),
        ]
        request_method = request.environ.get('REQUEST_METHOD')
        region_id = groups.group('region_id')

        if request_method == 'GET' and region_id:
            cities = CityRepository.get_by_region_id(region_id=region_id)
            cities_dict = [city.entity_to_dict() for city in cities]
            response_status = 200
            response_body = json.dumps(cities_dict)
            return (response_body, response_headers, response_status)
        else:
            return not_found(request, groups)
