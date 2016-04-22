#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from pyramid.config import Configurator
from pyramid.response import Response
from pyramid.view import view_config
from waitress import serve
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
    config = Configurator()
    config.add_route('root', '/')
    config.add_route('health', '/health')
    config.add_view(rootHandler, route_name='root', renderer='json')
    config.add_view(healthHandler, route_name='health', renderer='json')
    app = config.make_wsgi_app()
    serve(app, host='0.0.0.0', port=PORT_NUMBER)
