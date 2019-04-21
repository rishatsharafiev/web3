from views import test

url_patterns = (
    (r'^/test/(?P<pk>\d+)$', test),
)