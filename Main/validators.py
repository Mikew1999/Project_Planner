import re


def is_valid_html_color(color: str):
    return bool(re.compile(r'^#(?:[0-9a-fA-F]{3}){1,2}$').match(color))