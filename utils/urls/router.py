import re
from utils.views import internal_error, not_found


def router(url_patterns, path_info, request):
    try:
        for item in url_patterns:
            pattern, handler = item
            groups = re.search(pattern, path_info)
            if groups:
                return handler(request, groups)
    except Exception as exp:
        print('Error: {exp}'.format(exp=exp))
        return internal_error(request, groups)
    return not_found(request, groups)
