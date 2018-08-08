from urllib.parse import parse_qs


def app(environ, start_response):
    qs = parse_qs(environ['QUERY_STRING'])
    start_response('200 OK', [
        ('Content-Type', 'text/plain')
    ])
    return ['{}={}'.format(key, value) for key, value in qs.items()]
