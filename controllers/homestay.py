import sys, os, cgi, datetime
sys.path.insert(0, os.path.abspath(
  os.path.join(os.path.dirname(__file__), '..', 'config')))
import env, homestay, rest 
from google.appengine.api import users
from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app
from google.appengine.ext.webapp import template

class MainPage(webapp.RequestHandler):
  def get(self):
    self.response.out.write('Hello, ia ma  ')
  def post(self):
    h = homestay.Homestay()
    h.name = self.request.get('name')
    h.link = self.request.get('link')
    h.email = self.request.get('email')
    #h.status = self.request.get('status')
    h.status = 'invalid'
    h.create_at = datetime.datetime.now()
    h.put
    self.response.out.write('Hello ', h.name)

    
class NewPage(webapp.RequestHandler):
  def get(self):
    template_values = {
      'layout': rest.layout_path('homestay'), 
      'greetings': ['a','2','e']
      }
    self.response.out.write(
        template.render(rest.view_path(__file__, 'new'),
      template_values))

application = webapp.WSGIApplication(
                                     [('/homestay', MainPage),
                                      ('/homestay/new', NewPage)
                                     ],
                                     debug=True)

def main():
  run_wsgi_app(application)

if __name__ == "__main__":
  main()
