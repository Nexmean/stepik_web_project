from urllib.parse import parse_qs


def app(environ, start_response):
    qs = parse_qs(environ['QUERY_STRING'])
    start_response('200 OK', [
        ('Content-Type', 'text/plain')
    ])

    result = ''
    for key, values in qs.items():
        for value in values:
            result += '{}={}\n'.format(key, value)

    return [bytes(result)]
