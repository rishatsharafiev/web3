from views import CityView, CommentView

url_patterns = (
    (r'^/comment$', CommentView.add),
    (r'^/comment/success$', CommentView.success),
    (r'^/comment/fail$', CommentView.fail),
    (r'^/city/(?P<region_id>\d+)$', CityView.show),
)
