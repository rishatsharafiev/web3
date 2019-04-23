from views import StatView, CityView, CommentView

url_patterns = (
    (r'^/view/$', CommentView.index),
    (r'^/comment/$', CommentView.add),
    (r'^/comment/(?P<comment_id>\d+)/remove/$', CommentView.remove),
    (r'^/comment/success/$', CommentView.success),
    (r'^/comment/fail/$', CommentView.fail),
    (r'^/city/(?P<region_id>\d+)/$', CityView.show),
    (r'^/stat/$', StatView.regions),
    (r'^/stat/(?P<region_id>\d+)/$', StatView.cities),
)
