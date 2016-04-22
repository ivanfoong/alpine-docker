#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config
import consul

PORT_NUMBER = 4000

c = consul.Consul()

def rootHandler(request):
    body = {"services": []}
    (_, services) = c.catalog.services()
    for serviceName in services:
        (_, nodes) = c.catalog.service(serviceName)
        for node in nodes:
            body["services"].append(node)
    return body

def healthHandler(request):
    return {"status": 1}

if __name__ == '__main__':
    try:
        config = Configurator()
        config.add_route('root', '/')
        config.add_route('health', '/health')
        config.add_view(rootHandler, route_name='root', renderer='json')
        config.add_view(healthHandler, route_name='health', renderer='json')
        app = config.make_wsgi_app()
        server = make_server('0.0.0.0', PORT_NUMBER, app)
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down the web server'
        server.socket.close()
