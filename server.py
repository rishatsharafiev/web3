#!/usr/bin/env python3

from wsgiref.simple_server import make_server

from wsgi import application

httpd = make_server('localhost', 8051, application)
httpd.serve_forever()
