from urllib.parse import parse_qs
from string import join


def app(environ, start_response):
    qs = parse_qs(environ['QUERY_STRING'])
    start_response('200 OK', [
        ('Content-Type', 'text/plain')
    ])
    return join(['{}={}'.format(key, value) for key, value in qs.items()], '\n')
