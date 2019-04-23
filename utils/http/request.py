class Request:
    def __init__(self, body='', query_parameters={}, form_input={}, environ={}):
        self.body = body
        self.query_parameters = query_parameters
        self.form_input = form_input
        self.environ = environ
