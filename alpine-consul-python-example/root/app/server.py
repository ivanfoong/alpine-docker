#!/usr/bin/env python
# -*- coding: UTF-8 -*-

from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
import consul
import json

PORT_NUMBER = 4000

#This class will handles any incoming request from
#the browser 
class myHandler(BaseHTTPRequestHandler):

  #Handler for the GET requests
  def do_GET(self):
    c = consul.Consul()
    self.send_response(200)
    self.send_header('Content-type','application/json')
    self.end_headers()
    body = {"services": []}
    (_, services) = c.catalog.services()
    for serviceName in services:
      (_, nodes) = c.catalog.service(serviceName)
      for node in nodes:
        body["services"].append(node)
    self.wfile.write(json.dumps(body, ensure_ascii=False))
    return

try:
  #Create a web server and define the handler to manage the
  #incoming request
  server = HTTPServer(('', PORT_NUMBER), myHandler)
  print 'Started httpserver on port ' , PORT_NUMBER

  #Wait forever for incoming htto requests
  server.serve_forever()
except KeyboardInterrupt:
  print '^C received, shutting down the web server'
  server.socket.close()
