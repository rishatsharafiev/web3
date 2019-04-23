import os

BASE_DIR = os.path.dirname(__file__)
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')
STATIC_ROOT = 'static'
DATABASE_NAME = 'database.sqlite3'
DATABASE_PATH = os.path.join(BASE_DIR, DATABASE_NAME)
DATABASE_MIGRATE_NAME = 'database.sql'
DATABASE_MIGRATE_PATH = os.path.join(BASE_DIR, DATABASE_MIGRATE_NAME)
HOST = 'localhost'
PORT = 8080
