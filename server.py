#!/usr/bin/env python3

from wsgiref.simple_server import make_server

from wsgi import application

from utils.db import migrate
migrate()

from settings import HOST, PORT

httpd = make_server(HOST, PORT, application)
httpd.serve_forever()
