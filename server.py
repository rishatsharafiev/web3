#!/usr/bin/env python3

from wsgiref.simple_server import make_server

from wsgi import application

httpd = make_server('localhost', 8080, application)
httpd.serve_forever()