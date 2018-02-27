from django import template
from django.template.defaultfilters import cut

from song.models import Song

register = template.Library()


def ellipsis_line(value, arg):
    lines = value.splitlines()
    if len(lines) > arg:
        return '\n'.join(lines[:arg + 1] + ['...'])
    return value


register.filter('ellipsis_line', ellipsis_line)
