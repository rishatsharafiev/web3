from views import CommentView

url_patterns = (
    (r'^/comment$', CommentView.add),
)
