#!/usr/bin/env python

import cgi
import wsgiref.handlers

from google.appengine.ext import webapp

class MainHandler(webapp.RequestHandler):
  def post(self):
    handle(self, 'POST')
  def get(self):
    handle(self, 'GET')

def handle(self, method):
  self.response.out.write("""
  <!DOCTYPE html>
  <title>FormData</title>
  <link rel="stylesheet" href="http://github.com/cheeaun/cacss/raw/master/ca.css">
  <style>
  table th,
  table td{
    border: 1px solid #ccc;
  }
  </style>
  <h1>FormData</h1>
  """)
  args = self.request.arguments()
  if len(args):
    self.response.out.write("""
    <table>
    <caption>""" + method + """ form data</caption>
    <thead>
    <tr>
      <th>Param</th>
      <th>Value</th>
    </tr>
    </thead>
    <tbody>
    """)
    for arg in args:
      multiArgs = self.request.get(arg, allow_multiple=True)
      for margs in multiArgs:
        self.response.out.write('<tr><td>' + arg + '</td><td>' + cgi.escape(margs) + '</td>')
    self.response.out.write("""
    </tbody>
    </table>
    <script>
    if (history.length>1) document.write('<a href="javascript:history.back(1);">&laquo; Back</a> &middot; ')
    </script>
    <a href="/">Home</a></p>
    """)
  else:
    self.response.out.write("""
    <p><strong>A simple service to display POST and GET (form) data.</strong></p>
    <p>Try these:</p>
    <dl>
      <dt>GET</dt>
      <dd><a href="/?a=1&amp;b=2">/?a=1&amp;b=2</a></dd>
      <dt>POST</dt>
      <dd>
        <form action="/" method="post">
          <label>a: <input type="text" name="a" value="1"></label>
          <label>b: <input type="text" name="b" value="2"></label>
          <input type="submit">
        </form>
      </dd>
    </dl>
    <p>This is <a href="http://github.com/cheeaun/FormData">open-sourced</a>.</p>
    """)

def main():
  application = webapp.WSGIApplication([('/', MainHandler)],
                                       debug=True)
  wsgiref.handlers.CGIHandler().run(application)

if __name__ == '__main__':
  main()
