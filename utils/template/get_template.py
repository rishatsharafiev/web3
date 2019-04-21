import os
from string import Template

from settings import TEMPLATE_DIR


def get_template(template_name):
    """Load template from file"""
    abs_path = os.path.join(TEMPLATE_DIR, template_name)
    with open(abs_path, 'r') as template:
        return Template(template.read())
