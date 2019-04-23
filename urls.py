from views import CityView, CommentView

url_patterns = (
    (r'^/comment$', CommentView.add),
    (r'^/city/(?P<region_id>\d+)$', CityView.show),
)
